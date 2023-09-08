from .csv_extractor import CsvExtractor
from .web_extractor import WebExtractor


class ExtractorFactory:
    @staticmethod
    def get_extractor(source_type):
        if source_type == "csv":
            return CsvExtractor()
        elif source_type == "web":
            return WebExtractor()
        else:
            raise ValueError(f"Extractor not defined for {source_type}")