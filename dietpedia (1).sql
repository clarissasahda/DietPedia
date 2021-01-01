-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 01 Jan 2021 pada 09.54
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dietpedia`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `daftar`
--

CREATE TABLE `daftar` (
  `idPengguna` int(2) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Usia` int(2) NOT NULL,
  `JenisKelamin` varchar(10) NOT NULL,
  `TinggiBadan` int(3) NOT NULL,
  `BeratBadanAwal` int(3) NOT NULL,
  `BeratBadanImpian` int(3) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `ListMakanan` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `daftar`
--

INSERT INTO `daftar` (`idPengguna`, `Nama`, `Usia`, `JenisKelamin`, `TinggiBadan`, `BeratBadanAwal`, `BeratBadanImpian`, `Email`, `Password`, `ListMakanan`) VALUES
(4, 'dinda', 19, 'perempuan', 150, 47, 44, 'dindahahahihi@gmail.com', 'dindaunchh', '\n100 gr Tempe Goreng\nTelur Goreng\n100 gr Ayam Geprek\nTotal Kalori = 527');

-- --------------------------------------------------------

--
-- Struktur dari tabel `daftaradmin`
--

CREATE TABLE `daftaradmin` (
  `idAdmin` int(2) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `makanan`
--

CREATE TABLE `makanan` (
  `IdMakan` int(3) NOT NULL,
  `namaMakanan` varchar(200) NOT NULL,
  `jumlahKalori` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `makanan`
--

INSERT INTO `makanan` (`IdMakan`, `namaMakanan`, `jumlahKalori`) VALUES
(1, '1 mangkok Nasi Putih', 204),
(2, '1 Mangkok Nasi Merah', 110),
(3, '100 gr Tempe Goreng', 175),
(4, 'Telur Goreng', 89),
(5, '100 gr Ayam Goreng', 260),
(6, '100 g Sayur Taoge', 114),
(7, '1 Mangkok Sayur Lodeh', 162),
(8, '100 gr Ayam Geprek', 263),
(9, '1 Mangkok Salad Buah', 221),
(10, '1 Buah Sosis Ayam', 49),
(11, '100 gr Sayur Bening Bayam', 36);

-- --------------------------------------------------------

--
-- Struktur dari tabel `olahraga`
--

CREATE TABLE `olahraga` (
  `IdOlahraga` int(3) NOT NULL,
  `namaOlahraga` varchar(200) NOT NULL,
  `kaloriTerbakar` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `olahraga`
--

INSERT INTO `olahraga` (`IdOlahraga`, `namaOlahraga`, `kaloriTerbakar`) VALUES
(1, 'Jogging 30menit', 206),
(2, 'Bersepeda 1 Jam', 206),
(3, 'Push Up 30 menit', 206),
(4, 'Lompat Tali 1 Jam', 515),
(5, 'Senam 30 menit', 90);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `daftar`
--
ALTER TABLE `daftar`
  ADD PRIMARY KEY (`idPengguna`);

--
-- Indeks untuk tabel `daftaradmin`
--
ALTER TABLE `daftaradmin`
  ADD PRIMARY KEY (`idAdmin`);

--
-- Indeks untuk tabel `makanan`
--
ALTER TABLE `makanan`
  ADD PRIMARY KEY (`IdMakan`);

--
-- Indeks untuk tabel `olahraga`
--
ALTER TABLE `olahraga`
  ADD PRIMARY KEY (`IdOlahraga`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `daftar`
--
ALTER TABLE `daftar`
  MODIFY `idPengguna` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `daftaradmin`
--
ALTER TABLE `daftaradmin`
  MODIFY `idAdmin` int(2) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `makanan`
--
ALTER TABLE `makanan`
  MODIFY `IdMakan` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT untuk tabel `olahraga`
--
ALTER TABLE `olahraga`
  MODIFY `IdOlahraga` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
