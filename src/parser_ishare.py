import io
import xml.etree.cElementTree as ET

class ParserIShare:
    _ns = {"doc": "urn:schemas-microsoft-com:office:spreadsheet"}

    @staticmethod
    def _getvalueofnode(node):
        """ return node text or None """
        return node.text if node is not None else None

    @classmethod
    def _get_cell_value(cls, node, col):
        return cls._getvalueofnode(node.find(f'doc:Cell[{col}]/doc:Data', cls._ns))
    
    @staticmethod
    def _is_float(element) -> bool:
        try:
            float(element)
            return True
        except ValueError:
            return False

    @classmethod
    def _get_header(cls, row):
        ticker_col = None
        name_col = None
        weight_col = None
        for col in range(1, 10):
            cell_value = cls._get_cell_value(row, col)
            if cell_value:
                if "Name" in cell_value:
                    name_col = col
                if "Ticker" in cell_value:
                    ticker_col = col
                if "Weight" in cell_value:
                    weight_col = col
        return ticker_col, name_col, weight_col


    @classmethod
    def _get_ticker(cls, node, col, name, cache):
        if col: 
            ticker = cls._get_cell_value(node, col)
        elif cache is not None:
            ticker = cache.get_ticker(name)
        else:
            ticker = name
        if cache is not None:
            cache.set_cache(ticker, name)
        return ticker

    @classmethod
    def get_data(cls, data, cache=None):
        res = {}
        ticker_col = None
        name_col = None
        weight_col = None
        with io.open(data, 'rt', encoding='utf_8_sig') as f:
            xml_data = f.read()
            xml_data = xml_data.replace("&", "&#38;")
            tree = ET.ElementTree(ET.fromstring(xml_data))
        root = tree.getroot().find(".//doc:Worksheet[@doc:Name='Holdings']", cls._ns)
        for node in root.findall('.//doc:Row', cls._ns):
            if weight_col is None:
                ticker_col, name_col, weight_col = cls._get_header(node)
                continue

            weight = cls._get_cell_value(node, weight_col)
            name = cls._get_cell_value(node, name_col)
            ticker = cls._get_ticker(node, ticker_col, name, cache)

            if weight and cls._is_float(weight) and float(weight) > 0:
                weight = float(weight)/100
                if ticker in res:
                    res[ticker] += weight
                else:
                    res[ticker] = weight
        return res