from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import Crud


class Produktivitas(QWidget):
    def __init__(self):
        super().__init__()

        ui_file = QFile("form_produktivitas.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setWindowTitle("Form Produktivitas")

        self.db = Crud()
        self.id_prod = None

        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.tabelProduktivitas.cellClicked.connect(self.pilih_data)

        self.tampil_data()

    def tampil_data(self):
        data = self.db.dataProduktivitas()
        self.ui.tabelProduktivitas.setRowCount(0)

        for row, d in enumerate(data):
            self.ui.tabelProduktivitas.insertRow(row)
            self.ui.tabelProduktivitas.setItem(row, 0, QTableWidgetItem(str(d["id_produktivitas"])))
            self.ui.tabelProduktivitas.setItem(row, 1, QTableWidgetItem(str(d["tahun"])))
            self.ui.tabelProduktivitas.setItem(row, 2, QTableWidgetItem(str(d["produktivitas_ton_ha"])))
            self.ui.tabelProduktivitas.setItem(row, 3, QTableWidgetItem(str(d["id_kebun"])))

    def simpan(self):
        self.db.simpanProduktivitas(
            self.ui.editTahun.text(),
            self.ui.editProduktivitas.text(),
            self.ui.editIdKebun.text()
        )
        self.tampil_data()

    def pilih_data(self, row, col):
        self.id_prod = self.ui.tabelProduktivitas.item(row, 0).text()
        self.ui.editTahun.setText(self.ui.tabelProduktivitas.item(row, 1).text())
        self.ui.editProduktivitas.setText(self.ui.tabelProduktivitas.item(row, 2).text())
        self.ui.editIdKebun.setText(self.ui.tabelProduktivitas.item(row, 3).text())

    def ubah(self):
        if not self.id_prod:
            return

        self.db.ubahProduktivitas(
            self.id_prod,
            self.ui.editTahun.text(),
            self.ui.editProduktivitas.text(),
            self.ui.editIdKebun.text()
        )
        self.tampil_data()

    def hapus(self):
        if not self.id_prod:
            return

        self.db.hapusProduktivitas(self.id_prod)
        self.tampil_data()
