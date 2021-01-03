import asyncio
import logging
from dataclasses import asdict, dataclass
from typing import Any, Dict

import aiohttp

from query import VARIABLES, QUERY

logging.basicConfig(level=logging.DEBUG)


@dataclass
class Query:
    operationName: str
    query: str
    variables: Dict[str, Any]


async def main():
    url = "https://www.lego.com/api/graphql/ContentPageQuery"
    query = Query(
        operationName="ContentPageQuery",
        query=QUERY,
        variables=VARIABLES,
    )
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-locale": "cs-CZ",
        "x-lego-request-id": "my-request-id",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=asdict(query), headers=headers) as response:

            # print("Status:", response.status)
            data = await response.text()
            print(data)


asyncio.run(main())
