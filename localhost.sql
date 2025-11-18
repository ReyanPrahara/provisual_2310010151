-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 18, 2025 at 10:54 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbvisual3_2310010151`
--
CREATE DATABASE IF NOT EXISTS `dbvisual3_2310010151` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `dbvisual3_2310010151`;

-- --------------------------------------------------------

--
-- Table structure for table `klon_teh`
--

CREATE TABLE `klon_teh` (
  `id_klon` int NOT NULL,
  `kode_klon` varchar(20) NOT NULL,
  `potensi_hasil_kg_ha_th` decimal(8,2) DEFAULT NULL,
  `penurunan_hasil_persen` decimal(5,2) DEFAULT NULL,
  `toleransi_kekeringan` enum('tahan','sedang','peka') DEFAULT 'tahan',
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `klon_teh`
--

INSERT INTO `klon_teh` (`id_klon`, `kode_klon`, `potensi_hasil_kg_ha_th`, `penurunan_hasil_persen`, `toleransi_kekeringan`, `keterangan`) VALUES
(1, 'PGL 6', '3435.00', '6.95', 'tahan', 'Klon toleran kekeringan'),
(2, 'PGL 10', '3033.00', '7.47', 'tahan', 'Klon toleran kekeringan');

-- --------------------------------------------------------

--
-- Table structure for table `konservasi_air`
--

CREATE TABLE `konservasi_air` (
  `id_konservasi` int NOT NULL,
  `jenis_teknologi` enum('silt_pit','embung','irigasi_permukaan','irigasi_tetes','sprinkler','lainnya') NOT NULL,
  `nama_teknologi` varchar(150) NOT NULL,
  `dimensi` varchar(100) DEFAULT NULL,
  `peningkatan_kadar_air_min` decimal(5,2) DEFAULT NULL,
  `peningkatan_kadar_air_max` decimal(5,2) DEFAULT NULL,
  `lama_tahan_kering_bulan` decimal(4,2) DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `konservasi_air`
--

INSERT INTO `konservasi_air` (`id_konservasi`, `jenis_teknologi`, `nama_teknologi`, `dimensi`, `peningkatan_kadar_air_min`, `peningkatan_kadar_air_max`, `lama_tahan_kering_bulan`, `keterangan`) VALUES
(1, 'silt_pit', 'Silt pit kecil', '100-200 x 30-40 x 30-40 cm', '1.46', '19.22', '3.50', 'Menampung air hujan di sekitar tanaman.'),
(2, 'embung', 'Kolam penampung air (embung)', 'Ukuran bervariasi', '5.00', '25.00', '4.00', 'Menyimpan air untuk irigasi saat kemarau.'),
(3, 'sprinkler', 'Irigasi sprinkler', 'Jarak nozel sesuai jarak tanam', '3.00', '15.00', '2.50', 'Memberi air merata pada kanopi tanaman.');

-- --------------------------------------------------------

--
-- Table structure for table `mulsa`
--

CREATE TABLE `mulsa` (
  `id_mulsa` int NOT NULL,
  `jenis_mulsa` varchar(100) NOT NULL,
  `bahan` varchar(150) DEFAULT NULL,
  `manfaat` text,
  `efisiensi_air_min` decimal(5,2) DEFAULT NULL,
  `efisiensi_air_max` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mulsa`
--

INSERT INTO `mulsa` (`id_mulsa`, `jenis_mulsa`, `bahan`, `manfaat`, `efisiensi_air_min`, `efisiensi_air_max`) VALUES
(1, 'Organik', 'Jerami', 'Menjaga kelembaban tanah dan menekan gulma.', '43.00', '48.00'),
(2, 'Organik', 'Rumput Guatemala', 'Meningkatkan bahan organik dan mengurangi erosi.', '40.00', '45.00'),
(3, 'Plastik', 'Plastik hitam perak', 'Mengurangi evaporasi dan menekan gulma.', '35.00', '40.00');

-- --------------------------------------------------------

--
-- Table structure for table `pemangkasan`
--

CREATE TABLE `pemangkasan` (
  `id_pemangkasan` int NOT NULL,
  `id_teknologi` int NOT NULL,
  `nama_sistem` varchar(100) NOT NULL,
  `tinggi_cm` int DEFAULT NULL,
  `jumlah_cabang_maks` int DEFAULT NULL,
  `waktu_pemangkasan` varchar(100) DEFAULT NULL,
  `manfaat` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pohon_naungan`
--

CREATE TABLE `pohon_naungan` (
  `id_naungan` int NOT NULL,
  `nama_spesies` varchar(100) NOT NULL,
  `nama_latin` varchar(150) DEFAULT NULL,
  `fungsi` text,
  `jarak_tanam_awal_m` varchar(20) DEFAULT NULL,
  `jarak_tanam_lanjutan_m` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pohon_naungan`
--

INSERT INTO `pohon_naungan` (`id_naungan`, `nama_spesies`, `nama_latin`, `fungsi`, `jarak_tanam_awal_m`, `jarak_tanam_lanjutan_m`) VALUES
(1, 'Silver Oak', 'Grevillea robusta', 'Pohon penaung utama, menurunkan suhu dan menahan angin.', '6 x 6', '12 x 6'),
(2, 'Lamtoro', 'Leucaena leucocephala', 'Penaung tambahan, menambah bahan organik.', '6 x 6', '12 x 12');

-- --------------------------------------------------------

--
-- Table structure for table `pupuk`
--

CREATE TABLE `pupuk` (
  `id_pupuk` int NOT NULL,
  `nama_pupuk` varchar(100) NOT NULL,
  `tipe` varchar(50) DEFAULT NULL,
  `unsur_utama` varchar(100) DEFAULT NULL,
  `dosis_kg_per_ha` decimal(8,2) DEFAULT NULL,
  `frekuensi_per_tahun` int DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pupuk`
--

INSERT INTO `pupuk` (`id_pupuk`, `nama_pupuk`, `tipe`, `unsur_utama`, `dosis_kg_per_ha`, `frekuensi_per_tahun`, `keterangan`) VALUES
(1, 'KCl', 'anorganik', 'Kalium (K) tinggi', '150.00', 2, 'Meningkatkan ketahanan tanaman teh terhadap kekeringan.'),
(2, 'NPK 15-15-15', 'anorganik', 'NPK seimbang', '300.00', 3, 'Memperbaiki pertumbuhan vegetatif dan produktivitas.'),
(3, 'Pupuk Organik Padat', 'organik', 'Bahan organik, C-organik', '5000.00', 1, 'Memperbaiki struktur tanah dan kapasitas menahan air.'),
(4, 'Pupuk Hayati (mikroba tanah)', 'hayati', 'Mikroba menguntungkan', '50.00', 2, 'Meningkatkan penyerapan hara dan toleransi stres.');

-- --------------------------------------------------------

--
-- Table structure for table `teknologi_mitigasi`
--

CREATE TABLE `teknologi_mitigasi` (
  `id_teknologi` int NOT NULL,
  `nama_teknologi` varchar(100) NOT NULL,
  `kategori` enum('tanaman','lahan','air') NOT NULL,
  `deskripsi` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `teknologi_mitigasi`
--

INSERT INTO `teknologi_mitigasi` (`id_teknologi`, `nama_teknologi`, `kategori`, `deskripsi`) VALUES
(1, 'Penggunaan klon tahan kekeringan', 'tanaman', 'Pemilihan klon teh toleran kekeringan seperti PGL 6, PGL 10, dll.'),
(2, 'Pemupukan K, Zn, organik & hayati', 'tanaman', 'Pemupukan untuk meningkatkan ketahanan tanaman terhadap stres kekeringan.'),
(3, 'Pohon naungan (shade trees)', 'lahan', 'Penanaman pohon penaung untuk menurunkan suhu dan mengurangi stres air.'),
(4, 'Mulsa organik/plastik', 'lahan', 'Mulsa untuk menjaga kelembaban tanah dan menekan gulma.'),
(5, 'Pruning/pemangkasan', 'tanaman', 'Pengaturan tajuk untuk mengurangi evapotranspirasi dan menstabilkan produksi.'),
(6, 'Panen air hujan & irigasi', 'air', 'Silt pit, embung, dan irigasi untuk menambah ketersediaan air pada musim kering.');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id_user` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nama_lengkap` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `role` enum('admin','user') DEFAULT 'user',
  `status` tinyint(1) DEFAULT '1',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id_user`, `username`, `password`, `nama_lengkap`, `email`, `role`, `status`, `created_at`) VALUES
(1, 'admin', 'admin123', 'Administrator', 'admin@example.com', 'admin', 1, '2025-11-11 22:40:37'),
(4, 'user1', 'user123', 'Pengguna Biasa', 'user1@example.com', 'user', 1, '2025-11-11 23:22:59');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `klon_teh`
--
ALTER TABLE `klon_teh`
  ADD PRIMARY KEY (`id_klon`);

--
-- Indexes for table `konservasi_air`
--
ALTER TABLE `konservasi_air`
  ADD PRIMARY KEY (`id_konservasi`);

--
-- Indexes for table `mulsa`
--
ALTER TABLE `mulsa`
  ADD PRIMARY KEY (`id_mulsa`);

--
-- Indexes for table `pemangkasan`
--
ALTER TABLE `pemangkasan`
  ADD PRIMARY KEY (`id_pemangkasan`),
  ADD KEY `id_teknologi` (`id_teknologi`);

--
-- Indexes for table `pohon_naungan`
--
ALTER TABLE `pohon_naungan`
  ADD PRIMARY KEY (`id_naungan`);

--
-- Indexes for table `pupuk`
--
ALTER TABLE `pupuk`
  ADD PRIMARY KEY (`id_pupuk`);

--
-- Indexes for table `teknologi_mitigasi`
--
ALTER TABLE `teknologi_mitigasi`
  ADD PRIMARY KEY (`id_teknologi`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `klon_teh`
--
ALTER TABLE `klon_teh`
  MODIFY `id_klon` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `konservasi_air`
--
ALTER TABLE `konservasi_air`
  MODIFY `id_konservasi` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `mulsa`
--
ALTER TABLE `mulsa`
  MODIFY `id_mulsa` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `pemangkasan`
--
ALTER TABLE `pemangkasan`
  MODIFY `id_pemangkasan` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pohon_naungan`
--
ALTER TABLE `pohon_naungan`
  MODIFY `id_naungan` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pupuk`
--
ALTER TABLE `pupuk`
  MODIFY `id_pupuk` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `teknologi_mitigasi`
--
ALTER TABLE `teknologi_mitigasi`
  MODIFY `id_teknologi` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pemangkasan`
--
ALTER TABLE `pemangkasan`
  ADD CONSTRAINT `pemangkasan_ibfk_1` FOREIGN KEY (`id_teknologi`) REFERENCES `teknologi_mitigasi` (`id_teknologi`) ON DELETE RESTRICT ON UPDATE CASCADE;
--
-- Database: `db_2310010151`
--
CREATE DATABASE IF NOT EXISTS `db_2310010151` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `db_2310010151`;

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `id_mahasiswa` int NOT NULL,
  `NIM` varchar(10) NOT NULL,
  `nama_mhs` varchar(90) NOT NULL,
  `id_prodi` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`id_mahasiswa`, `NIM`, `nama_mhs`, `id_prodi`) VALUES
(6, '2310010151', 'Reyan Prahara', 2),
(8, '2310010153', 'Muhammad Fiqri', 3),
(9, '2310010152', 'Dimas Prasetyo', 4),
(10, '2310010154', 'Rizal Arif', 5);

-- --------------------------------------------------------

--
-- Table structure for table `prodi`
--

CREATE TABLE `prodi` (
  `id_prodi` int NOT NULL,
  `kode_prodi` varchar(10) NOT NULL,
  `nama_prodi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prodi`
--

INSERT INTO `prodi` (`id_prodi`, `kode_prodi`, `nama_prodi`) VALUES
(1, 'TI', 'Teknik Informatika'),
(2, 'SI', 'Sistem Informasi'),
(3, 'MI', 'Manajemen Informatika'),
(4, 'TK', 'Teknik Komputer'),
(5, 'RPL', 'Rekayasa Perangkat Lunak');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`id_mahasiswa`),
  ADD KEY `fk_prodi` (`id_prodi`);

--
-- Indexes for table `prodi`
--
ALTER TABLE `prodi`
  ADD PRIMARY KEY (`id_prodi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `id_mahasiswa` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `prodi`
--
ALTER TABLE `prodi`
  MODIFY `id_prodi` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD CONSTRAINT `fk_prodi` FOREIGN KEY (`id_prodi`) REFERENCES `prodi` (`id_prodi`) ON DELETE SET NULL ON UPDATE CASCADE;
--
-- Database: `donorku`
--
CREATE DATABASE IF NOT EXISTS `donorku` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `donorku`;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`, `created_at`) VALUES
(1, 'admin', '0192023a7bbd73250516f069df18b500', '2025-11-15 06:53:17');

-- --------------------------------------------------------

--
-- Table structure for table `donasi`
--

CREATE TABLE `donasi` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `amount` int NOT NULL,
  `date` date NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `rating` int NOT NULL,
  `message` text NOT NULL,
  `date` date NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `jadwal`
--

CREATE TABLE `jadwal` (
  `id` int NOT NULL,
  `lokasi_id` int NOT NULL,
  `tanggal` date NOT NULL,
  `waktu` varchar(50) NOT NULL,
  `capacity` int NOT NULL,
  `coordinator` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `jadwal_pendaftar`
--

CREATE TABLE `jadwal_pendaftar` (
  `id` int NOT NULL,
  `jadwal_id` int NOT NULL,
  `user_id` int NOT NULL,
  `tanggal_daftar` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lokasi`
--

CREATE TABLE `lokasi` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` enum('hospital','pmi') NOT NULL,
  `address` text NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `riwayat_donor`
--

CREATE TABLE `riwayat_donor` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `volume` varchar(20) DEFAULT NULL,
  `hemoglobin` varchar(20) DEFAULT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `stok_darah`
--

CREATE TABLE `stok_darah` (
  `id` int NOT NULL,
  `lokasi_id` int NOT NULL,
  `A` int DEFAULT '0',
  `B` int DEFAULT '0',
  `AB` int DEFAULT '0',
  `O` int DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `birth_date` date NOT NULL,
  `blood_type` varchar(5) NOT NULL,
  `rhesus` varchar(3) NOT NULL,
  `address` text,
  `weight` int DEFAULT NULL,
  `blood_pressure` varchar(20) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `donasi`
--
ALTER TABLE `donasi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `jadwal`
--
ALTER TABLE `jadwal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lokasi_id` (`lokasi_id`);

--
-- Indexes for table `jadwal_pendaftar`
--
ALTER TABLE `jadwal_pendaftar`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jadwal_id` (`jadwal_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `lokasi`
--
ALTER TABLE `lokasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `riwayat_donor`
--
ALTER TABLE `riwayat_donor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `stok_darah`
--
ALTER TABLE `stok_darah`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lokasi_id` (`lokasi_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `donasi`
--
ALTER TABLE `donasi`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `jadwal`
--
ALTER TABLE `jadwal`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `jadwal_pendaftar`
--
ALTER TABLE `jadwal_pendaftar`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lokasi`
--
ALTER TABLE `lokasi`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `riwayat_donor`
--
ALTER TABLE `riwayat_donor`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stok_darah`
--
ALTER TABLE `stok_darah`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `donasi`
--
ALTER TABLE `donasi`
  ADD CONSTRAINT `donasi_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `jadwal`
--
ALTER TABLE `jadwal`
  ADD CONSTRAINT `jadwal_ibfk_1` FOREIGN KEY (`lokasi_id`) REFERENCES `lokasi` (`id`);

--
-- Constraints for table `jadwal_pendaftar`
--
ALTER TABLE `jadwal_pendaftar`
  ADD CONSTRAINT `jadwal_pendaftar_ibfk_1` FOREIGN KEY (`jadwal_id`) REFERENCES `jadwal` (`id`),
  ADD CONSTRAINT `jadwal_pendaftar_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `riwayat_donor`
--
ALTER TABLE `riwayat_donor`
  ADD CONSTRAINT `riwayat_donor_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `stok_darah`
--
ALTER TABLE `stok_darah`
  ADD CONSTRAINT `stok_darah_ibfk_1` FOREIGN KEY (`lokasi_id`) REFERENCES `lokasi` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
