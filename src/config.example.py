from parser_ishare import ParserIShare
from parser_vanguard import ParserVanguard
from parser_vanguard_csv import ParserVanguardCSV
from fetcher_local import FetcherLocal


data_source = {
    "AOR": {
        "source": r"..\\ETF\\iShares-Core-Growth-Allocation-ETF_fund.xls",
        "parser": ParserIShare,
        "fetcher": FetcherLocal
    },
    "VTI": {
        "source": r"..\\ETF\\VTI_Holdings_details_Total_Stock_Market_ETF.csv",
        "parser": ParserVanguardCSV,
        "fetcher": FetcherLocal
    },
    "VMO": {
        "source": r"..\\ETF\Holding_Details_VMO.xlsx",
        "parser": ParserVanguard,
        "fetcher": FetcherLocal
    }
}
currency = {
    "CAD": 1,
    "USD": 1.28
}

always_report = [
    "WEED",
    "MRNA",
]

holdings = {
    "AOR": {
        "quantity": 175,
        "price": 54.49,
        "currency": "USD"
    },
    "VTI": {
        "quantity": 20,
        "price": 222.03,   
        "currency": "USD"
    },
    "VMO": {
        "quantity": 21,
        "price": 43.18, 
        "currency": "CAD"
    }
}