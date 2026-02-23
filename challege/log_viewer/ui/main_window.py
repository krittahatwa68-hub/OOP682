from PySide6.QtWidgets import QMainWindow, QListWidget, QVBoxLayout, QWidget
from interfaces.data_source import ILogSource
from abc import ABC, abstractmethod
from typing import List


class IFilterStrategy(ABC):
    @abstractmethod
    def filter(self, logs: List[str]) -> List[str]:
        pass

class ErrorOnlyFilter(IFilterStrategy):
    def filter(self, logs):
        return [l for l in logs if "ERROR" in l]

class NoFilter(IFilterStrategy):
    def filter(self, logs):
        return logs


class MainWindow(QMainWindow):
    def __init__(self, source: ILogSource):
        super().__init__()
        self.source = source  
        self.filter_strategy = NoFilter() 
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Log Viewer")
        self.list_widget = QListWidget()
        self.setCentralWidget(self.list_widget)
        self.load_data()

    def load_data(self):
        logs = self.source.get_logs()
        filtered_logs = self.filter_strategy.filter(logs)
        self.list_widget.addItems(filtered_logs)