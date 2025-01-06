# Copyright (c) 2025 Rafael Schmetcka <rafael.schmetcka@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images.icons_rc

class Ui_Home(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 230)
        MainWindow.setMinimumSize(QSize(770, 230))
        MainWindow.setMaximumSize(QSize(770, 230))
        icon = QIcon()
        icon.addFile(u"./Icone/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 180))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(350, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_7.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.lineEdit_ip_local = QLineEdit(self.frame_16)
        self.lineEdit_ip_local.setObjectName(u"lineEdit_ip_local")
        self.lineEdit_ip_local.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_ip_local.setFont(font1)
        self.lineEdit_ip_local.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outside;\n"
"border-radius:10px;\n"
"border-width: 2px;\n"
"border: 1px solid black;")

        self.horizontalLayout_9.addWidget(self.lineEdit_ip_local)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.lineEdit_senha_local = QLineEdit(self.frame_15)
        self.lineEdit_senha_local.setObjectName(u"lineEdit_senha_local")
        self.lineEdit_senha_local.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_senha_local.setFont(font1)
        self.lineEdit_senha_local.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outside;\n"
"border-radius:10px;\n"
"border-width: 2px;\n"
"border: 1px solid black;")

        self.horizontalLayout_10.addWidget(self.lineEdit_senha_local)


        self.verticalLayout_6.addWidget(self.frame_15)


        self.horizontalLayout_4.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setSpacing(22)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_copiar = QPushButton(self.frame_14)
        self.btn_copiar.setObjectName(u"btn_copiar")
        self.btn_copiar.setMinimumSize(QSize(100, 0))
        self.btn_copiar.setFont(font1)
        self.btn_copiar.setStyleSheet(u"QPushButton {\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(178, 178, 178, 255));\n"
"\n"
"border-style: outside;\n"
"border-width: 2px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(131, 131, 131);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(60, 60, 60);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_copiar)

        self.btn_salvar = QPushButton(self.frame_14)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setMinimumSize(QSize(40, 0))
        self.btn_salvar.setMaximumSize(QSize(40, 16777215))
        self.btn_salvar.setFont(font1)
        self.btn_salvar.setStyleSheet(u"QPushButton {\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"background-image: url(:/Icone/chack 24.png);\n"
"border-style: outside;\n"
"border-width: 2px;\n"
"border: 1px solid black;\n"
"background-position: center;\n"
" background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(146, 217, 108);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(73, 147, 0);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_salvar)


        self.horizontalLayout_4.addWidget(self.frame_14)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(350, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_ip_destino = QLineEdit(self.frame_11)
        self.lineEdit_ip_destino.setObjectName(u"lineEdit_ip_destino")
        self.lineEdit_ip_destino.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_ip_destino.setFont(font1)
        self.lineEdit_ip_destino.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outside;\n"
"border-radius:10px;\n"
"border-width: 2px;\n"
"border: 1px solid black;")

        self.horizontalLayout_6.addWidget(self.lineEdit_ip_destino)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.lineEdit_senha_destino = QLineEdit(self.frame_12)
        self.lineEdit_senha_destino.setObjectName(u"lineEdit_senha_destino")
        self.lineEdit_senha_destino.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_senha_destino.setFont(font1)
        self.lineEdit_senha_destino.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outside;\n"
"border-radius:10px;\n"
"border-width: 2px;\n"
"border: 1px solid black;")

        self.horizontalLayout_8.addWidget(self.lineEdit_senha_destino)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.horizontalLayout.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_conectar = QPushButton(self.frame_9)
        self.btn_conectar.setObjectName(u"btn_conectar")
        self.btn_conectar.setMinimumSize(QSize(100, 0))
        self.btn_conectar.setFont(font1)
        self.btn_conectar.setStyleSheet(u"QPushButton {\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(117, 255, 115, 248), stop:1 rgba(185, 230, 230, 255));\n"
"border-style: outside;\n"
"border-width: 2px;\n"
"border: 1px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(146, 217, 108);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(73, 147, 0);\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_conectar)


        self.horizontalLayout.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Ajudesktop</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Seu computador \u00e9 acess\u00edvel</p><p align=\"center\">neste endere\u00e7o IP:</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>IP:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SENHA:", None))
        self.btn_copiar.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.btn_salvar.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Digite o endere\u00e7o IP e senha da</p><p align=\"center\">m\u00e1quina que deseja acessar:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>IP:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SENHA:", None))
        self.btn_conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
    # retranslateUi

