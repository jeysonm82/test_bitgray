-- MySQL dump 10.13  Distrib 5.6.24, for Win32 (x86)
--
-- Host: 127.0.0.1    Database: prueba_pythonDjango
-- ------------------------------------------------------
-- Server version	5.6.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `documento` int(11) DEFAULT NULL,
  `nombres` varchar(80) DEFAULT NULL,
  `detalles` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,123456,'Arturo Lopez',NULL),(2,234567,'Carlos Rodriguez',NULL),(3,345678,'Daniel Acosta',NULL),(4,456789,'Jason Martinez',NULL),(5,567890,'Felipe Salazar',NULL),(6,987654,'Alejandra Rodriguez',NULL),(7,876543,'Daniela Arias',NULL),(8,765432,'Haroll Cuervo',NULL),(9,654321,'Jenny Perez',NULL);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `compras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `id_sede` int(11) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `descripcion` text,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_producto` (`id_producto`),
  KEY `id_sede` (`id_sede`),
  CONSTRAINT `compras_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`),
  CONSTRAINT `compras_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`),
  CONSTRAINT `compras_ibfk_3` FOREIGN KEY (`id_sede`) REFERENCES `sedes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES (19,1,2,1,1000,NULL,'2015-08-01 15:07:30'),(20,2,2,1,NULL,NULL,'2015-08-02 15:07:30'),(21,3,1,1,NULL,NULL,'2015-08-02 15:07:30'),(22,4,4,2,10000,NULL,'2015-08-03 15:07:30'),(23,5,3,2,NULL,NULL,'2015-08-03 15:07:30'),(24,6,5,3,NULL,NULL,'2015-08-03 15:07:30'),(25,7,1,1,NULL,NULL,'2015-08-03 15:07:30'),(26,8,2,1,30000,NULL,'2015-08-03 15:07:30'),(27,9,5,1,NULL,NULL,'2015-08-03 15:07:30'),(28,2,4,2,1000,NULL,'2015-08-03 15:07:30'),(29,2,2,NULL,NULL,'dañado','2015-08-03 15:07:30'),(30,2,1,NULL,NULL,NULL,'2015-08-03 15:07:30'),(31,1,NULL,NULL,NULL,NULL,'2015-08-03 15:07:30'),(32,1,NULL,NULL,NULL,NULL,'2015-08-03 15:07:30'),(33,1,NULL,NULL,NULL,NULL,'2015-08-03 15:07:30'),(34,1,NULL,NULL,NULL,NULL,'2015-08-03 15:07:30'),(35,NULL,3,NULL,9999,NULL,'2015-08-03 15:07:30'),(36,NULL,1,NULL,9999,NULL,'2015-08-03 15:07:30'),(37,NULL,5,NULL,NULL,NULL,'2015-08-03 15:07:30'),(38,3,2,NULL,NULL,NULL,'2015-08-03 15:07:30'),(39,3,NULL,NULL,1000,NULL,'2015-08-03 15:07:30'),(40,4,2,NULL,NULL,NULL,'2015-08-03 15:07:30'),(41,NULL,NULL,NULL,NULL,NULL,'2015-08-03 15:07:30');
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `descripcion` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `producto` varchar(40) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `descripcion` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Producto1',100000,'DProducto1'),(2,'Producto2',32000,'DProducto2'),(3,'Producto3',2000,'DProducto3'),(4,'Producto4',30000,'DProducto4'),(5,'Producto5',140500,'DProducto5');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sedes`
--

DROP TABLE IF EXISTS `sedes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sedes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sede` varchar(40) DEFAULT NULL,
  `direccion` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sedes`
--

LOCK TABLES `sedes` WRITE;
/*!40000 ALTER TABLE `sedes` DISABLE KEYS */;
INSERT INTO `sedes` VALUES (1,'Sur','Cll 1 # 6 23'),(2,'Norte','Cll 100 # 19 31'),(3,'Centro','Cll 12 # 4 2');
/*!40000 ALTER TABLE `sedes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-10 10:37:05
