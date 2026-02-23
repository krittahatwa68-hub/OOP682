import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from services.factory import SourceFactory

if __name__ == "__main__":
    app = QApplication(sys.argv)
    source = SourceFactory.create_source("csv") 
    window = MainWindow(source)
    window.resize(400, 300)
    window.show() 

    sys.exit(app.exec())