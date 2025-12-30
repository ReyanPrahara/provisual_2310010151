# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_tenaga_kerja.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_FormTenagaKerja(object):
    def setupUi(self, FormTenagaKerja):
        if not FormTenagaKerja.objectName():
            FormTenagaKerja.setObjectName(u"FormTenagaKerja")
        FormTenagaKerja.resize(650, 500)
        self.verticalLayout = QVBoxLayout(FormTenagaKerja)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelNama = QLabel(FormTenagaKerja)
        self.labelNama.setObjectName(u"labelNama")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelNama)

        self.editNama = QLineEdit(FormTenagaKerja)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.labelUmur = QLabel(FormTenagaKerja)
        self.labelUmur.setObjectName(u"labelUmur")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelUmur)

        self.editUmur = QLineEdit(FormTenagaKerja)
        self.editUmur.setObjectName(u"editUmur")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editUmur)

        self.labelPendidikan = QLabel(FormTenagaKerja)
        self.labelPendidikan.setObjectName(u"labelPendidikan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelPendidikan)

        self.cmbPendidikan = QComboBox(FormTenagaKerja)
        self.cmbPendidikan.addItem("")
        self.cmbPendidikan.addItem("")
        self.cmbPendidikan.setObjectName(u"cmbPendidikan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbPendidikan)

        self.labelLama = QLabel(FormTenagaKerja)
        self.labelLama.setObjectName(u"labelLama")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.labelLama)

        self.editLamaBekerja = QLineEdit(FormTenagaKerja)
        self.editLamaBekerja.setObjectName(u"editLamaBekerja")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editLamaBekerja)

        self.labelIdKebun = QLabel(FormTenagaKerja)
        self.labelIdKebun.setObjectName(u"labelIdKebun")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.labelIdKebun)

        self.editIdKebun = QLineEdit(FormTenagaKerja)
        self.editIdKebun.setObjectName(u"editIdKebun")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editIdKebun)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormTenagaKerja)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormTenagaKerja)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormTenagaKerja)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.tabelTenagaKerja = QTableWidget(FormTenagaKerja)
        if (self.tabelTenagaKerja.columnCount() < 6):
            self.tabelTenagaKerja.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelTenagaKerja.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelTenagaKerja.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelTenagaKerja.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelTenagaKerja.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelTenagaKerja.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabelTenagaKerja.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabelTenagaKerja.setObjectName(u"tabelTenagaKerja")
        self.tabelTenagaKerja.setColumnCount(6)

        self.verticalLayout.addWidget(self.tabelTenagaKerja)


        self.retranslateUi(FormTenagaKerja)

        QMetaObject.connectSlotsByName(FormTenagaKerja)
    # setupUi

    def retranslateUi(self, FormTenagaKerja):
        FormTenagaKerja.setWindowTitle(QCoreApplication.translate("FormTenagaKerja", u"Form Tenaga Kerja", None))
        self.labelNama.setText(QCoreApplication.translate("FormTenagaKerja", u"Nama", None))
        self.labelUmur.setText(QCoreApplication.translate("FormTenagaKerja", u"Umur", None))
        self.labelPendidikan.setText(QCoreApplication.translate("FormTenagaKerja", u"Pendidikan", None))
        self.cmbPendidikan.setItemText(0, QCoreApplication.translate("FormTenagaKerja", u"SMP", None))
        self.cmbPendidikan.setItemText(1, QCoreApplication.translate("FormTenagaKerja", u"SMA", None))

        self.labelLama.setText(QCoreApplication.translate("FormTenagaKerja", u"Lama Bekerja (Tahun)", None))
        self.labelIdKebun.setText(QCoreApplication.translate("FormTenagaKerja", u"ID Kebun", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormTenagaKerja", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormTenagaKerja", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormTenagaKerja", u"Hapus", None))
        ___qtablewidgetitem = self.tabelTenagaKerja.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormTenagaKerja", u"ID", None));
        ___qtablewidgetitem1 = self.tabelTenagaKerja.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormTenagaKerja", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelTenagaKerja.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormTenagaKerja", u"Umur", None));
        ___qtablewidgetitem3 = self.tabelTenagaKerja.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormTenagaKerja", u"Pendidikan", None));
        ___qtablewidgetitem4 = self.tabelTenagaKerja.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormTenagaKerja", u"Lama Bekerja", None));
        ___qtablewidgetitem5 = self.tabelTenagaKerja.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormTenagaKerja", u"ID Kebun", None));
    # retranslateUi

