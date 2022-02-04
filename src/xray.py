class XRay:
    def get_results(holdings, funds_data, currency):
        res = {}
        total = 0
        for ticker, holding in holdings.items():
            if ticker in funds_data:
                for share, weight in funds_data[ticker].items():
                    if weight > 0:
                        share_price = holding["quantity"] * holding["price"] * weight * currency[holding["currency"]]
                        total += share_price
                        if share in res:
                            res[share] += share_price
                        else:
                            res[share] = share_price
        res_sorted = {k: v for k, v in sorted(res.items(), reverse=True, key=lambda item: item[1])}
        return res_sorted, total