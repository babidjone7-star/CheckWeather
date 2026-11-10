# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WeatherApp.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(308, 282)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 309, 281))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Town = QLineEdit(self.widget)
        self.Town.setObjectName(u"Town")

        self.verticalLayout_3.addWidget(self.Town)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FindWeather = QPushButton(self.widget)
        self.FindWeather.setObjectName(u"FindWeather")
        self.FindWeather.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.FindWeather.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 170, 0);\n"
"font: 14pt \"Terminal\";")

        self.verticalLayout.addWidget(self.FindWeather)

        self.TempLbl = QLabel(self.widget)
        self.TempLbl.setObjectName(u"TempLbl")
        self.TempLbl.setStyleSheet(u"font: 10pt \"Segoe Script\";\n"
"color: rgb(0, 0, 0)")

        self.verticalLayout.addWidget(self.TempLbl)

        self.OpisWeth = QLabel(self.widget)
        self.OpisWeth.setObjectName(u"OpisWeth")
        self.OpisWeth.setStyleSheet(u"color: black;\n"
"font: 9pt \"Segoe Script\";")

        self.verticalLayout.addWidget(self.OpisWeth)

        self.Icn = QLabel(self.widget)
        self.Icn.setObjectName(u"Icn")
        self.Icn.setStyleSheet(u"color: black;\n"
"font: 9pt \"Segoe Print\";")

        self.verticalLayout.addWidget(self.Icn)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.FindWeather.setText(QCoreApplication.translate("Dialog", u"Found weather...", None))
        self.TempLbl.setText(QCoreApplication.translate("Dialog", u" \u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 (C) :", None))
        self.OpisWeth.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0433\u043e\u0434\u044b:", None))
        self.Icn.setText(QCoreApplication.translate("Dialog", u"\u0418\u043a\u043e\u043d\u043a\u0430...", None))
    # retranslateUi

