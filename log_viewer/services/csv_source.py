import csv
from typing import List
from interfaces.data_source import ILogSource

class CsvLogSource(ILogSource):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_logs(self) -> List[str]:
        logs = []
        try:
            with open(self.filepath, mode='r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    logs.append(" | ".join(row)) 
            return logs
        except FileNotFoundError:
            return ["Error: CSV File not found"]