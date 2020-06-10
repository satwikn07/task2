-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2020 at 05:23 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cgpa`
--

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE `marks` (
  `regd` varchar(30) NOT NULL,
  `name` varchar(50) NOT NULL,
  `branch` varchar(10) NOT NULL,
  `physics` int(100) NOT NULL,
  `chemistry` int(100) NOT NULL,
  `math` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `marks`
--

INSERT INTO `marks` (`regd`, `name`, `branch`, `physics`, `chemistry`, `math`) VALUES
('1110000001', 'fvedrv', 'CSE', 100, 100, 100),
('1232456789', 'vfdv', 'vfvf', 100, 100, 100),
('1234567890', 'bndsad', 'CSE', 100, 100, 100),
('1272737474', 'css', 'cesdcd', 100, 100, 100),
('1701105180', 'bnd', 'CSE', 0, 0, 0),
('1701106123', 'abhishek', 'CSE', 92, 78, 91),
('1701106125', 'bishwanath', 'CSE', 0, 0, 0),
('211213', 'cece', 'cece', 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `pass`
--

CREATE TABLE `pass` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `year` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pass`
--

INSERT INTO `pass` (`username`, `password`, `email`, `year`) VALUES
('max', '1234', 'fgd25022000@gmail.com', 3),
('max2', '123456', 'fgf25022000@gmail.com', 3),
('max3', '12345', 'fgf25022000@gmail.com', 3),
('max4', '1234574748', 'fgf23@gmail.com', 1),
('max6', '12345465768', 'fgf2@gmail.com', 2),
('max7', '12356676876', 'f@gmail.com', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `marks`
--
ALTER TABLE `marks`
  ADD PRIMARY KEY (`regd`);

--
-- Indexes for table `pass`
--
ALTER TABLE `pass`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
