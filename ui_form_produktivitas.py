# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_produktivitas.ui'
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

class Ui_FormProduktivitas(object):
    def setupUi(self, FormProduktivitas):
        if not FormProduktivitas.objectName():
            FormProduktivitas.setObjectName(u"FormProduktivitas")
        FormProduktivitas.resize(593, 450)
        self.verticalLayout = QVBoxLayout(FormProduktivitas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelTahun = QLabel(FormProduktivitas)
        self.labelTahun.setObjectName(u"labelTahun")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelTahun)

        self.editTahun = QLineEdit(FormProduktivitas)
        self.editTahun.setObjectName(u"editTahun")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editTahun)

        self.labelProduktivitas = QLabel(FormProduktivitas)
        self.labelProduktivitas.setObjectName(u"labelProduktivitas")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelProduktivitas)

        self.editProduktivitas = QLineEdit(FormProduktivitas)
        self.editProduktivitas.setObjectName(u"editProduktivitas")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editProduktivitas)

        self.labelIdKebun = QLabel(FormProduktivitas)
        self.labelIdKebun.setObjectName(u"labelIdKebun")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelIdKebun)

        self.editIdKebun = QLineEdit(FormProduktivitas)
        self.editIdKebun.setObjectName(u"editIdKebun")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editIdKebun)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormProduktivitas)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormProduktivitas)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormProduktivitas)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.tabelProduktivitas = QTableWidget(FormProduktivitas)
        if (self.tabelProduktivitas.columnCount() < 4):
            self.tabelProduktivitas.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelProduktivitas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelProduktivitas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelProduktivitas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelProduktivitas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelProduktivitas.setObjectName(u"tabelProduktivitas")
        self.tabelProduktivitas.setColumnCount(4)

        self.verticalLayout.addWidget(self.tabelProduktivitas)


        self.retranslateUi(FormProduktivitas)

        QMetaObject.connectSlotsByName(FormProduktivitas)
    # setupUi

    def retranslateUi(self, FormProduktivitas):
        FormProduktivitas.setWindowTitle(QCoreApplication.translate("FormProduktivitas", u"Form Produktivitas", None))
        self.labelTahun.setText(QCoreApplication.translate("FormProduktivitas", u"Tahun", None))
        self.labelProduktivitas.setText(QCoreApplication.translate("FormProduktivitas", u"Produktivitas (Ton/Ha)", None))
        self.labelIdKebun.setText(QCoreApplication.translate("FormProduktivitas", u"ID Kebun", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormProduktivitas", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormProduktivitas", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormProduktivitas", u"Hapus", None))
        ___qtablewidgetitem = self.tabelProduktivitas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormProduktivitas", u"ID", None));
        ___qtablewidgetitem1 = self.tabelProduktivitas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormProduktivitas", u"Tahun", None));
        ___qtablewidgetitem2 = self.tabelProduktivitas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormProduktivitas", u"Produktivitas", None));
        ___qtablewidgetitem3 = self.tabelProduktivitas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormProduktivitas", u"ID Kebun", None));
    # retranslateUi

