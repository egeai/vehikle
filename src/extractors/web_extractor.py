from typing import Any

from scrapy import Selector  # type: ignore
from .extractor_interface import DataExtractor  # type: ignore
import requests  # type: ignore


class WebExtractor(DataExtractor):
    def extract(self, url: str) -> Any:
        response = requests.get(url=url)
        selector = Selector(response=response)
        # Extraction logic with Scrapy's Selector
        # For example: titles = selector.css('title::text').getall()
        return "Web Data"