# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_premi.ui'
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

class Ui_FormPremi(object):
    def setupUi(self, FormPremi):
        if not FormPremi.objectName():
            FormPremi.setObjectName(u"FormPremi")
        FormPremi.resize(523, 450)
        self.verticalLayout = QVBoxLayout(FormPremi)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelTenaga = QLabel(FormPremi)
        self.labelTenaga.setObjectName(u"labelTenaga")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelTenaga)

        self.editIdTenaga = QLineEdit(FormPremi)
        self.editIdTenaga.setObjectName(u"editIdTenaga")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editIdTenaga)

        self.labelProduktivitas = QLabel(FormPremi)
        self.labelProduktivitas.setObjectName(u"labelProduktivitas")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelProduktivitas)

        self.editIdProduktivitas = QLineEdit(FormPremi)
        self.editIdProduktivitas.setObjectName(u"editIdProduktivitas")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIdProduktivitas)

        self.labelPremi = QLabel(FormPremi)
        self.labelPremi.setObjectName(u"labelPremi")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelPremi)

        self.editPremiBulanan = QLineEdit(FormPremi)
        self.editPremiBulanan.setObjectName(u"editPremiBulanan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editPremiBulanan)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnSimpan = QPushButton(FormPremi)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.buttonLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(FormPremi)
        self.btnUbah.setObjectName(u"btnUbah")

        self.buttonLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(FormPremi)
        self.btnHapus.setObjectName(u"btnHapus")

        self.buttonLayout.addWidget(self.btnHapus)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.tabelPremi = QTableWidget(FormPremi)
        if (self.tabelPremi.columnCount() < 4):
            self.tabelPremi.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPremi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPremi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPremi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPremi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelPremi.setObjectName(u"tabelPremi")
        self.tabelPremi.setColumnCount(4)

        self.verticalLayout.addWidget(self.tabelPremi)


        self.retranslateUi(FormPremi)

        QMetaObject.connectSlotsByName(FormPremi)
    # setupUi

    def retranslateUi(self, FormPremi):
        FormPremi.setWindowTitle(QCoreApplication.translate("FormPremi", u"Form Data Premi", None))
        self.labelTenaga.setText(QCoreApplication.translate("FormPremi", u"ID Tenaga Kerja", None))
        self.labelProduktivitas.setText(QCoreApplication.translate("FormPremi", u"ID Produktivitas", None))
        self.labelPremi.setText(QCoreApplication.translate("FormPremi", u"Premi Bulanan", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormPremi", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormPremi", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormPremi", u"Hapus", None))
        ___qtablewidgetitem = self.tabelPremi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormPremi", u"ID", None));
        ___qtablewidgetitem1 = self.tabelPremi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormPremi", u"ID Tenaga", None));
        ___qtablewidgetitem2 = self.tabelPremi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormPremi", u"ID Produktivitas", None));
        ___qtablewidgetitem3 = self.tabelPremi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormPremi", u"Premi Bulanan", None));
    # retranslateUi

