import asyncio
import logging
from dataclasses import dataclass
from typing import Any, List

from aiohttp import ClientSession

from kupcimat.query import Country, create_headers, create_query
from kupcimat.utils import flatten

DOWNLOAD_LIMIT = 20


@dataclass
class Product:
    code: str
    name: str
    availability: str
    availability_text: str
    max_order_quantity: int
    price: float
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
            country=country.code,
        )
        for product in products
        if "variant" in product  # skip multi-variant products (clothing)
    ]


async def download_page(
    session: ClientSession, country: Country, page: int
) -> List[Product]:

    url = "https://www.lego.com/api/graphql/ContentPageQuery"
    query = create_query(page, limit=DOWNLOAD_LIMIT)
    headers = create_headers(country)

    async with session.post(url, json=query, headers=headers) as response:
        logging.info(
            f"action=download country={country.name} page={page} status={response.status}"
        )
        data = await response.json()
        try:
            return extract_products(data, country)
        except KeyError as error:
            logging.error(await response.text())
            raise error


async def download_products(
    session: ClientSession, country: Country, page: int = 0
) -> List[Product]:

    products = await download_page(session, country, page)
    if len(products) == 0:
        return products
    else:
        return products + await download_products(session, country, page + 1)


async def download_countries(
    session: ClientSession, country_list: List[Country], concurrency: int
) -> List[Product]:
    country_lists = [
        country_list[i : i + concurrency]
        for i in range(0, len(country_list), concurrency)
    ]

    product_lists = []
    for countries in country_lists:
        download_tasks = [
            asyncio.create_task(download_products(session, country))
            for country in countries
        ]
        products = [await task for task in download_tasks]
        product_lists.extend(products)

    return flatten(product_lists)
