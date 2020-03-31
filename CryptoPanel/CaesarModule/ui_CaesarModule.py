from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_CaesarPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_CaesarPanel, self).__init__()

        # Caesar Encrypt button
        self.CaesarEncryptButton = uni_Widget.ICTFEButton(self)
        self.CaesarEncryptButton.setObjectName('CaesarEncryptButton')
        self.CaesarEncryptButton.setGeometry(QtCore.QRect(580, 20, 120, 45))
        self.CaesarEncryptButton.setText('加密')

        # Caesar Disp edit box and label
        self.CaesarDispTips = uni_Widget.ICTFELabel(self)
        self.CaesarDispTips.setObjectName('CaesarDispTips')
        self.CaesarDispTips.setText('位移:')
        self.CaesarDispTips.setGeometry(QtCore.QRect(50, 20, 60, 45))

        self.CaesarDispBox = uni_Widget.ICTFELineBox(self)
        self.CaesarDispBox.setObjectName('CaesarDispBox')
        self.CaesarDispBox.setGeometry(QtCore.QRect(110, 20, 60, 45))

        # step and limits
        self.CaesarStepTips = uni_Widget.ICTFELabel(self)
        self.CaesarStepTips.setObjectName('CaesarStepTips')
        self.CaesarStepTips.setGeometry(QtCore.QRect(180, 20, 60, 45))
        self.CaesarStepTips.setText('Step:')
        self.CaesarStepBox = uni_Widget.ICTFELineBox(self)
        self.CaesarStepBox.setObjectName('CaesarStepBox')
        self.CaesarStepBox.setGeometry(QtCore.QRect(240, 20, 60, 45))
        self.CaesarLimitTips = uni_Widget.ICTFELabel(self)
        self.CaesarLimitTips.setObjectName('CaesarLimitTips')
        self.CaesarLimitTips.setGeometry(QtCore.QRect(310, 20, 60, 45))
        self.CaesarLimitTips.setText('Lim:')
        self.CaesarLimitBox = uni_Widget.ICTFELineBox(self)
        self.CaesarLimitBox.setObjectName('CaesarLimitBox')
        self.CaesarLimitBox.setGeometry(QtCore.QRect(360, 20, 60, 45))

        # some check boxs
        self.CaesarDigitCheckBox = uni_Widget.ICTFECheckBox(self)
        self.CaesarDigitCheckBox.setObjectName('CaesarDigitCheckBox')
        self.CaesarDigitCheckBox.setGeometry(QtCore.QRect(430, 20, 80, 45))
        self.CaesarDigitCheckBox.setText('数字')
        # Caesar Decrypt button
        self.CaesarDecryptButton = uni_Widget.ICTFEButton(self)
        self.CaesarDecryptButton.setObjectName('CaesarDecryptButton')
        self.CaesarDecryptButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.CaesarDecryptButton.setText('解密')

        self.CaesarTextBox = uni_Widget.ICTFETextBox(self)
        self.CaesarTextBox.setObjectName('CaesarTextBox')
        self.CaesarTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.CaesarTextBox.setPlaceholderText('Caesar Encrypt\n这里写明文')

        self.CaesarCipherBox = uni_Widget.ICTFETextBox(self)
        self.CaesarCipherBox.setObjectName('CaesarCipherBox')
        self.CaesarCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.CaesarCipherBox.setPlaceholderText('Caesar Decrypt\n这里写编码')
        # end Caesar panel