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


class Ui_Recebendo_Imagem(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 836)
        icon = QIcon()
        icon.addFile(u"../images/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(180, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.label_endereco_acessado = QLabel(self.frame_6)
        self.label_endereco_acessado.setObjectName(u"label_endereco_acessado")
        self.label_endereco_acessado.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_endereco_acessado)

        self.btn_encerrar = QPushButton(self.frame_6)
        self.btn_encerrar.setObjectName(u"btn_encerrar")
        self.btn_encerrar.setMinimumSize(QSize(0, 20))
        self.btn_encerrar.setMaximumSize(QSize(150, 16777215))
        self.btn_encerrar.setFont(font)
        self.btn_encerrar.setStyleSheet(u"QPushButton {\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.534091, x2:1, y2:0.534091, stop:0 rgba(255, 34, 53, 248), stop:1 rgba(230, 139, 139, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(184, 0, 0);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_encerrar)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(300, 0))
        self.frame_8.setMaximumSize(QSize(300, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_8)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)

        self.horizontalLayout_5.addWidget(self.checkBox)


        self.horizontalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_tela = QLabel(self.frame_10)
        self.label_tela.setObjectName(u"label_tela")
        self.label_tela.setStyleSheet(u"border: 1px solid black;\n"
"border-radius:10px;")

        self.horizontalLayout.addWidget(self.label_tela)

        self.frame_geral_comando = QFrame(self.frame_10)
        self.frame_geral_comando.setObjectName(u"frame_geral_comando")
        self.frame_geral_comando.setMinimumSize(QSize(300, 0))
        self.frame_geral_comando.setMaximumSize(QSize(300, 16777215))
        self.frame_geral_comando.setFrameShape(QFrame.StyledPanel)
        self.frame_geral_comando.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_geral_comando)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_geral_comando)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_geral_comando)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setMaximumSize(QSize(16777215, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_comando = QLineEdit(self.frame_5)
        self.lineEdit_comando.setObjectName(u"lineEdit_comando")
        self.lineEdit_comando.setMinimumSize(QSize(0, 20))
        self.lineEdit_comando.setFont(font)
        self.lineEdit_comando.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.lineEdit_comando)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_geral_comando)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_enviar = QPushButton(self.frame_7)
        self.btn_enviar.setObjectName(u"btn_enviar")
        self.btn_enviar.setMinimumSize(QSize(0, 20))
        self.btn_enviar.setFont(font)
        self.btn_enviar.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btn_enviar)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.textEdit = QTextEdit(self.frame_geral_comando)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"border: 1px solid black;")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.horizontalLayout.addWidget(self.frame_geral_comando)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o do dispositivo acessado:", None))
        self.label_endereco_acessado.setText("")
        self.btn_encerrar.setText(QCoreApplication.translate("MainWindow", u"Encerrar Acesso", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Mostrar Linha de Comandos", None))
        self.label_tela.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Linha de Comando:", None))
        self.btn_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar Comando", None))
    # retranslateUi

