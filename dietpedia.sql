-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 28 Des 2020 pada 12.00
-- Versi server: 10.4.14-MariaDB
-- Versi PHP: 7.4.9

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
  `BeratBadanAwal` int(3) NOT NULL,
  `BeratBadanImpian` int(3) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `daftar`
--

INSERT INTO `daftar` (`idPengguna`, `Nama`, `Usia`, `JenisKelamin`, `BeratBadanAwal`, `BeratBadanImpian`, `Email`, `Password`) VALUES
(1, 'Dinda', 19, 'Perempuan', 50, 40, 'clarissasahda@gmail.com', '2510');

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
-- Struktur dari tabel `paketdiet`
--

CREATE TABLE `paketdiet` (
  `idPaket` int(2) NOT NULL,
  `NamaPaket` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `paketdiet`
--

INSERT INTO `paketdiet` (`idPaket`, `NamaPaket`) VALUES
(1, 'Paket Diet Vegetarian'),
(2, 'Paket Diet Paleo'),
(3, 'Paket Diet Mayo'),
(4, 'Paket Diet Vegan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `paketdietmayo`
--

CREATE TABLE `paketdietmayo` (
  `idDM` int(2) NOT NULL,
  `Hari` int(2) NOT NULL,
  `MakanPagi` varchar(100) NOT NULL,
  `MakanSiang` varchar(100) NOT NULL,
  `MakanMalam` varchar(100) NOT NULL,
  `Olahraga` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `paketdietmayo`
--

INSERT INTO `paketdietmayo` (`idDM`, `Hari`, `MakanPagi`, `MakanSiang`, `MakanMalam`, `Olahraga`) VALUES
(1, 1, '2 Buah Pisang ', '1 Mangkuk Salad Sayur dan 100gr Mangga\r\n', '1 Kentang Rebus dan 175 Buah Semangka', 'Jalan Kaki 20 menit\r\n'),
(2, 2, '1 Potong Roti Gandum dan 1 Buah Apel\r\n', '1 Porsi Ayam Bakar dan 100gr Buah Nangka \r\n', '1 Mangkuk Nasi Merah dan 180 Ikan Bakar\r\n', 'Jogging 20 menit\r\n'),
(3, 3, '1 Mangkok Oatmeal dan 1 Buah Pir\r\n', '1 Potong Roti Gandum dan 180gr Buah Melon \r\n', '250gr Dada Ayam Rebus dan Saus Tomat\r\n', 'Jalan Kaki 25 menit'),
(4, 4, '1 Potong Roti Gandum dan 1 Buah Jeruk\r\n', '1 Butir Telur Rebus dan 5 Buah Anggur', '200gr Buah Pepaya dan 1 Gelas Susu Rendah Lemak\r\n', 'Jogging 25 menit\r\n'),
(5, 5, '1 Potong Roti Gandum dan 1 Butir Telur Rebus\r\n', '250gr Dada Ayam Panggang dan Segelas Infuse Water\r\n', 'Semangkok Salad Buah dan 150gr Plain Yoghurt\r\n', 'Lari 20 menit\r\n'),
(6, 6, '1 Buah Pisang dan Secangkir Teh Hijau Tanpa Gula\r\n', '250gr Daging Ikan Dori Panggan\r\n', '1 Buah Ubi Rebus dan 1 Butir Telur Rebus\r\n', 'Lari 25 menit\r\n'),
(7, 7, '1 Lembar Roti Bakar dan Selai Strawberry\r\n', '1 Kentang Rebus dan 200gr Sayur Bayam\r\n', '1 Buah Telur Rebus dan 2 Potong Semangka\r\n', 'Jalan Kaki 20 menit');

-- --------------------------------------------------------

--
-- Struktur dari tabel `paketdietpaleo`
--

CREATE TABLE `paketdietpaleo` (
  `Hari` int(2) NOT NULL,
  `idDP` int(2) NOT NULL,
  `MakanPagi` varchar(100) NOT NULL,
  `MakanSiang` varchar(100) NOT NULL,
  `MakanMalam` varchar(100) NOT NULL,
  `Olahraga` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `paketdietpaleo`
--

INSERT INTO `paketdietpaleo` (`Hari`, `idDP`, `MakanPagi`, `MakanSiang`, `MakanMalam`, `Olahraga`) VALUES
(1, 1, '1 Mangkok Bubur Kacang Hijau dan 1 Buah Salak', '250gr Dada Ayam Rebus dan 100gr Tumis Asparagus\r\n', '1 Buah Mangga\r\n', 'Senam Aerobik 5 menit\r\n'),
(2, 2, '1 Mangkok Salad Sayur dan 1 Kentang Rebus\r\n', '150gr Salmon Panggang dan 1 Buah Jeruk\r\n', '1 Mangkok Oatmeal dan 5 Buah Strawberry\r\n', 'Jogging 30 menit\r\n'),
(3, 3, '1 Mangkok Bubur Ayam\r\n', '1 Buah Jagung Rebus dan 1 Butir Telur Rebus\r\n', '2 Buah Pisang Kukus\r\n', 'Zumba 15 menit\r\n'),
(4, 4, '200gr Tumis Udang dan dan 5 Buah Anggur', '200gr Tumis Jamur Kancing dan 1 Gelas Jus Jambu', '150gr Ubi Panggang dan 150gr Tumis Kangkung\r\n', 'Jogging 25 menit'),
(5, 5, '1 Mangkok Sup Ayam dan 1 Buah Apel\r\n', '1 Kentang Rebus dan 200gr Oseng Jamur Kancing\r\n', '1 Mangkok Sup Tahu\r\n', 'Lari 30 menit\r\n'),
(6, 6, '100gr Kol Rebus dan 1 Butir Telur Rebus\r\n', '1 Butir Telur Orak-Arik dan 1 Buah Labu Siam Rebus\r\n', '200gr Edamame Rebus\r\n', 'Sit-Up 20 kali\r\n'),
(7, 7, '200gr Ikan Sarden dan 1 Gelas Jus Melon\r\n', '150gr Cumi Asam Manis dan 1 Buah Pisang\r\n', '1 Jagung Rebus dan 5 Buah Tomat Cherry\r\n', 'Jalan Cepat 15 menit\r\n');

-- --------------------------------------------------------

--
-- Struktur dari tabel `paketdietvegan`
--

CREATE TABLE `paketdietvegan` (
  `idDV` int(2) NOT NULL,
  `Hari` int(2) NOT NULL,
  `MakanPagi` varchar(100) NOT NULL,
  `MakanSiang` varchar(100) NOT NULL,
  `MakanMalam` varchar(100) NOT NULL,
  `Olahraga` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `paketdietvegan`
--

INSERT INTO `paketdietvegan` (`idDV`, `Hari`, `MakanPagi`, `MakanSiang`, `MakanMalam`, `Olahraga`) VALUES
(1, 1, 'Satu Buah Ubi Jalar Rebus dan 1 Gelas Jus Alpukat', '1 Mangkuk Sup Sayur dan 1 Tahu Goreng', 'Tumis Pokcoy, Kentang, dan Tempe', 'Sit-Up 20 kali'),
(2, 2, '1 Potong Roti Gandum dan 1 Gelas Susu Kedelai', '195gr Nasi Goreng Sayur dan 1 Buah Jeruk', '1 Buah Kentang Rebus dan 1 Gelas Infuse Water', 'Push-up 25 kali'),
(3, 3, '1 Mangkuk Oatmeal dan 150gr Buah Melon', '230gr Tumis Brokoli dan 2 Potong Tempe Goreng', 'Semangkuk Sup Jagung dan 1 Gelas Susu Kedelai', 'Lompat Tali 15 menit'),
(4, 4, '1 Mangkuk Bubur Kacang Hijau dan Secangkir Air Lemon Hangat', '150gr Pepes Tahu dan 2 Potong Semangka', '1 Porsi Steak Tempe dan 1 Gelas Infuse Water', 'Senam Aerobik 10 menit'),
(5, 5, '150gr Nasi Merah dan 100gr Tumis Kangkung', '3 Tusuk Sate Tempe Bakar dan 1 Gelas Susu Almond', '200gr Edamame Rebus ', 'Squat-jump 30 kali'),
(6, 6, 'Roti Gandum Bakar dan 1 Buah Alpukat ', '180gr Tumis Kacang Panjang dan Perkedel Tempe', '150gr Singkong Kukus dan 1 Gelas Jus Strawberry', 'Bersepeda 20 menit'),
(7, 7, '1 Potong Sandwich Sayur dan 1 Gelas Susu Kedelai', '180gr Tumis Wortel dan Babycorn ', '2 Buah Pisang ', 'Jogging 20 menit');

-- --------------------------------------------------------

--
-- Struktur dari tabel `paketdietvegetarian`
--

CREATE TABLE `paketdietvegetarian` (
  `idDVE` int(2) NOT NULL,
  `Hari` int(2) NOT NULL,
  `MakanPagi` varchar(100) NOT NULL,
  `MakanSiang` varchar(100) NOT NULL,
  `MakanMalam` varchar(100) NOT NULL,
  `Olahraga` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `paketdietvegetarian`
--

INSERT INTO `paketdietvegetarian` (`idDVE`, `Hari`, `MakanPagi`, `MakanSiang`, `MakanMalam`, `Olahraga`) VALUES
(1, 1, '1 Butir Telur Rebus dan 1 Buah Kentang Rebus', '180gr Tumis Sawi Putih dan 1 Gelas Jus Mangga', '1 Buah Naga ', 'Lari 30 menit'),
(2, 2, '200gr Sayur Gambas dan 2 Potong Tempe Goreng', 'Semangkuk sayuran kukus dan 1 Butir Telur Rebus', 'Semangkuk Oatmeal dan 1 Gelas Susu Rendah Lemak', 'Zumba 15 menit'),
(3, 3, '1 Buah Pir dan 1 Mangkuk Salad Sayur', '150gr Nasi Merah Goreng dan 1 Buah Apel', '1 Buah Kentang Rebus dan 1 Gelas Infuse Water', 'Jalan kaki 30 menit'),
(4, 4, ' 180gr Orak-orik Buncis dan Telur', '1 Mangkuk Capcay dan 1 Buah Kiwi', '180gr Tumis Taoge dan 1 Gelas Susu Rendah Lemak', 'Lompat Tali 20 menit'),
(5, 5, '1 Mangkuk Sup Tomat Telur', '8 Tusuk Sate Jamur dan 1 Gelas Jus Lemon ', '1 Mangkok Salad Buah ', 'Senam Aerobik 10 menit'),
(6, 6, '1 Pepes Jamur dan 150gr Urap-urap', '1 Mangkuk Bakso Tempe dan 150gr Nanas', '200gr Plecing Kangkung dan 1 Potong Tahu Goreng', 'Sit-Up 30 kali'),
(7, 7, '1 Mangkuk Sup Jamur Kuping', '200gr Tumis Bihun Wortel', '200gr Pepaya ', 'Jogging 25 menit');

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
-- Indeks untuk tabel `paketdiet`
--
ALTER TABLE `paketdiet`
  ADD PRIMARY KEY (`idPaket`);

--
-- Indeks untuk tabel `paketdietmayo`
--
ALTER TABLE `paketdietmayo`
  ADD PRIMARY KEY (`idDM`);

--
-- Indeks untuk tabel `paketdietpaleo`
--
ALTER TABLE `paketdietpaleo`
  ADD PRIMARY KEY (`idDP`);

--
-- Indeks untuk tabel `paketdietvegan`
--
ALTER TABLE `paketdietvegan`
  ADD PRIMARY KEY (`idDV`);

--
-- Indeks untuk tabel `paketdietvegetarian`
--
ALTER TABLE `paketdietvegetarian`
  ADD PRIMARY KEY (`idDVE`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `daftar`
--
ALTER TABLE `daftar`
  MODIFY `idPengguna` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `daftaradmin`
--
ALTER TABLE `daftaradmin`
  MODIFY `idAdmin` int(2) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `paketdiet`
--
ALTER TABLE `paketdiet`
  MODIFY `idPaket` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `paketdietmayo`
--
ALTER TABLE `paketdietmayo`
  MODIFY `idDM` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `paketdietpaleo`
--
ALTER TABLE `paketdietpaleo`
  MODIFY `idDP` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `paketdietvegan`
--
ALTER TABLE `paketdietvegan`
  MODIFY `idDV` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `paketdietvegetarian`
--
ALTER TABLE `paketdietvegetarian`
  MODIFY `idDVE` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
