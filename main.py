import asyncio
import logging
from dataclasses import asdict, dataclass
from typing import Any, Dict, List

import aiohttp

from constants import OPERATION_NAME, QUERY, query_variables

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
            price=product["variant"]["price"]["centAmount"],
            price_text=product["variant"]["price"]["formattedAmount"],
            currency=product["variant"]["price"]["currencyCode"],
        )
        for product in products
    ]


async def main():
    url = "https://www.lego.com/api/graphql/ContentPageQuery"
    query = Query(
        operationName=OPERATION_NAME,
        query=QUERY,
        variables=query_variables(page=0, limit=10),
    )
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-locale": "cs-CZ",
        "x-lego-request-id": "my-request-id",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=asdict(query), headers=headers) as response:
            logging.info(f"action=get-data status={response.status}")
            data = await response.json()
            products = extract_products(data)
            for product in products:
                print(product)


asyncio.run(main())
