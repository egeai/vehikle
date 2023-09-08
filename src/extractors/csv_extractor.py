from typing import Any

import pandas as pd
from .extractor_interface import DataExtractor  # type: ignore


class CsvExtractor(DataExtractor):
    def extract(self, file_path: str) -> Any:  # type: ignore
        return pd.read_csv(file_path)
