-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 07, 2016 at 01:19 PM
-- Server version: 5.7.15-0ubuntu0.16.04.1
-- PHP Version: 7.0.8-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `phpmysimplelogin`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `username` varchar(25) NOT NULL PRIMARY KEY,
  `password` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `security_q_1` varchar(255) NOT NULL,
  `security_a_1` varchar(255) NOT NULL,
  `security_q_2` varchar(255) NOT NULL,
  `security_a_2` varchar(255) NOT NULL,
  `account` varchar(11) NOT NULL,
  `balance` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `Name`, `security_q_1`, `security_a_1`, `security_q_2`, `security_a_2`, `account`, `balance`) VALUES ('admin', MD5('admin'), '', '', '', '', '', '0', 0);

INSERT INTO `user` (`username`, `password`, `Name`, `security_q_1`, `security_a_1`, `security_q_2`, `security_a_2`, `account`, `balance`) VALUES ('alice', MD5('hackmenot'), 'Alice Liddell', 'What comes after drink me?', 'eat me', 'Who gives good advices?', 'caterpillar', '43266780001', 1000000);

INSERT INTO `user` (`username`, `password`, `Name`, `security_q_1`, `security_a_1`, `security_q_2`, `security_a_2`, `account`, `balance`) VALUES ('bob', MD5('rita1966'), 'Bob Marley', 'No woman?', 'no cry', 'Wake up?', 'and live', '43266780002', '1000000');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
