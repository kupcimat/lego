import asyncio
import csv
import logging
from dataclasses import asdict
from typing import List

from aiohttp import ClientSession

from kupcimat.currency import get_exchange_rates
from kupcimat.product import Product, download_countries
from kupcimat.query import Country
from kupcimat.utils import field_names

logging.basicConfig(level=logging.DEBUG)


def write_to_csv(products: List[Product], file_name: str):
    with open(file_name, "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=field_names(Product))
        csv_writer.writeheader()
        csv_writer.writerows([asdict(product) for product in products])


async def main():
    async with ClientSession() as session:
        exchange_rates = await get_exchange_rates(session, base_currency="EUR")
        products = await download_countries(session, list(Country), concurrency=5)
        for product in products:
            product.normalize_price(exchange_rates)
        write_to_csv(products, "products.csv")


if __name__ == "__main__":
    asyncio.run(main())
