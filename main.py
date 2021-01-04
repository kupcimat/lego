import asyncio
import csv
import logging
from dataclasses import asdict, dataclass
from typing import Any, Dict, List

from aiohttp import ClientSession

from kupcimat.query import Country, create_headers, create_query
from kupcimat.utils import field_names

logging.basicConfig(level=logging.DEBUG)


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


def extract_products(json_data: Any, country: Country) -> List[Product]:
    sections = [
        section
        for section in json_data["data"]["contentPage"]["sections"]
        if "products" in section
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
            country=country.name,
        )
        for product in products
    ]


def write_to_csv(products: List[Product], file_name: str):
    with open(file_name, "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=field_names(Product))
        csv_writer.writeheader()
        csv_writer.writerows([asdict(product) for product in products])


async def download_page(
    session: ClientSession, country: Country, page: int
) -> List[Product]:
    url = "https://www.lego.com/api/graphql/ContentPageQuery"
    query = create_query(page, limit=20)
    headers = create_headers(country)

    async with session.post(url, json=asdict(query), headers=headers) as response:
        logging.info(
            f"action=download country={country.name} page={page} status={response.status}"
        )
        data = await response.json()
        return extract_products(data, country)


async def download_products(
    session: ClientSession, country: Country, page: int = 0
) -> List[Product]:
    products = await download_page(session, country, page)
    if len(products) == 0:
        return products
    else:
        return products + await download_products(session, country, page + 1)


async def main():
    async with ClientSession() as session:
        products = await download_products(session, Country.CZ)
        write_to_csv(products, "products.csv")


asyncio.run(main())
