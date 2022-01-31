import requests
from config import data_source, holdings, currency, always_report
from urllib.parse import urlparse
from ticker_cache import TickerCache
  
all_data = {}


def is_url(url):
    return urlparse(url).scheme != ""

def print_result(cache):
    res = {}
    total = 0
    for ticker, holding in holdings.items():
        if ticker in all_data:
            for share, weight in all_data[ticker].items():
                if weight > 0:
                    share_price = holding["quantity"] * holding["price"] * weight * currency[holding["currency"]]
                    total += share_price
                    if share in res:
                        res[share] += share_price
                    else:
                        res[share] = share_price
    res_sorted = {k: v for k, v in sorted(res.items(), reverse=True, key=lambda item: item[1])}
    for ticker, value in list(res_sorted.items())[:50]:
        name = cache.get_name(ticker)
        print(f"{ticker:10}\t{name:50}\t{value:10,.2f}\t{100*value/total:10,.2f}%")
    print("---")
    for ticker in always_report:
        name = cache.get_name(ticker)
        value = res_sorted[ticker]
        print(f"{ticker:10}\t{name:50}\t{value:10,.2f}\t{100*value/total:10,.2f}%")
    print("---")
    print(f"Total holdings: {total:,.2f}")

def fetch_data():
    cache = TickerCache()
    for etf_code, etf_data in data_source.items():
        if is_url(etf_data["source"]):
            ret = requests.get(etf_data["source"])
            ret.raise_for_status()
            data = ret.content
        else:
            data = etf_data["source"]
        all_data[etf_code] = etf_data["parser"].get_data(data, cache)
    print_result(cache)

if __name__ == "__main__":
    fetch_data()