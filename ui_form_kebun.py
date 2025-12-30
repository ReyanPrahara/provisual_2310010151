# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_kebun.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_FormKebun(object):
    def setupUi(self, FormKebun):
        if not FormKebun.objectName():
            FormKebun.setObjectName(u"FormKebun")
        FormKebun.resize(600, 450)
        self.verticalLayout = QVBoxLayout(FormKebun)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelNama = QLabel(FormKebun)
        self.labelNama.setObjectName(u"labelNama")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelNama)

        self.editNamaKebun = QLineEdit(FormKebun)
        self.editNamaKebun.setObjectName(u"editNamaKebun")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editNamaKebun)

        self.labelDivisi = QLabel(FormKebun)
        self.labelDivisi.setObjectName(u"labelDivisi")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelDivisi)

        self.editDivisi = QLineEdit(FormKebun)
        self.editDivisi.setObjectName(u"editDivisi")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editDivisi)

        self.labelLuas = QLabel(FormKebun)
        self.labelLuas.setObjectName(u"labelLuas")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelLuas)

        self.editLuasLahan = QLineEdit(FormKebun)
        self.editLuasLahan.setObjectName(u"editLuasLahan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editLuasLahan)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormKebun)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormKebun)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormKebun)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.tabelKebun = QTableWidget(FormKebun)
        if (self.tabelKebun.columnCount() < 4):
            self.tabelKebun.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelKebun.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelKebun.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelKebun.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelKebun.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelKebun.setObjectName(u"tabelKebun")
        self.tabelKebun.setRowCount(0)
        self.tabelKebun.setColumnCount(4)

        self.verticalLayout.addWidget(self.tabelKebun)


        self.retranslateUi(FormKebun)

        QMetaObject.connectSlotsByName(FormKebun)
    # setupUi

    def retranslateUi(self, FormKebun):
        FormKebun.setWindowTitle(QCoreApplication.translate("FormKebun", u"Form Data Kebun", None))
        self.labelNama.setText(QCoreApplication.translate("FormKebun", u"Nama Kebun", None))
        self.labelDivisi.setText(QCoreApplication.translate("FormKebun", u"Divisi", None))
        self.labelLuas.setText(QCoreApplication.translate("FormKebun", u"Luas Lahan (Ha)", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormKebun", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormKebun", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormKebun", u"Hapus", None))
        ___qtablewidgetitem = self.tabelKebun.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormKebun", u"ID", None));
        ___qtablewidgetitem1 = self.tabelKebun.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormKebun", u"Nama Kebun", None));
        ___qtablewidgetitem2 = self.tabelKebun.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormKebun", u"Divisi", None));
        ___qtablewidgetitem3 = self.tabelKebun.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormKebun", u"Luas Lahan", None));
    # retranslateUi

