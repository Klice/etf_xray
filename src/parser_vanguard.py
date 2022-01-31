import pandas as pd

class ParserVanguard:
    @staticmethod
    def format_number(num):
        return float(num[:-1])/100


    @staticmethod
    def name_to_ticker(name, cache):
        name = str(name).upper()
        ticker = cache.get_ticker(name)
        if ticker == name:
            ticker = cache.find_ticker(name)
        cache.set_cache(ticker, name)
        return ticker

    @classmethod
    def get_data(cls, data, cache=None):
        df = pd.read_excel(io=data, header=5, usecols=[0, 1], skipfooter=3, sheet_name="Holding_Details")
        df["weight"] = df[r"% of Market Value"].apply(cls.format_number)
        df = df[df["weight"] > 0]
        df["ticker"] = df[r"Holding Name"].apply(cls.name_to_ticker, args=(cache,))
        res = df[["ticker", "weight"]].set_index('ticker').groupby(level=0).sum().to_dict(orient="index")
        return {k: v["weight"] for k,v in res.items()}