# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(450, 260)
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(self.centralwidget)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitle)

        self.verticalSpacerTop = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerTop)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblUsername = QLabel(self.centralwidget)
        self.lblUsername.setObjectName(u"lblUsername")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblUsername)

        self.txtUsername = QLineEdit(self.centralwidget)
        self.txtUsername.setObjectName(u"txtUsername")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtUsername)

        self.lblPassword = QLabel(self.centralwidget)
        self.lblPassword.setObjectName(u"lblPassword")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPassword)

        self.txtPassword = QLineEdit(self.centralwidget)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtPassword)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacerMid = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerMid)

        self.btnLogin = QPushButton(self.centralwidget)
        self.btnLogin.setObjectName(u"btnLogin")

        self.verticalLayout.addWidget(self.btnLogin)

        self.lblStatus = QLabel(self.centralwidget)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setStyleSheet(u"color: red;")
        self.lblStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblStatus)

        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 25))
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"Login Sistem Mitigasi Kekeringan Teh", None))
        self.lblTitle.setText(QCoreApplication.translate("main", u"<b>Login Pengguna</b>", None))
        self.lblUsername.setText(QCoreApplication.translate("main", u"Username", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("main", u"Masukkan username", None))
        self.lblPassword.setText(QCoreApplication.translate("main", u"Password", None))
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("main", u"Masukkan password", None))
        self.btnLogin.setText(QCoreApplication.translate("main", u"&Login", None))
        self.lblStatus.setText("")
    # retranslateUi

