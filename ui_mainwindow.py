# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(294, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(999999999)

        self.gridLayout.addWidget(self.spinBox_8, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_3, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_4, 4, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(999999999)

        self.gridLayout.addWidget(self.spinBox_9, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_5, 6, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_6, 7, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_7, 8, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 294, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen (x):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen (y):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino (x):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino (y):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color (Red):", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Color (Green):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Color (Blue):", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar part\u00edcula", None))
    # retranslateUi

