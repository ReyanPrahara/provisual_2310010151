from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import Crud


class Premi(QWidget):
    def __init__(self):
        super().__init__()
        self.crud = Crud()
        self.id_premi = None

        self.load_ui()
        self.connect_signal()
        self.load_data()

    def load_ui(self):
        file = QFile("form_premi.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file, self)
        file.close()
        self.setWindowTitle("Form Data Premi")

    def connect_signal(self):
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.tabelPremi.cellClicked.connect(self.pilih_data)

    def load_data(self):
        data = self.crud.dataPremi()
        self.ui.tabelPremi.setRowCount(0)

        for row, d in enumerate(data):
            self.ui.tabelPremi.insertRow(row)
            self.ui.tabelPremi.setItem(row, 0, QTableWidgetItem(str(d["id_premi"])))
            self.ui.tabelPremi.setItem(row, 1, QTableWidgetItem(str(d["id_tenaga"])))
            self.ui.tabelPremi.setItem(row, 2, QTableWidgetItem(str(d["id_produktivitas"])))
            self.ui.tabelPremi.setItem(row, 3, QTableWidgetItem(str(d["premi_bulanan"])))

    def simpan(self):
        self.crud.simpanPremi(
            self.ui.editIdTenaga.text(),
            self.ui.editIdProduktivitas.text(),
            self.ui.editPremiBulanan.text()
        )
        QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
        self.load_data()
        self.reset()

    def pilih_data(self, row):
        self.id_premi = self.ui.tabelPremi.item(row, 0).text()
        self.ui.editIdTenaga.setText(self.ui.tabelPremi.item(row, 1).text())
        self.ui.editIdProduktivitas.setText(self.ui.tabelPremi.item(row, 2).text())
        self.ui.editPremiBulanan.setText(self.ui.tabelPremi.item(row, 3).text())

    def ubah(self):
        self.crud.ubahPremi(
            self.id_premi,
            self.ui.editIdTenaga.text(),
            self.ui.editIdProduktivitas.text(),
            self.ui.editPremiBulanan.text()
        )
        QMessageBox.information(self, "Sukses", "Data berhasil diubah")
        self.load_data()
        self.reset()

    def hapus(self):
        self.crud.hapusPremi(self.id_premi)
        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
        self.load_data()
        self.reset()

    def reset(self):
        self.id_premi = None
        self.ui.editIdTenaga.clear()
        self.ui.editIdProduktivitas.clear()
        self.ui.editPremiBulanan.clear()
