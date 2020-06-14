from PyQt5 import QtWidgets, QtGui, QtCore

ButtonStyleNormal = "QPushButton{" \
                    "background-color:rgb(30, 30, 30);" \
                    "color: white;" \
                    "border-radius: 0px;" \
                    "border: 0px groove gray;" \
                    "border-style: outset;" \
                    "}" \
                    "QPushButton:hover{" \
                    "background-color: rgba(30, 30, 30, 100%);" \
                    "color: white;" \
                    "}" \
                    "QPushButton:pressed{" \
                    "background-color: rgb(40, 40, 40);" \
                    "border-style: inset; " \
                    "}"

ButtonStyleSelected = "QPushButton{" \
                      "background-color:rgba(40, 140, 255, 100%);" \
                      "color: white;" \
                      "border-radius: 0px;" \
                      "border: 0px groove gray;" \
                      "border-style: outset;" \
                      "}" \
                      "QPushButton:hover{" \
                      "background-color: rgba(60, 60, 255, 100%);" \
                      "color: white;" \
                      "}" \
                      "QPushButton:pressed{" \
                      "background-color: rgb(100, 100, 255);" \
                      "border-style: inset; " \
                      "}"
ButtonStyleBlue = "QPushButton{" \
                  "background-color:rgba(40, 140, 255, 100%);" \
                  "color: white;" \
                  "border-radius: 0px;" \
                  "border: 0px groove gray;" \
                  "border-style: outset;" \
                  "}" \
                  "QPushButton:hover{" \
                  "background-color: rgba(60, 60, 255, 100%);" \
                  "color: white;" \
                  "}" \
                  "QPushButton:pressed{" \
                  "background-color: rgb(100, 100, 255);" \
                  "border-style: inset; " \
                  "}"
ButtonStyleYellow = "QPushButton{" \
                    "background-color:rgba(240, 145, 40, 100%);" \
                    "color: white;" \
                    "border-radius: 0px;" \
                    "border: 0px groove gray;" \
                    "border-style: outset;" \
                    "}" \
                    "QPushButton:hover{" \
                    "background-color: rgba(160, 145, 60, 100%);" \
                    "color: white;" \
                    "}" \
                    "QPushButton:pressed{" \
                    "background-color: rgb(160, 115, 60);" \
                    "border-style: inset; " \
                    "}"
ButtonStyleRed = "QPushButton{" \
    "background-color:rgba(250, 40, 155, 100%);" \
    "color: white;" \
    "border-radius: 0px;" \
    "border: 0px groove gray;" \
    "border-style: outset;" \
    "}" \
    "QPushButton:hover{" \
    "background-color: rgba(255, 60, 60, 100%);" \
    "color: white;" \
    "}" \
    "QPushButton:pressed{" \
    "background-color: rgb(100, 100, 255);" \
    "border-style: inset; " \
    "}"
ButtonStyleGreen = "QPushButton{" \
    "background-color:rgba(60, 180, 75, 100%);" \
    "color: white;" \
    "border-radius: 0px;" \
    "border: 0px groove gray;" \
    "border-style: outset;" \
    "}" \
    "QPushButton:hover{" \
    "background-color: rgba(60, 165, 60, 100%);" \
    "color: white;" \
    "}" \
    "QPushButton:pressed{" \
    "background-color: rgb(30, 225, 30);" \
    "border-style: inset; " \
    "}"
SplitterBlue = "QWidget{\n"\
    "background-color: rgba(40, 140, 255, 100%);\n"\
    "border: 1px rgba(40, 140, 255, 100%);\n"\
    "border-style: solid;\n"\
    "}"
SplitterRed = "QWidget{\n"\
    "background-color: rgba(250, 40, 155, 100%);\n"\
    "border: 1px rgba(250, 40, 155, 100%);\n"\
    "border-style: solid;\n"\
    "}"
SplitterYellow = "QWidget{\n"\
    "background-color: rgba(240, 145, 40, 100%);\n"\
    "border: 1px rgba(240, 145, 40, 100%);\n"\
    "border-style: solid;\n"\
    "}"
SplitterGreen = "QWidget{\n"\
    "background-color: rgba(60, 180, 75, 100%);\n"\
    "border: 1px rgba(60, 180, 75, 100%);\n"\
    "border-style: solid;\n"\
    "}"
ButtonStyles = [ButtonStyleBlue, ButtonStyleGreen,
                ButtonStyleRed, ButtonStyleYellow]
SplitterStyles = [SplitterBlue, SplitterGreen, SplitterRed, SplitterYellow]


class ICTFESplitter(QtWidgets.QSplitter):
    def __init__(self, parent=None):
        super(ICTFESplitter, self).__init__(parent)
        self.setStyleSheet("QSplitter::handle {"
                           "background-color: rgb(30, 30, 30);"
                           "}"
                           "QSplitter::handle:horizontal {"
                           "width: 3px;"
                           "}"
                           "QSplitter::handle:vertical {"
                           "height: 3px;"
                           "}"
                           "QSplitter::handle:pressed {"
                           "background-color: rgb(50, 250, 150);"
                           "}"
                           "QSplitter::handle:hover {"
                           "background-color: rgb(50, 150, 250);"
                           "}")


class ICTFEButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(ICTFEButton, self).__init__(parent)
        self.setMinimumSize(120, 32)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(RPushButtonDarkStyle)


class ICTFETextBox(QtWidgets.QTextEdit):
    def __init__(self, parent=None):
        super(ICTFETextBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet('QTextEdit{background-color: rgb(20,20,20); color: rgb(200, 200, 200);}'+ScrollBarStyle)
        self.setTextColor(QtGui.QColor(200, 200, 200))
        self.setAcceptDrops(True)
        self.setAcceptRichText(False)


class ICTFELineBox(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(ICTFELineBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            'color: white;'
            'border: 2px solid gray;'
            'border-radius: 2px;'
            'padding: 0 4px;'
            'background: rgb(30, 30, 30);'
            'selection-background-color: blue;')
        self.setDragEnabled(True)


class ICTFECheckBox(QtWidgets.QCheckBox):
    def __init__(self, parent=None):
        super(ICTFECheckBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            'QCheckBox:unchecked{ border:none; color: white; }'
            'QCheckBox:checked{ border:none; color: cyan; }')


class ICTFELabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(ICTFELabel, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet('color: white; background-color: rgb(30, 30, 30);')


class ICTFEList(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(ICTFEList, self).__init__(parent)
        self.setStyleSheet(
            'QListWidget{'
            'background-color: rgb(30, 30, 30);'
            'border: 1px solid rgb(50, 50, 50);'
            'color: white;'
            '}')
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setDragEnabled(True)
        self.setDefaultDropAction(QtCore.Qt.TargetMoveAction)

    def dragEnterEvent(self, e):
        e.accept()


class ICTFEScrollArea(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super(ICTFEScrollArea, self).__init__(parent)
        self.setStyleSheet(
            'QScrollArea{'
            'border: none;'
            'background-color:rgb(30, 30, 30);'
            '}')
        self.viewport().setStyleSheet(
            'QScrollArea{'
            'border: none;'
            'background-color:rgb(30, 30, 30);'
            '}')
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)


class PropertiesEditWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)


class BoolEditItem(QtWidgets.QWidget):
    def __init__(self, parent=None, name: str = ''):
        super().__init__(parent=parent, flags=QtCore.Qt.WindowFlags())
        layout = QtWidgets.QVBoxLayout()
        check = ICTFECheckBox()
        check.setText(name)
        layout.addWidget(check, alignment=QtCore.Qt.Alignment())
        self.setLayout(layout)


class LineEditItem(QtWidgets.QWidget):
    def __init__(self, parent=None, name: str = ''):
        super().__init__(parent=parent, flags=QtCore.Qt.WindowFlags())
        layout = QtWidgets.QHBoxLayout()
        label = ICTFELabel()
        label.setText(name)
        layout.addWidget(label, alignment=QtCore.Qt.Alignment())
        editbox = ICTFELineBox()
        layout.addWidget(editbox, alignment=QtCore.Qt.Alignment())
        self.setLayout(layout)


DockStyleSheet = '''
QDockWidget {
    border: 1px solid rgb(50, 50, 50);
    titlebar-close-icon: url(./Resources/closeDock.png);
    titlebar-normal-icon: url(./Resources/maxDock.png);
}

QDockWidget::title {
    text-align: left;
    background: rgb(60, 60, 60);
    min-height: 24px;
}

QDockWidget::close-button, QDockWidget::float-button {
    border: none;
    background: transparent;
    icon-size: 24px;
    padding: 0px;
}

QDockWidget::close-button:hover {
    background: rgb(250, 50, 50);
}

QDockWidget::float-button:hover {
    background: rgb(100, 100, 100);
}

QDockWidget::close-button:pressed{
    background: rgb(200, 100, 100);
}

QDockWidget::float-button:pressed {
    background: rgb(80, 80, 80);
}
'''

TabStyle = '''
QMainWindow::separator {
    background: rgb(30, 30, 30);
    width: 3px; /* when vertical */
    height: 3px; /* when horizontal */
}
QMainWindow::separator:hover {
    background: rgb(50, 150, 250);
    width: 3px; /* when vertical */
    height: 3px; /* when horizontal */
}
QTabWidget::tab-bar {
alignment:left;
top:0px;
left:0px;
right:0px;
}
QTabBar::tab {
border-color: white;
border-width: 0px;
border-bottom: none;
border-top-left-radius: 0px;
border-top-right-radius: 0px;
min-width:60px;
min-height:20px;
margin 2px 2px 2px 2px;
}
QTabBar::tab:selected{
background: rgb(60, 60, 60);
color: rgb(250, 100, 100);
}
QTabBar::tab:!selected{
background: rgb(40, 40, 40);
color: white;
border-top: 0px solid rgb(40, 40, 40);
}
QTabBar::tab:hover{
background:rgb(80, 80, 80);
}
'''
ScrollBarStyle ='''
QScrollBar:vertical {
     border: 0px solid grey;
     background: #1e1e1e;
     width: 15px;
     margin: 1px 0 1px 0;
 }
 QScrollBar::handle:vertical:hover {
     border: 5px solid #454545;
     background: #454545;
     width: 15px;
     border-radius: 7px;
 }
 QScrollBar::handle:vertical {
     border: 5px solid #353535;
     background: #353535;
     min-height: 20px;
     border-radius: 7px;
 }
 QScrollBar::add-line:vertical {
     border: 0px solid grey;
     background: #1e1e1e;
     height: 2px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }

 QScrollBar::sub-line:vertical {
     border: 0px solid grey;
     background: #1e1e1e;
     height: 2px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }
 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: none;
 }


 QScrollBar:horizontal {
    border: 0px solid grey;
    background: #1e1e1e;
    height: 15px;
    margin: 0px 1px 0px 1px;
}
QScrollBar::handle:horizontal {
    background: #353535;
    min-width: 20px;
    border: 5px solid #353535;
    border-radius: 7px;
}
QScrollBar::handle:horizontal:hover {
    background: #454545;
    border: 5px solid #454545;
    min-width: 20px;
    border-radius: 7px;
}
QScrollBar::add-line:horizontal {
    border: 0px solid grey;
    background: #1e1e1e;
    width: 2px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    border: 0px solid grey;
    background: #1e1e1e;
    width: 2px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
'''
RMenuButtonDarkStyle = '''
QPushButton{
    background-color: transparent;
    color: white;
    font: 18px;
    border-radius: 0px;
    border: 0px solid rgb(40, 40, 40);
}
QPushButton:hover{
    background-color: rgb(50, 90, 150);
}
QPushButton:pressed{
    background-color: rgb(80, 140, 250);
}
'''

RMenuButtonLightStyle = '''
QPushButton{
    background-color: transparent;
    color: black;
    font: 18px;
    border-radius: 0px;
    border: 0px solid rgb(40, 40, 40);
}
QPushButton:hover{
    background-color: rgb(50, 50, 220);
}
QPushButton:pressed{
    background-color: rgb(70, 70, 250);
}
'''

RPushButtonDarkStyle = '''
QPushButton{
    background-color: rgb(40, 40, 40);
    color: white;
    font: 18px;
    border-radius: 20px;
    border: 3px solid rgb(40, 40, 40);
}
QPushButton:hover{
    background-color: rgb(50, 90, 150);
    border: 3px solid rgb(50, 90, 150);
}
QPushButton:pressed{
    background-color: rgb(80, 140, 250);
    border: 3px solid rgb(80, 140, 250);
}
'''

RPushButtonLightStyle = '''
QPushButton{
    background-color: rgb(80, 120, 255);
    color: black;
    font: 18px;
    border-radius: 20px;
    border: 3px solid rgb(80, 120, 255);
}
QPushButton:hover{
    background-color: rgb(50, 50, 220);
    border: 3px solid rgb(50, 50, 220);
}
QPushButton:pressed{
    background-color: rgb(70, 70, 250);
    border: 3px solid rgb(70, 70, 250);
}
'''
