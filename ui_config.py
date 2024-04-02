# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1251, 760)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout.addWidget(self.label_7)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(40)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 40))
        self.lineEdit_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 40))
        self.lineEdit_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 40))
        self.lineEdit_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(Form)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 40))
        self.lineEdit_8.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEdit_8)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.pushButton.setFont(font2)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u043b\u044e\u0447 API (1):", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041a\u043b\u044e\u0447 API (2):", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u043c\u0442:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043f\u044b\u0442\u043e\u043a:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Model:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Temp:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Max_tokens:", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

