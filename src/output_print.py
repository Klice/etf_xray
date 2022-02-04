class OutputPrint:

    def output_result(xray_results, total, always_report, cache):
        for ticker, value in list(xray_results.items())[:50]:
            name = cache.get_name(ticker)
            print('\t'.join([
                f"{ticker:10}",
                f"{name:50}",
                f"{value:10,.2f}",
                f"{100*value/total:10,.2f}%"
            ]))
        print("---")
        for ticker in always_report:
            name = cache.get_name(ticker)
            value = xray_results[ticker]
            print(f"{ticker:10}\t{name:50}\t{value:10,.2f}\t{100*value/total:10,.2f}%")
        print("---")
        print(f"Total holdings: {total:,.2f}")