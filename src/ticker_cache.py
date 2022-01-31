class TickerCache:
    ticker_to_name = {}
    name_to_ticker = {
        "PROVINCE OF ONTARIO CANADA": "ONT",
        "CANADIAN GOVERNMENT BOND": "CAN"
    }

    def _get_varians(self, name):
        v1 = name.replace("&amp;", "&")
        v2 = v1.replace(".", "").replace("-", " ").replace("CLASS A", "").strip()
        v3 = v2.replace("INC", "").strip()
        return [v1, v2, v3]

    def get_name(self, ticker):
        return self.ticker_to_name.get(ticker, None)

    def get_ticker(self, name):
        name = self._get_varians(name)[0]
        return self.name_to_ticker.get(name, name)

    def find_ticker(self, name):
        names = self._get_varians(name)
        for t_name, t_ticker in self.name_to_ticker.items():
            for n in names:
                if n in t_name:
                    return t_ticker
        return name

    def set_cache(self, ticker, name):
        name = self._get_varians(name)[0]
        self.ticker_to_name[ticker] = name
        self.name_to_ticker[name] = ticker
