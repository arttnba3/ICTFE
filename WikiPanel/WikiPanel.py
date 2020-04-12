import os

from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets, QtWebEngine, QtWebEngineCore
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from PyQt5 import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
import platform


class WikiPanel(QtWidgets.QWidget):
    def __init__(self):
        super(WikiPanel, self).__init__()
        self.WikiBrowserPanel = WikiBrowserPanelWidget(self)
        self.WikiBrowserPanel.setObjectName('WikiBrowserPanel')
        self.WikiBrowserPanel.setStyleSheet('background-color: transparent;')
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.addWidget(self.WikiBrowserPanel)
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.Layouts)


class WikiBrowserPanelWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WikiBrowserPanelWidget, self).__init__(parent)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        pwd = os.getcwd()
        pwd = pwd.replace('\\', '/')
        self.browser.load(QtCore.QUrl(
            'file:///' + pwd + '/Resources/Wiki/index.html'))
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.addWidget(self.browser)
        self.Layouts.setSpacing(0)
        self.Layouts.setContentsMargins(0, 0, 0, 0)
        self.browser.urlChanged.connect(lambda link: self.SuitLocalWiki(link))
        self.browser.show()
        self.browser.setZoomFactor(1.1)
        self.setLayout(self.Layouts)
        osinfo = platform.system()
        if osinfo == 'Windows':
            self.browser.settings().setFontFamily(QWebEngineSettings.StandardFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.FixedFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.SerifFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.SansSerifFont, '微软雅黑')
            self.browser.settings().setFontFamily(QWebEngineSettings.CursiveFont, '微软雅黑')
        self.shortcutd = QShortcut(QKeySequence("Ctrl+="), self)
        self.shortcutd.activated.connect(self.zoom_in_func)
        self.shortcutu = QShortcut(QKeySequence("Ctrl+-"), self)
        self.shortcutu.activated.connect(self.zoom_out_func)

    def zoom_in_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1)

    def zoom_out_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1)

    def SuitLocalWiki(self, qlink):
        link = qlink.toString()
        if link[-1] == '/':
            link += 'index.html'
            out = QtCore.QUrl(link)
            self.browser.load(QtCore.QUrl(out))
