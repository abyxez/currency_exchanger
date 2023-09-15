import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse


def get_exchange_list_xrates(currency, amount=1):
    content = requests.get(
        f"https://www.x-rates.com/table/?from={currency}&amount={amount}"
    ).content
    soup = bs(content, "html.parser")
    price_datetime = parse(
        soup.find_all("span", attrs={"class": "ratesTimestamp"})[1].text
    )
    exchange_tables = soup.find_all("table")
    exchange_rates = {}

    for exchange_table in exchange_tables:
        for tr in exchange_table.find_all("tr"):
            tds = tr.find_all("td")
            if tds:
                currency = tds[0].text
                exchange_rate = float(tds[1].text)
                exchange_rates[currency] = exchange_rate
    return price_datetime, exchange_rates
