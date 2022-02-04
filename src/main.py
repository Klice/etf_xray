from config import data_source, holdings, currency, always_report
from output_print import OutputPrint
from xray import XRay
from ticker_cache import TickerCache
  
all_data = {}


def fetch_data():
    cache = TickerCache()
    for etf_code, etf_data in data_source.items():
        data = etf_data["fetcher"].get_data(etf_data["source"])
        all_data[etf_code] =  etf_data["parser"].get_data(data, cache)
    
    xray, total = XRay.get_results(holdings, all_data, currency)
    OutputPrint.output_result(xray, total, always_report, cache)


if __name__ == "__main__":
    fetch_data()