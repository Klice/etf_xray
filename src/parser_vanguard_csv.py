import pandas as pd

class ParserVanguardCSV:
    @staticmethod
    def format_number(num):
        if num[0] == "<":
            return 0
        try:
            return float(num[:-1])/100
        except ValueError:
            return None

    
    @classmethod
    def get_data(cls, data, cache=None):
        df = pd.read_csv(data, header=3, usecols=[2, 3, 4])
        df = df[df["TICKER"].notnull()]
        df["weight"] = df[r"% OF FUNDS*"].apply(cls.format_number)
        df = df[df["weight"] > 0]
        df.apply(lambda x: cache.set_cache(x["TICKER"], x["HOLDINGS"]), axis = 1)
        df = df.set_index('TICKER').groupby(level=0).sum()
        res = df.to_dict(orient="index")
        return {k: v["weight"] for k,v in res.items()}