# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(321, 380)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 50)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(165, 50))
        self.pushButton_2.setMaximumSize(QSize(250, 0))
        self.pushButton_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">GPT+MIDJOUNEY</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u043e\u043d\u0444\u0438\u0433\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443", None))
    # retranslateUi

