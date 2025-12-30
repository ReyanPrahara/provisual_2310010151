from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import Crud


class Kebun(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        file = QFile("form_kebun.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file, self)
        file.close()

        self.setWindowTitle("Form Kebun")

        # CRUD
        self.crud = Crud()

        # Event Button
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)

        # Event Table
        self.ui.tabelKebun.cellClicked.connect(self.pilihData)

        self.id_kebun = None
        self.tampilData()

    # ================= TAMPIL DATA =================

    def tampilData(self):
        self.ui.tabelKebun.setRowCount(0)
        data = self.crud.dataKebun()

        for row_idx, row in enumerate(data):
            self.ui.tabelKebun.insertRow(row_idx)
            self.ui.tabelKebun.setItem(row_idx, 0, QTableWidgetItem(str(row["id_kebun"])))
            self.ui.tabelKebun.setItem(row_idx, 1, QTableWidgetItem(row["nama_kebun"]))
            self.ui.tabelKebun.setItem(row_idx, 2, QTableWidgetItem(row["divisi"]))
            self.ui.tabelKebun.setItem(row_idx, 3, QTableWidgetItem(str(row["luas_lahan_ha"])))

    def bersih(self):
        self.ui.editNamaKebun.clear()
        self.ui.editDivisi.clear()
        self.ui.editLuasLahan.clear()
        self.id_kebun = None

    # ================= CRUD =================

    def simpan(self):
        nama = self.ui.editNamaKebun.text()
        divisi = self.ui.editDivisi.text()
        luas = self.ui.editLuasLahan.text()

        if not nama or not divisi or not luas:
            QMessageBox.warning(self, "Validasi", "Data tidak boleh kosong")
            return

        self.crud.simpanKebun(nama, divisi, luas)
        QMessageBox.information(self, "Sukses", "Data berhasil disimpan")

        self.bersih()
        self.tampilData()

    def pilihData(self, row, column):
        self.id_kebun = self.ui.tabelKebun.item(row, 0).text()
        self.ui.editNamaKebun.setText(self.ui.tabelKebun.item(row, 1).text())
        self.ui.editDivisi.setText(self.ui.tabelKebun.item(row, 2).text())
        self.ui.editLuasLahan.setText(self.ui.tabelKebun.item(row, 3).text())

    def ubah(self):
        if not self.id_kebun:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        nama = self.ui.editNamaKebun.text()
        divisi = self.ui.editDivisi.text()
        luas = self.ui.editLuasLahan.text()

        self.crud.ubahKebun(self.id_kebun, nama, divisi, luas)
        QMessageBox.information(self, "Sukses", "Data berhasil diubah")

        self.bersih()
        self.tampilData()

    def hapus(self):
        if not self.id_kebun:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        self.crud.hapusKebun(self.id_kebun)
        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")

        self.bersih()
        self.tampilData()
