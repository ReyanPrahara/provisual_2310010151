import mysql.connector


class Crud:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbvisual3_2310010151"
        )

    # =====================================================
    # CRUD KEBUN
    # =====================================================
    def simpanKebun(self, nama, divisi, luas):
        cur = self.koneksi.cursor()
        sql = """
            INSERT INTO kebun (nama_kebun, divisi, luas_lahan_ha)
            VALUES (%s, %s, %s)
        """
        cur.execute(sql, (nama, divisi, luas))
        self.koneksi.commit()
        cur.close()

    def dataKebun(self):
        cur = self.koneksi.cursor(dictionary=True)
        cur.execute("SELECT * FROM kebun ORDER BY id_kebun ASC")
        data = cur.fetchall()
        cur.close()
        return data

    def ubahKebun(self, id_kebun, nama, divisi, luas):
        cur = self.koneksi.cursor()
        sql = """
            UPDATE kebun SET
                nama_kebun=%s,
                divisi=%s,
                luas_lahan_ha=%s
            WHERE id_kebun=%s
        """
        cur.execute(sql, (nama, divisi, luas, id_kebun))
        self.koneksi.commit()
        cur.close()

    def hapusKebun(self, id_kebun):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM kebun WHERE id_kebun=%s", (id_kebun,))
        self.koneksi.commit()
        cur.close()

    # =====================================================
    # CRUD TENAGA KERJA
    # =====================================================
    def simpanTenagaKerja(self, nama, umur, pendidikan, lama, id_kebun):
        cur = self.koneksi.cursor()
        sql = """
            INSERT INTO tenaga_kerja
            (nama, umur, pendidikan, lama_bekerja_tahun, id_kebun)
            VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(sql, (nama, umur, pendidikan, lama, id_kebun))
        self.koneksi.commit()
        cur.close()

    def dataTenagaKerja(self):
        cur = self.koneksi.cursor(dictionary=True)
        cur.execute("SELECT * FROM tenaga_kerja ORDER BY id_tenaga ASC")
        data = cur.fetchall()
        cur.close()
        return data

    def ubahTenagaKerja(self, id_tenaga, nama, umur, pendidikan, lama, id_kebun):
        cur = self.koneksi.cursor()
        sql = """
            UPDATE tenaga_kerja SET
                nama=%s,
                umur=%s,
                pendidikan=%s,
                lama_bekerja_tahun=%s,
                id_kebun=%s
            WHERE id_tenaga=%s
        """
        cur.execute(sql, (nama, umur, pendidikan, lama, id_kebun, id_tenaga))
        self.koneksi.commit()
        cur.close()

    def hapusTenagaKerja(self, id_tenaga):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM tenaga_kerja WHERE id_tenaga=%s", (id_tenaga,))
        self.koneksi.commit()
        cur.close()

    # =====================================================
    # CRUD PRODUKTIVITAS
    # =====================================================
    def simpanProduktivitas(self, tahun, produktivitas, id_kebun):
        cur = self.koneksi.cursor()
        sql = """
            INSERT INTO produktivitas
            (tahun, produktivitas_ton_ha, id_kebun)
            VALUES (%s, %s, %s)
        """
        cur.execute(sql, (tahun, produktivitas, id_kebun))
        self.koneksi.commit()
        cur.close()

    def dataProduktivitas(self):
        cur = self.koneksi.cursor(dictionary=True)
        cur.execute("SELECT * FROM produktivitas ORDER BY id_produktivitas ASC")
        data = cur.fetchall()
        cur.close()
        return data

    def ubahProduktivitas(self, id_prod, tahun, produktivitas, id_kebun):
        cur = self.koneksi.cursor()
        sql = """
            UPDATE produktivitas SET
                tahun=%s,
                produktivitas_ton_ha=%s,
                id_kebun=%s
            WHERE id_produktivitas=%s
        """
        cur.execute(sql, (tahun, produktivitas, id_kebun, id_prod))
        self.koneksi.commit()
        cur.close()

    def hapusProduktivitas(self, id_prod):
        cur = self.koneksi.cursor()
        cur.execute(
            "DELETE FROM produktivitas WHERE id_produktivitas=%s",
            (id_prod,)
        )
        self.koneksi.commit()
        cur.close()

    # =====================================================
    # CRUD PREMI (FINAL SESUAI DATABASE)
    # =====================================================
    def simpanPremi(self, id_tenaga, id_produktivitas, premi_bulanan):
        cur = self.koneksi.cursor()
        sql = """
            INSERT INTO premi
            (id_tenaga, id_produktivitas, premi_bulanan)
            VALUES (%s, %s, %s)
        """
        cur.execute(sql, (id_tenaga, id_produktivitas, premi_bulanan))
        self.koneksi.commit()
        cur.close()

    def dataPremi(self):
        cur = self.koneksi.cursor(dictionary=True)
        cur.execute("SELECT * FROM premi ORDER BY id_premi ASC")
        data = cur.fetchall()
        cur.close()
        return data

    def ubahPremi(self, id_premi, id_tenaga, id_produktivitas, premi_bulanan):
        cur = self.koneksi.cursor()
        sql = """
            UPDATE premi SET
                id_tenaga=%s,
                id_produktivitas=%s,
                premi_bulanan=%s
            WHERE id_premi=%s
        """
        cur.execute(
            sql,
            (id_tenaga, id_produktivitas, premi_bulanan, id_premi)
        )
        self.koneksi.commit()
        cur.close()

    def hapusPremi(self, id_premi):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM premi WHERE id_premi=%s", (id_premi,))
        self.koneksi.commit()
        cur.close()
