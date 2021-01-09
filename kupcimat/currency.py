from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Dict

from aiohttp import ClientSession


@dataclass
class ExchangeRates:
    base: str
    date: str
    rates: Dict[str, float]

    def __init__(self, base: str, date: str, rates: Dict[str, float]):
        self.base = base
        self.date = date
        self.rates = defaultdict(lambda: 0.0, rates)
        self.rates[self.base] = 1.0


def extract_rates(json_data: Any) -> ExchangeRates:
    return ExchangeRates(
        base=json_data["base"], date=json_data["date"], rates=json_data["rates"]
    )


async def get_exchange_rates(
    session: ClientSession, base_currency: str = "EUR"
) -> ExchangeRates:
    url = "https://api.exchangeratesapi.io/latest?base=EUR"
    params = {"base": base_currency}

    async with session.get(url, params=params) as response:
        data = await response.json()
        return extract_rates(data)
