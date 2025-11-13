import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox,
    QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QInputDialog, QLabel
)
import mysql.connector
from mysql.connector import Error

from ui_form import Ui_main   # pastikan nama kelas di ui_form.py = Ui_main


# ========================
# FUNGSI KONEKSI DATABASE
# ========================
def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",                 # sesuaikan kalau beda
            password="",                 # sesuaikan kalau pakai password
            database="dbvisual3_2310010151",
        )
        return conn
    except Error as e:
        print("Error saat koneksi:", e)
        return None


# ========================
# WINDOW TEKNOLOGI MITIGASI
# ========================
class TeknologiWindow(QMainWindow):
    def __init__(self, role="admin", parent=None):
        super().__init__(parent)
        self.role = role

        self.setWindowTitle("Data Teknologi Mitigasi Kekeringan Tanaman Teh")
        self.resize(700, 400)

        central = QWidget(self)
        self.setCentralWidget(central)

        vlayout = QVBoxLayout(central)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "ID", "Nama Teknologi", "Kategori", "Deskripsi"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        vlayout.addWidget(self.table)

        hlayout = QHBoxLayout()
        self.btnTambah = QPushButton("Tambah")
        self.btnHapus = QPushButton("Hapus")
        self.btnRefresh = QPushButton("Refresh")
        hlayout.addWidget(self.btnTambah)
        hlayout.addWidget(self.btnHapus)
        hlayout.addWidget(self.btnRefresh)
        hlayout.addStretch()
        vlayout.addLayout(hlayout)

        self.btnTambah.clicked.connect(self.tambah_teknologi)
        self.btnHapus.clicked.connect(self.hapus_teknologi)
        self.btnRefresh.clicked.connect(self.load_data)

        if self.role != "admin":
            self.btnTambah.setEnabled(False)
            self.btnHapus.setEnabled(False)

        self.load_data()

    def load_data(self):
        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_teknologi, nama_teknologi, kategori, deskripsi
                FROM teknologi_mitigasi
                ORDER BY id_teknologi
            """)
            rows = cursor.fetchall()
            self.table.setRowCount(len(rows))
            for r, row in enumerate(rows):
                for c, value in enumerate(row):
                    item = QTableWidgetItem(str(value) if value is not None else "")
                    if c == 0:
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(r, c, item)
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def tambah_teknologi(self):
        nama, ok = QInputDialog.getText(self, "Tambah Teknologi", "Nama Teknologi:")
        if not ok or not nama.strip():
            return

        kategori, ok = QInputDialog.getItem(
            self, "Tambah Teknologi", "Kategori:",
            ["tanaman", "lahan", "air"], 0, False
        )
        if not ok:
            return

        deskripsi, ok = QInputDialog.getText(self, "Tambah Teknologi", "Deskripsi:")
        if not ok:
            deskripsi = ""

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO teknologi_mitigasi (nama_teknologi, kategori, deskripsi)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (nama.strip(), kategori, deskripsi.strip()))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data teknologi berhasil ditambahkan.")
            self.load_data()
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def hapus_teknologi(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Hapus", "Pilih data teknologi yang akan dihapus.")
            return

        id_item = self.table.item(row, 0)
        if id_item is None:
            return

        id_teknologi = id_item.text()
        jawab = QMessageBox.question(
            self, "Konfirmasi Hapus",
            f"Yakin ingin menghapus data dengan ID {id_teknologi}?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if jawab != QMessageBox.Yes:
            return

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM teknologi_mitigasi WHERE id_teknologi = %s", (id_teknologi,))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data teknologi berhasil dihapus.")
            self.load_data()
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()


# ========================
# WINDOW POHON NAUNGAN
# ========================
class PohonNaunganWindow(QMainWindow):
    def __init__(self, role="admin", parent=None):
        super().__init__(parent)
        self.role = role

        self.setWindowTitle("Data Pohon Naungan pada Perkebunan Teh")
        self.resize(750, 400)

        central = QWidget(self)
        self.setCentralWidget(central)

        vlayout = QVBoxLayout(central)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Nama Spesies", "Nama Latin",
            "Fungsi", "Jarak Tanam Awal", "Jarak Tanam Lanjutan"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        vlayout.addWidget(self.table)

        hlayout = QHBoxLayout()
        self.btnTambah = QPushButton("Tambah")
        self.btnHapus = QPushButton("Hapus")
        self.btnRefresh = QPushButton("Refresh")
        hlayout.addWidget(self.btnTambah)
        hlayout.addWidget(self.btnHapus)
        hlayout.addWidget(self.btnRefresh)
        hlayout.addStretch()
        vlayout.addLayout(hlayout)

        self.btnTambah.clicked.connect(self.tambah_naungan)
        self.btnHapus.clicked.connect(self.hapus_naungan)
        self.btnRefresh.clicked.connect(self.load_data)

        if self.role != "admin":
            self.btnTambah.setEnabled(False)
            self.btnHapus.setEnabled(False)

        self.load_data()

    def load_data(self):
        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_naungan, nama_spesies, nama_latin,
                       fungsi, jarak_tanam_awal_m, jarak_tanam_lanjutan_m
                FROM pohon_naungan
                ORDER BY id_naungan
            """)
            rows = cursor.fetchall()
            self.table.setRowCount(len(rows))
            for r, row in enumerate(rows):
                for c, value in enumerate(row):
                    item = QTableWidgetItem(str(value) if value is not None else "")
                    if c == 0:
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(r, c, item)
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def tambah_naungan(self):
        nama_spesies, ok = QInputDialog.getText(self, "Tambah Pohon Naungan", "Nama Spesies:")
        if not ok or not nama_spesies.strip():
            return

        nama_latin, ok = QInputDialog.getText(self, "Tambah Pohon Naungan", "Nama Latin:")
        if not ok:
            nama_latin = ""

        fungsi, ok = QInputDialog.getText(self, "Tambah Pohon Naungan", "Fungsi:")
        if not ok:
            fungsi = ""

        jarak_awal, ok = QInputDialog.getText(self, "Tambah Pohon Naungan", "Jarak Tanam Awal (misal 6 x 6):")
        if not ok:
            jarak_awal = ""

        jarak_lanjut, ok = QInputDialog.getText(self, "Tambah Pohon Naungan", "Jarak Tanam Lanjutan (misal 12 x 6):")
        if not ok:
            jarak_lanjut = ""

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO pohon_naungan
                    (nama_spesies, nama_latin, fungsi, jarak_tanam_awal_m, jarak_tanam_lanjutan_m)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                nama_spesies.strip(),
                nama_latin.strip(),
                fungsi.strip(),
                jarak_awal.strip(),
                jarak_lanjut.strip()
            ))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data pohon naungan berhasil ditambahkan.")
            self.load_data()
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def hapus_naungan(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Hapus", "Pilih data pohon naungan yang akan dihapus.")
            return

        id_item = self.table.item(row, 0)
        if id_item is None:
            return

        id_naungan = id_item.text()
        jawab = QMessageBox.question(
            self, "Konfirmasi Hapus",
            f"Yakin ingin menghapus data dengan ID {id_naungan}?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if jawab != QMessageBox.Yes:
            return

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pohon_naungan WHERE id_naungan = %s", (id_naungan,))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data pohon naungan berhasil dihapus.")
            self.load_data()
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()


# ========================
# WINDOW MULSA
# ========================
class MulsaWindow(QMainWindow):
    def __init__(self, role="admin", parent=None):
        super().__init__(parent)
        self.role = role

        self.setWindowTitle("Data Mulsa untuk Mitigasi Kekeringan")
        self.resize(750, 400)

        central = QWidget(self)
        self.setCentralWidget(central)

        vlayout = QVBoxLayout(central)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Jenis Mulsa", "Bahan",
            "Manfaat", "Efisiensi Air Min (%)", "Efisiensi Air Max (%)"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        vlayout.addWidget(self.table)

        hlayout = QHBoxLayout()
        self.btnTambah = QPushButton("Tambah")
        self.btnHapus = QPushButton("Hapus")
        self.btnRefresh = QPushButton("Refresh")
        hlayout.addWidget(self.btnTambah)
        hlayout.addWidget(self.btnHapus)
        hlayout.addWidget(self.btnRefresh)
        hlayout.addStretch()
        vlayout.addLayout(hlayout)

        self.btnTambah.clicked.connect(self.tambah_mulsa)
        self.btnHapus.clicked.connect(self.hapus_mulsa)
        self.btnRefresh.clicked.connect(self.load_data)

        if self.role != "admin":
            self.btnTambah.setEnabled(False)
            self.btnHapus.setEnabled(False)

        self.load_data()

    def load_data(self):
        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_mulsa, jenis_mulsa, bahan,
                       manfaat, efisiensi_air_min, efisiensi_air_max
                FROM mulsa
                ORDER BY id_mulsa
            """)
            rows = cursor.fetchall()
            self.table.setRowCount(len(rows))
            for r, row in enumerate(rows):
                for c, value in enumerate(row):
                    item = QTableWidgetItem(str(value) if value is not None else "")
                    if c == 0:
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(r, c, item)
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def tambah_mulsa(self):
        jenis, ok = QInputDialog.getText(self, "Tambah Mulsa", "Jenis Mulsa:")
        if not ok or not jenis.strip():
            return

        bahan, ok = QInputDialog.getText(self, "Tambah Mulsa", "Bahan:")
        if not ok:
            bahan = ""

        manfaat, ok = QInputDialog.getText(self, "Tambah Mulsa", "Manfaat:")
        if not ok:
            manfaat = ""

        ef_min_str, ok = QInputDialog.getText(self, "Tambah Mulsa", "Efisiensi Air Min (%):")
        if not ok or not ef_min_str.strip():
            ef_min_str = "0"

        ef_max_str, ok = QInputDialog.getText(self, "Tambah Mulsa", "Efisiensi Air Max (%):")
        if not ok or not ef_max_str.strip():
            ef_max_str = "0"

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO mulsa
                    (jenis_mulsa, bahan, manfaat, efisiensi_air_min, efisiensi_air_max)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                jenis.strip(),
                bahan.strip(),
                manfaat.strip(),
                float(ef_min_str),
                float(ef_max_str),
            ))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data mulsa berhasil ditambahkan.")
            self.load_data()
        except ValueError:
            QMessageBox.warning(self, "Input Salah", "Efisiensi harus berupa angka.")
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def hapus_mulsa(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Hapus", "Pilih data mulsa yang akan dihapus.")
            return

        id_item = self.table.item(row, 0)
        if id_item is None:
            return

        id_mulsa = id_item.text()
        jawab = QMessageBox.question(
            self, "Konfirmasi Hapus",
            f"Yakin ingin menghapus data dengan ID {id_mulsa}?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if jawab != QMessageBox.Yes:
            return

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM mulsa WHERE id_mulsa = %s", (id_mulsa,))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data mulsa berhasil dihapus.")
            self.load_data()
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()


# ========================
# WINDOW KONSERVASI AIR
# ========================
class KonservasiAirWindow(QMainWindow):
    def __init__(self, role="admin", parent=None):
        super().__init__(parent)
        self.role = role

        self.setWindowTitle("Data Teknologi Konservasi Air pada Perkebunan Teh")
        self.resize(850, 400)

        central = QWidget(self)
        self.setCentralWidget(central)

        vlayout = QVBoxLayout(central)

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID", "Jenis Teknologi", "Nama Teknologi",
            "Dimensi", "Δ Kadar Air Min", "Δ Kadar Air Max",
            "Lama Tahan Kering (bln)", "Keterangan"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        vlayout.addWidget(self.table)

        hlayout = QHBoxLayout()
        self.btnTambah = QPushButton("Tambah")
        self.btnHapus = QPushButton("Hapus")
        self.btnRefresh = QPushButton("Refresh")
        hlayout.addWidget(self.btnTambah)
        hlayout.addWidget(self.btnHapus)
        hlayout.addWidget(self.btnRefresh)
        hlayout.addStretch()
        vlayout.addLayout(hlayout)

        self.btnTambah.clicked.connect(self.tambah_konservasi)
        self.btnHapus.clicked.connect(self.hapus_konservasi)
        self.btnRefresh.clicked.connect(self.load_data)

        if self.role != "admin":
            self.btnTambah.setEnabled(False)
            self.btnHapus.setEnabled(False)

        self.load_data()

    def load_data(self):
        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_konservasi, jenis_teknologi, nama_teknologi,
                       dimensi, peningkatan_kadar_air_min, peningkatan_kadar_air_max,
                       lama_tahan_kering_bulan, keterangan
                FROM konservasi_air
                ORDER BY id_konservasi
            """)
            rows = cursor.fetchall()
            self.table.setRowCount(len(rows))
            for r, row in enumerate(rows):
                for c, value in enumerate(row):
                    item = QTableWidgetItem(str(value) if value is not None else "")
                    if c == 0:
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(r, c, item)
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def tambah_konservasi(self):
        jenis, ok = QInputDialog.getItem(
            self, "Tambah Konservasi Air", "Jenis Teknologi:",
            ["silt_pit", "embung", "irigasi_permukaan", "irigasi_tetes", "sprinkler", "lainnya"],
            0, False
        )
        if not ok:
            return

        nama, ok = QInputDialog.getText(self, "Tambah Konservasi Air", "Nama Teknologi:")
        if not ok or not nama.strip():
            return

        dimensi, ok = QInputDialog.getText(self, "Tambah Konservasi Air", "Dimensi:")
        if not ok:
            dimensi = ""

        min_str, ok = QInputDialog.getText(self, "Tambah Konservasi Air", "Δ Kadar Air Min:")
        if not ok or not min_str.strip():
            min_str = "0"

        max_str, ok = QInputDialog.getText(self, "Tambah Konservasi Air", "Δ Kadar Air Max:")
        if not ok or not max_str.strip():
            max_str = "0"

        lama_str, ok = QInputDialog.getText(self, "Tambah Konservasi Air", "Lama Tahan Kering (bulan):")
        if not ok or not lama_str.strip():
            lama_str = "0"

        ket, ok = QInputDialog.getText(self, "Tambah Konservasi Air", "Keterangan:")
        if not ok:
            ket = ""

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO konservasi_air
                    (jenis_teknologi, nama_teknologi, dimensi,
                     peningkatan_kadar_air_min, peningkatan_kadar_air_max,
                     lama_tahan_kering_bulan, keterangan)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                jenis,
                nama.strip(),
                dimensi.strip(),
                float(min_str),
                float(max_str),
                float(lama_str),
                ket.strip()
            ))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data konservasi air berhasil ditambahkan.")
            self.load_data()
        except ValueError:
            QMessageBox.warning(self, "Input Salah", "Nilai numerik harus berupa angka.")
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def hapus_konservasi(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Hapus", "Pilih data konservasi air yang akan dihapus.")
            return

        id_item = self.table.item(row, 0)
        if id_item is None:
            return

        id_konservasi = id_item.text()
        jawab = QMessageBox.question(
            self, "Konfirmasi Hapus",
            f"Yakin ingin menghapus data dengan ID {id_konservasi}?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if jawab != QMessageBox.Yes:
            return

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM konservasi_air WHERE id_konservasi = %s", (id_konservasi,))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data konservasi air berhasil dihapus.")
            self.load_data()
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()


# ========================
# WINDOW PUPUK
# ========================
class PupukWindow(QMainWindow):
    def __init__(self, role="admin", parent=None):
        super().__init__(parent)
        self.role = role

        self.setWindowTitle("Data Pupuk untuk Mitigasi Kekeringan")
        self.resize(800, 400)

        central = QWidget(self)
        self.setCentralWidget(central)

        vlayout = QVBoxLayout(central)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "ID", "Nama Pupuk", "Tipe",
            "Unsur Utama", "Dosis (kg/ha)",
            "Frekuensi/tahun", "Keterangan"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        vlayout.addWidget(self.table)

        hlayout = QHBoxLayout()
        self.btnTambah = QPushButton("Tambah")
        self.btnHapus = QPushButton("Hapus")
        self.btnRefresh = QPushButton("Refresh")
        hlayout.addWidget(self.btnTambah)
        hlayout.addWidget(self.btnHapus)
        hlayout.addWidget(self.btnRefresh)
        hlayout.addStretch()
        vlayout.addLayout(hlayout)

        self.btnTambah.clicked.connect(self.tambah_pupuk)
        self.btnHapus.clicked.connect(self.hapus_pupuk)
        self.btnRefresh.clicked.connect(self.load_data)

        if self.role != "admin":
            self.btnTambah.setEnabled(False)
            self.btnHapus.setEnabled(False)

        self.load_data()

    def load_data(self):
        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_pupuk, nama_pupuk, tipe,
                       unsur_utama, dosis_kg_per_ha,
                       frekuensi_per_tahun, keterangan
                FROM pupuk
                ORDER BY id_pupuk
            """)
            rows = cursor.fetchall()
            self.table.setRowCount(len(rows))
            for r, row in enumerate(rows):
                for c, value in enumerate(row):
                    item = QTableWidgetItem(str(value) if value is not None else "")
                    if c == 0:
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(r, c, item)
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def tambah_pupuk(self):
        nama, ok = QInputDialog.getText(self, "Tambah Pupuk", "Nama Pupuk:")
        if not ok or not nama.strip():
            return

        tipe, ok = QInputDialog.getItem(
            self, "Tambah Pupuk", "Tipe:",
            ["anorganik", "organik", "hayati", "mikro", "lainnya"],
            0, False
        )
        if not ok:
            return

        unsur, ok = QInputDialog.getText(self, "Tambah Pupuk", "Unsur Utama:")
        if not ok:
            unsur = ""

        dosis_str, ok = QInputDialog.getText(self, "Tambah Pupuk", "Dosis (kg/ha):")
        if not ok or not dosis_str.strip():
            dosis_str = "0"

        frek_str, ok = QInputDialog.getText(self, "Tambah Pupuk", "Frekuensi per tahun:")
        if not ok or not frek_str.strip():
            frek_str = "0"

        ket, ok = QInputDialog.getText(self, "Tambah Pupuk", "Keterangan:")
        if not ok:
            ket = ""

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO pupuk
                    (nama_pupuk, tipe, unsur_utama,
                     dosis_kg_per_ha, frekuensi_per_tahun, keterangan)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                nama.strip(),
                tipe,
                unsur.strip(),
                float(dosis_str),
                int(frek_str),
                ket.strip()
            ))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data pupuk berhasil ditambahkan.")
            self.load_data()
        except ValueError:
            QMessageBox.warning(self, "Input Salah", "Dosis dan frekuensi harus berupa angka.")
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def hapus_pupuk(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Hapus", "Pilih data pupuk yang akan dihapus.")
            return

        id_item = self.table.item(row, 0)
        if id_item is None:
            return

        id_pupuk = id_item.text()
        jawab = QMessageBox.question(
            self, "Konfirmasi Hapus",
            f"Yakin ingin menghapus data dengan ID {id_pupuk}?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if jawab != QMessageBox.Yes:
            return

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pupuk WHERE id_pupuk = %s", (id_pupuk,))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data pupuk berhasil dihapus.")
            self.load_data()
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()


# ========================
# WINDOW DATA KLON TEH (MAIN MENU)
# ========================
class MainMenu(QMainWindow):
    def __init__(self, role, nama_lengkap, parent=None):
        super().__init__(parent)
        self.role = role
        self.nama_lengkap = nama_lengkap

        self.setWindowTitle(f"Sistem Informasi Mitigasi Kekeringan Teh - (Login: {nama_lengkap} - {role})")
        self.resize(1100, 520)

        central = QWidget(self)
        self.setCentralWidget(central)

        vlayout = QVBoxLayout(central)

        # ===== Header judul aplikasi =====
        title = QLabel("<h2>Sistem Informasi Mitigasi Kekeringan Tanaman Teh</h2>")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel(
            "Berdasarkan jurnal teknologi mitigasi kekeringan pada tanaman teh<br>"
            "<i>(Rokhmah dkk., 2022)</i>"
        )
        subtitle.setAlignment(Qt.AlignCenter)

        vlayout.addWidget(title)
        vlayout.addWidget(subtitle)

        # ===== Tabel utama klon teh =====
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Kode Klon", "Potensi Hasil (kg/ha/th)",
            "Penurunan Hasil (%)", "Toleransi", "Keterangan"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        vlayout.addWidget(self.table)

        # ===== Baris tombol =====
        hlayout = QHBoxLayout()
        self.btnTambah = QPushButton("Tambah")
        self.btnHapus = QPushButton("Hapus")
        self.btnRefresh = QPushButton("Refresh")
        self.btnTeknologi = QPushButton("Teknologi Mitigasi...")
        self.btnNaungan = QPushButton("Pohon Naungan...")
        self.btnMulsa = QPushButton("Mulsa...")
        self.btnPupuk = QPushButton("Pupuk...")
        self.btnKonservasi = QPushButton("Konservasi Air...")
        self.btnAbout = QPushButton("Tentang Jurnal")
        self.btnLogout = QPushButton("Logout")

        hlayout.addWidget(self.btnTambah)
        hlayout.addWidget(self.btnHapus)
        hlayout.addWidget(self.btnRefresh)
        hlayout.addWidget(self.btnTeknologi)
        hlayout.addWidget(self.btnNaungan)
        hlayout.addWidget(self.btnMulsa)
        hlayout.addWidget(self.btnPupuk)
        hlayout.addWidget(self.btnKonservasi)
        hlayout.addStretch()
        hlayout.addWidget(self.btnAbout)
        hlayout.addWidget(self.btnLogout)
        vlayout.addLayout(hlayout)

        # ===== Koneksi tombol =====
        self.btnTambah.clicked.connect(self.tambah_klon)
        self.btnHapus.clicked.connect(self.hapus_klon)
        self.btnRefresh.clicked.connect(self.load_data)
        self.btnTeknologi.clicked.connect(self.open_teknologi_window)
        self.btnNaungan.clicked.connect(self.open_naungan_window)
        self.btnMulsa.clicked.connect(self.open_mulsa_window)
        self.btnPupuk.clicked.connect(self.open_pupuk_window)
        self.btnKonservasi.clicked.connect(self.open_konservasi_window)
        self.btnAbout.clicked.connect(self.show_about)
        self.btnLogout.clicked.connect(self.logout)

        if self.role != "admin":
            self.btnTambah.setEnabled(False)
            self.btnHapus.setEnabled(False)

        self.load_data()

    def load_data(self):
        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_klon, kode_klon, potensi_hasil_kg_ha_th,
                       penurunan_hasil_persen, toleransi_kekeringan, keterangan
                FROM klon_teh
                ORDER BY id_klon
            """)
            rows = cursor.fetchall()
            self.table.setRowCount(len(rows))
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    item = QTableWidgetItem(str(value) if value is not None else "")
                    if col_idx == 0:
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(row_idx, col_idx, item)
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def tambah_klon(self):
        kode, ok = QInputDialog.getText(self, "Tambah Klon", "Kode Klon:")
        if not ok or not kode.strip():
            return

        potensi_str, ok = QInputDialog.getText(self, "Tambah Klon", "Potensi Hasil (kg/ha/th):")
        if not ok or not potensi_str.strip():
            return

        penurunan_str, ok = QInputDialog.getText(self, "Tambah Klon", "Penurunan Hasil (%):")
        if not ok or not penurunan_str.strip():
            return

        toleransi, ok = QInputDialog.getItem(
            self, "Tambah Klon", "Toleransi Kekeringan:",
            ["tahan", "sedang", "peka"], 0, False
        )
        if not ok:
            return

        ket, ok = QInputDialog.getText(self, "Tambah Klon", "Keterangan (opsional):")
        if not ok:
            ket = ""

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO klon_teh
                    (kode_klon, potensi_hasil_kg_ha_th,
                     penurunan_hasil_persen, toleransi_kekeringan, keterangan)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                kode.strip(),
                float(potensi_str),
                float(penurunan_str),
                toleransi,
                ket.strip()
            ))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data klon berhasil ditambahkan.")
            self.load_data()
        except ValueError:
            QMessageBox.warning(self, "Input Salah", "Potensi dan penurunan harus berupa angka.")
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def hapus_klon(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Hapus", "Pilih data klon yang akan dihapus.")
            return

        id_item = self.table.item(row, 0)
        if id_item is None:
            return

        id_klon = id_item.text()
        jawab = QMessageBox.question(
            self, "Konfirmasi Hapus",
            f"Yakin ingin menghapus data dengan ID {id_klon}?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if jawab != QMessageBox.Yes:
            return

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM klon_teh WHERE id_klon = %s", (id_klon,))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data klon berhasil dihapus.")
            self.load_data()
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def open_teknologi_window(self):
        self.teknologi_window = TeknologiWindow(self.role, self)
        self.teknologi_window.show()

    def open_naungan_window(self):
        self.naungan_window = PohonNaunganWindow(self.role, self)
        self.naungan_window.show()

    def open_mulsa_window(self):
        self.mulsa_window = MulsaWindow(self.role, self)
        self.mulsa_window.show()

    def open_pupuk_window(self):
        self.pupuk_window = PupukWindow(self.role, self)
        self.pupuk_window.show()

    def open_konservasi_window(self):
        self.konservasi_window = KonservasiAirWindow(self.role, self)
        self.konservasi_window.show()

    def show_about(self):
        QMessageBox.information(
            self,
            "Tentang Jurnal",
            (
                "Aplikasi ini dibuat sebagai visualisasi sederhana dari jurnal\n"
                "tentang teknologi mitigasi kekeringan pada tanaman teh.\n\n"
                "Menu yang tersedia menggambarkan beberapa kelompok teknologi:\n"
                "- Klon teh toleran kekeringan\n"
                "- Teknologi pemeliharaan tanaman (pohon naungan, mulsa, pupuk, dll.)\n"
                "- Teknologi konservasi air (silt pit, embung, irigasi, dll.)\n\n"
                "Tujuan aplikasi: membantu memahami dan mengelola data\n"
                "mitigasi kekeringan pada perkebunan teh."
            )
        )

    def logout(self):
        jawab = QMessageBox.question(
            self, "Logout", "Yakin ingin logout?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if jawab != QMessageBox.Yes:
            return
        # kembali ke login
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


# ========================
# WINDOW LOGIN
# ========================
class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)

        self.ui.btnLogin.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.txtUsername.text().strip()
        password = self.ui.txtPassword.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Login", "Username dan password wajib diisi.")
            return

        conn = get_connection()
        if conn is None:
            QMessageBox.critical(self, "Error", "Tidak bisa konek ke database.")
            return

        try:
            cursor = conn.cursor()
            sql = """
                SELECT role, nama_lengkap
                FROM user
                WHERE username = %s AND password = %s AND status = 1
            """
            cursor.execute(sql, (username, password))
            row = cursor.fetchone()

            if row:
                role, nama_lengkap = row
                QMessageBox.information(
                    self,
                    "Login Berhasil",
                    f"Halo {nama_lengkap}!\nRole: {role}"
                )
                self.open_main_menu(role, nama_lengkap)
            else:
                QMessageBox.warning(
                    self,
                    "Login Gagal",
                    "Username atau password salah, atau akun tidak aktif."
                )
        except Error as e:
            QMessageBox.critical(self, "Error DB", str(e))
        finally:
            cursor.close()
            conn.close()

    def open_main_menu(self, role, nama_lengkap):
        self.main_menu = MainMenu(role, nama_lengkap)
        self.main_menu.show()
        self.close()


# ========================
# MAIN APP
# ========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
