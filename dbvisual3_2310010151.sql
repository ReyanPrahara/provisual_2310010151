-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 30, 2025 at 01:44 PM
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

-- --------------------------------------------------------

--
-- Table structure for table `kebun`
--

CREATE TABLE `kebun` (
  `id_kebun` int NOT NULL,
  `nama_kebun` varchar(100) DEFAULT NULL,
  `divisi` varchar(50) DEFAULT NULL,
  `luas_lahan_ha` decimal(6,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `kebun`
--

INSERT INTO `kebun` (`id_kebun`, `nama_kebun`, `divisi`, `luas_lahan_ha`) VALUES
(1, 'KEBUN SAWIT', 'SAWIT', '5.00'),
(2, 'KEBUN KELAPA', 'KELAPA', '10.00');

-- --------------------------------------------------------

--
-- Table structure for table `premi`
--

CREATE TABLE `premi` (
  `id_premi` int NOT NULL,
  `id_tenaga` int DEFAULT NULL,
  `id_produktivitas` int DEFAULT NULL,
  `premi_bulanan` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `premi`
--

INSERT INTO `premi` (`id_premi`, `id_tenaga`, `id_produktivitas`, `premi_bulanan`) VALUES
(1, 1, 1, '1375000.00'),
(2, 2, 2, '1834000.00');

-- --------------------------------------------------------

--
-- Table structure for table `produktivitas`
--

CREATE TABLE `produktivitas` (
  `id_produktivitas` int NOT NULL,
  `tahun` year DEFAULT NULL,
  `produktivitas_ton_ha` decimal(6,2) DEFAULT NULL,
  `id_kebun` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `produktivitas`
--

INSERT INTO `produktivitas` (`id_produktivitas`, `tahun`, `produktivitas_ton_ha`, `id_kebun`) VALUES
(1, 2025, '110.00', 1),
(2, 2025, '200.00', 2);

-- --------------------------------------------------------

--
-- Table structure for table `tenaga_kerja`
--

CREATE TABLE `tenaga_kerja` (
  `id_tenaga` int NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `umur` int DEFAULT NULL,
  `pendidikan` enum('SMP','SMA') DEFAULT NULL,
  `lama_bekerja_tahun` int DEFAULT NULL,
  `id_kebun` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tenaga_kerja`
--

INSERT INTO `tenaga_kerja` (`id_tenaga`, `nama`, `umur`, `pendidikan`, `lama_bekerja_tahun`, `id_kebun`) VALUES
(1, 'REYAN PRAHARA', 21, 'SMA', 1, 1),
(2, 'PURNIAWAN', 26, 'SMA', 4, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kebun`
--
ALTER TABLE `kebun`
  ADD PRIMARY KEY (`id_kebun`);

--
-- Indexes for table `premi`
--
ALTER TABLE `premi`
  ADD PRIMARY KEY (`id_premi`),
  ADD KEY `fk_premi_tenaga` (`id_tenaga`),
  ADD KEY `fk_premi_produk` (`id_produktivitas`);

--
-- Indexes for table `produktivitas`
--
ALTER TABLE `produktivitas`
  ADD PRIMARY KEY (`id_produktivitas`),
  ADD KEY `fk_produk_kebun` (`id_kebun`);

--
-- Indexes for table `tenaga_kerja`
--
ALTER TABLE `tenaga_kerja`
  ADD PRIMARY KEY (`id_tenaga`),
  ADD KEY `fk_tenaga_kebun` (`id_kebun`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kebun`
--
ALTER TABLE `kebun`
  MODIFY `id_kebun` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `premi`
--
ALTER TABLE `premi`
  MODIFY `id_premi` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `produktivitas`
--
ALTER TABLE `produktivitas`
  MODIFY `id_produktivitas` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tenaga_kerja`
--
ALTER TABLE `tenaga_kerja`
  MODIFY `id_tenaga` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `premi`
--
ALTER TABLE `premi`
  ADD CONSTRAINT `fk_premi_produk` FOREIGN KEY (`id_produktivitas`) REFERENCES `produktivitas` (`id_produktivitas`),
  ADD CONSTRAINT `fk_premi_tenaga` FOREIGN KEY (`id_tenaga`) REFERENCES `tenaga_kerja` (`id_tenaga`);

--
-- Constraints for table `produktivitas`
--
ALTER TABLE `produktivitas`
  ADD CONSTRAINT `fk_produk_kebun` FOREIGN KEY (`id_kebun`) REFERENCES `kebun` (`id_kebun`);

--
-- Constraints for table `tenaga_kerja`
--
ALTER TABLE `tenaga_kerja`
  ADD CONSTRAINT `fk_tenaga_kebun` FOREIGN KEY (`id_kebun`) REFERENCES `kebun` (`id_kebun`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
