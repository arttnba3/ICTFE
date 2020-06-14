#!/bin/python
import json
import sys
from time import sleep

from PyQt5 import QtGui, QtWidgets
from PyQt5.Qt import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

import MainWindow
from Config import Settings


class rMainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(rMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./Resources/icon.png'))
        self.m_flag = False

    def closeEvent(self, QCloseEvent):
        self.StatusThread.terminate()
        with open('UserConfig/paths.ctfe', 'w') as out:
            out.write(json.dumps({'GlobalPath': Settings.GlobalPath, 'PDFPath': Settings.PDFPath}))
        try:
            self.MainStackWindow.DataFlowPanelDock.close()
        except:
            pass
        super(rMainWindow, self).closeEvent(QCloseEvent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.MaxFlag is False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag and self.MaxFlag is False:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False


class SplashScreen(QtWidgets.QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QPixmap("./Resources/splash.png"))


if __name__ == "__main__":
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    sys.setrecursionlimit(1000000)
    splash = SplashScreen()
    splash.show()
    sleep(0.5)
    QtWidgets.qApp.processEvents()
    Win = rMainWindow()
    Win.setWindowTitle('ICTFE')
    # Win.TypeStack.setCurrentWidget(Win.WelcomeLabel)
    Win.show()
    Win.showMaximized()
    splash.finish(Win)
    font = QtGui.QFont()
    font.setFamily('文泉驿等宽微米黑')
    app.setFont(font)
    sys.exit(app.exec_())
