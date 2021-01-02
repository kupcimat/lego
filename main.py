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
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.lego.com/cs-cz/categories/new-sets-and-products",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InB1YiI6e30sInB2dCI6IjR5bUN0aHppQ0liNHhVSlJIbklLbmlJRU9pNGhWdVJTc2plcHUyT0hVUEJRcVNrRzhZM2lGZDRxNThBTVd3SjNhM0lZL1BJNnNhbkJoZjVEYkw2VVRPRkpzZTQvYzJadmcrbEZZb1FlYmNvckdpeUZFMnZJdmx1UnNxaGxJRXg0RUxqS0g3c3pWS0t3V3ZJZWQ2Tk5zckdmVjVnTFV4b3JyVmRDbllhMWxMdktPVTZzR0VkMmZnWk5VYVNnZGRVNFlhMGhGOWlYZHlQUVNuZUh0eExSbE1CbkZpMFJyUEN4UXo5Q1VvczNFWkU1YVVQZFhqUUpnNGdRejJ1Si9XVFdpTER5bE9nc24zK3lSbnppSzl3MW1pdmtRWmpjdlE5MVFQUlNXR1g3WWR1RFh1NkR0ZFpoNGVKV3pvME1sZHdzc3F2dHp6eVppV0E4dDNISEFKeGhWdVFpTTVWUTJlU3N5NjRBMjEvMExvb3dPMnRNd2xqVFhCRzJWejl1OHJmczFxUHNyR0VZM21YQ0hOVEYzdTVjWDJiTERPZFZLMWVMRU9qSmQ4YWh4WjJHNmVSWXkvZmxWd0w3OG5TUUpxZWxjNWIwQ3Jya2FjYkVxWm04dlNnU3JxWXZGTzc1K2o5NjNnbldCMSs0c2ZqeFcxZjBzSlNsSlYzWGVYay9kOEczeHlkK05KbWVkcTNGTVgxdTBzT0hXRStJMnQ4K2VvL2FkUHhSb3hrdFBCcz0uSVZXbXNITUZnSktidEZoeGpPUyszQT09In0sImlhdCI6MTYwOTYwODA4MSwiZXhwIjoxNjA5NzgwODgxfQ.MXCvevMF9z8dImxgmMxpFRjaiyG0d_41FfR5nnScw8I",
        "content-type": "application/json",
        "features": "rewardsCenter=false",
        "lid": "",
        "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE3NDY4NzEiLCJhcCI6IjEwMzI0NzQ2OCIsImlkIjoiNzRjNTFlY2Q4NzcwMWUxZiIsInRyIjoiZmE1YmU0MjYyZDViYjJjNzM1NmQ0ZWQ1ZDNhMTkwMTAiLCJ0aSI6MTYwOTYwODA4NDkzMH19",
        "session-cookie-id": "vGhcFWIm3na6D9xg4-uyl",
        "traceparent": "00-fa5be4262d5bb2c7356d4ed5d3a19010-74c51ecd87701e1f-01",
        "tracestate": "1746871@nr=0-1-1746871-103247468-74c51ecd87701e1f----1609608084930",
        "x-lego-request-id": "b2f2b1e8-1954-43a4-a139-f5195c2e0e6c-shop-c",
        "x-locale": "cs-CZ",
        "Origin": "https://www.lego.com",
        "DNT": "1",
        "Connection": "keep-alive",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=asdict(query), headers=headers) as response:

            # print("Status:", response.status)
            data = await response.text()
            print(data)


asyncio.run(main())
