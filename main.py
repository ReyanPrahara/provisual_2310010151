import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# Import Form
from kebun import Kebun
from tenaga_kerja import TenagaKerja
from produktivitas import Produktivitas
from premi import Premi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.connect_menu()

    def load_ui(self):
        file = QFile("form.ui")
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(file)
        file.close()

        self.setMenuBar(self.ui.menuBar())
        self.setStatusBar(self.ui.statusBar())
        self.setCentralWidget(self.ui.centralWidget())
        self.setWindowTitle("Aplikasi Perkebunan")

    def connect_menu(self):
        self.ui.actionKebun.triggered.connect(self.buka_kebun)
        self.ui.actionTenagaKerja.triggered.connect(self.buka_tenaga_kerja)
        self.ui.actionProduktivitas.triggered.connect(self.buka_produktivitas)
        self.ui.actionPremi.triggered.connect(self.buka_premi)

    def buka_kebun(self):
        self.form_kebun = Kebun()
        self.form_kebun.show()

    def buka_tenaga_kerja(self):
        self.form_tenaga = TenagaKerja()
        self.form_tenaga.show()

    def buka_produktivitas(self):
        self.form_produktivitas = Produktivitas()
        self.form_produktivitas.show()

    def buka_premi(self):
        self.form_premi = Premi()
        self.form_premi.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
