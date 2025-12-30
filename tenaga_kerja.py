from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from crud import Crud


class TenagaKerja(QWidget):
    def __init__(self):
        super().__init__()

        # =============================
        # LOAD UI
        # =============================
        file = QFile("form_tenaga_kerja.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file, self)
        file.close()

        self.setWindowTitle("Form Tenaga Kerja")

        # =============================
        # KONEKSI DATABASE
        # =============================
        self.crud = Crud()
        self.id_tenaga = None

        # =============================
        # KONEKSI EVENT
        # =============================
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.tabelTenagaKerja.cellClicked.connect(self.pilihData)

        # tampilkan data awal
        self.tampilData()

    # =============================
    # TAMPIL DATA KE TABEL
    # =============================
    def tampilData(self):
        data = self.crud.dataTenagaKerja()
        self.ui.tabelTenagaKerja.setRowCount(0)

        for row_idx, row in enumerate(data):
            self.ui.tabelTenagaKerja.insertRow(row_idx)
            self.ui.tabelTenagaKerja.setItem(
                row_idx, 0, QTableWidgetItem(str(row["id_tenaga"]))
            )
            self.ui.tabelTenagaKerja.setItem(
                row_idx, 1, QTableWidgetItem(row["nama"])
            )
            self.ui.tabelTenagaKerja.setItem(
                row_idx, 2, QTableWidgetItem(str(row["umur"]))
            )
            self.ui.tabelTenagaKerja.setItem(
                row_idx, 3, QTableWidgetItem(row["pendidikan"])
            )
            self.ui.tabelTenagaKerja.setItem(
                row_idx, 4, QTableWidgetItem(str(row["lama_bekerja_tahun"]))
            )
            self.ui.tabelTenagaKerja.setItem(
                row_idx, 5, QTableWidgetItem(str(row["id_kebun"]))
            )

    # =============================
    # BERSIHKAN FORM
    # =============================
    def bersih(self):
        self.ui.editNama.clear()
        self.ui.editUmur.clear()
        self.ui.cmbPendidikan.setCurrentIndex(0)
        self.ui.editLamaBekerja.clear()
        self.ui.editIdKebun.clear()
        self.id_tenaga = None

    # =============================
    # SIMPAN DATA
    # =============================
    def simpan(self):
        nama = self.ui.editNama.text()
        umur = self.ui.editUmur.text()
        pendidikan = self.ui.cmbPendidikan.currentText()
        lama = self.ui.editLamaBekerja.text()
        id_kebun = self.ui.editIdKebun.text()

        if not nama or not umur or not lama or not id_kebun:
            QMessageBox.warning(self, "Validasi", "Data tidak boleh kosong")
            return

        self.crud.simpanTenagaKerja(
            nama, umur, pendidikan, lama, id_kebun
        )
        QMessageBox.information(self, "Sukses", "Data berhasil disimpan")

        self.bersih()
        self.tampilData()

    # =============================
    # PILIH DATA DARI TABEL
    # =============================
    def pilihData(self, row, column):
        self.id_tenaga = self.ui.tabelTenagaKerja.item(row, 0).text()

        self.ui.editNama.setText(
            self.ui.tabelTenagaKerja.item(row, 1).text()
        )
        self.ui.editUmur.setText(
            self.ui.tabelTenagaKerja.item(row, 2).text()
        )
        self.ui.cmbPendidikan.setCurrentText(
            self.ui.tabelTenagaKerja.item(row, 3).text()
        )
        self.ui.editLamaBekerja.setText(
            self.ui.tabelTenagaKerja.item(row, 4).text()
        )
        self.ui.editIdKebun.setText(
            self.ui.tabelTenagaKerja.item(row, 5).text()
        )

    # =============================
    # UBAH DATA
    # =============================
    def ubah(self):
        if not self.id_tenaga:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        self.crud.ubahTenagaKerja(
            self.id_tenaga,
            self.ui.editNama.text(),
            self.ui.editUmur.text(),
            self.ui.cmbPendidikan.currentText(),
            self.ui.editLamaBekerja.text(),
            self.ui.editIdKebun.text()
        )
        QMessageBox.information(self, "Sukses", "Data berhasil diubah")

        self.bersih()
        self.tampilData()

    # =============================
    # HAPUS DATA
    # =============================
    def hapus(self):
        if not self.id_tenaga:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        self.crud.hapusTenagaKerja(self.id_tenaga)
        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")

        self.bersih()
        self.tampilData()
