# SB - Safe Browser (written in Py)

The sample for making a fully functional web browser which contains no user information and is perfectly safe to use with the usage of Python library - **PyQt5.**

# Introductory Part: *what is PyQt?*

**PyQt5** is a library that lets you use the *Qt application framework from Python*. Qt is a popular cross-platform application framework that is widely used for developing graphical user interface (GUI) applications. PyQt5 allows you to use the Qt application framework from Python, providing a convenient interface for Python programmers to create graphical user interfaces, games, and other multimedia applications. It is implemented as a set of Python modules and contains hundreds of classes and functions that you can use to create a wide variety of applications. PyQt5 is available under the GPL and commercial licenses.

# How does it work?

**SOURCE CODE:**
```
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.url_loader)
        self.viewport = QWebEngineView()
        self.setCentralWidget(self.viewport)
        self.addToolBar(self.address_bar)

    def url_loader(self):
        url = self.address_bar.text()
        self.viewport.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = BrowserWindow()
window.show()
sys.exit(app.exec_())
```
This written above program creates a **simple web browser application using PyQt5**. It defines a BrowserWindow class that subclasses QMainWindow, which is a main application window in Qt. The BrowserWindow class has a QLineEdit widget called address_bar that is used as an address bar for the web browser, and a QWebEngineView widget called viewport that is used to display web pages. The __init__ method (main initialization) of the BrowserWindow class sets up the layout of the window, adds the address_bar and viewport widgets to the window, and connects the returnPressed signal of the address_bar widget to the url_loader method. The url_loader method is called when the user presses the Enter key while typing in the address bar. It retrieves the text entered in the address bar and uses it to set the URL of the viewport widget using the setUrl method. The code creates an instance of QApplication and a BrowserWindow object, shows the window, and enters the loop.

Thank you for reading.
