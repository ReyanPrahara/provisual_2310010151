# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionKebun = QAction(main)
        self.actionKebun.setObjectName(u"actionKebun")
        self.actionTenagaKerja = QAction(main)
        self.actionTenagaKerja.setObjectName(u"actionTenagaKerja")
        self.actionProduktivitas = QAction(main)
        self.actionProduktivitas.setObjectName(u"actionProduktivitas")
        self.actionPremi = QAction(main)
        self.actionPremi.setObjectName(u"actionPremi")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionKebun)
        self.menuMenu.addAction(self.actionTenagaKerja)
        self.menuMenu.addAction(self.actionProduktivitas)
        self.menuMenu.addAction(self.actionPremi)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionKebun.setText(QCoreApplication.translate("main", u"Form Kebun", None))
        self.actionTenagaKerja.setText(QCoreApplication.translate("main", u"Form Tenaga Kerja", None))
        self.actionProduktivitas.setText(QCoreApplication.translate("main", u"Form Produktivitas", None))
        self.actionPremi.setText(QCoreApplication.translate("main", u"Form Premi", None))
        self.menuMenu.setTitle(QCoreApplication.translate("main", u"Menu", None))
    # retranslateUi

