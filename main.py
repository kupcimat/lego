import asyncio
import csv
import logging
from dataclasses import asdict, dataclass
from typing import Any, Dict, List

from aiohttp import ClientSession

from constants import OPERATION_NAME, QUERY, query_variables
from utils import field_names

logging.basicConfig(level=logging.DEBUG)


@dataclass
class Query:
    operationName: str
    query: str
    variables: Dict[str, Any]


@dataclass
class Product:
    code: str
    name: str
    availability: str
    availability_text: str
    max_order_quantity: int
    price: int
    price_text: str
    currency: str
    country: str


def extract_products(json_data: Any) -> List[Product]:
    sections = [
        section
        for section in json_data["data"]["contentPage"]["sections"]
        if section["__typename"] == "DisruptorProductSection"
    ]
    products = sections[0]["products"]["results"]

    return [
        Product(
            code=product["productCode"],
            name=product["name"],
            availability=product["variant"]["attributes"]["availabilityStatus"],
            availability_text=product["variant"]["attributes"]["availabilityText"],
            max_order_quantity=product["variant"]["attributes"]["maxOrderQuantity"],
            price=product["variant"]["price"]["centAmount"] / 100,
            price_text=product["variant"]["price"]["formattedAmount"],
            currency=product["variant"]["price"]["currencyCode"],
            country="CZ",
        )
        for product in products
    ]


def write_to_csv(products: List[Product], file_name: str):
    with open(file_name, "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=field_names(Product))
        csv_writer.writeheader()
        csv_writer.writerows([asdict(product) for product in products])


async def download_page(session: ClientSession, page: int, limit: int) -> List[Product]:
    url = "https://www.lego.com/api/graphql/ContentPageQuery"
    query = Query(
        operationName=OPERATION_NAME,
        query=QUERY,
        variables=query_variables(page, limit),
    )
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-locale": "cs-CZ",
        "x-lego-request-id": "my-request-id",
    }

    async with session.post(url, json=asdict(query), headers=headers) as response:
        logging.info(
            f"action=download page={page} limit={limit} status={response.status}"
        )
        data = await response.json()
        return extract_products(data)


async def main():
    async with ClientSession() as session:
        products = await download_page(session, page=0, limit=10)
        write_to_csv(products, "out.csv")


asyncio.run(main())
