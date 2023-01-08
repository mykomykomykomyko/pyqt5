import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)
        self.viewport = QWebEngineView()
        self.setCentralWidget(self.viewport)
        self.addToolBar(self.address_bar)
    def load_url(self):
        url = self.address_bar.text()
        self.viewport.setUrl(QUrl(url))
app = QApplication(sys.argv)
window = BrowserWindow()
window.show()
sys.exit(app.exec_())
