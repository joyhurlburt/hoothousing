-- MySQL dump 10.13  Distrib 5.6.19, for osx10.7 (i386)
--
-- Host: hoothousing.cvkyicyt5jgc.us-west-2.rds.amazonaws.com    Database: hoothousingdb
-- ------------------------------------------------------
-- Server version	5.6.19-log

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
-- Table structure for table `properties`
--

DROP TABLE IF EXISTS `properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `properties` (
  `property_id` int(11) NOT NULL AUTO_INCREMENT,
  `prop_name` varchar(100) DEFAULT NULL,
  `street_number` varchar(45) NOT NULL,
  `street_name` varchar(45) NOT NULL,
  `unit` varchar(45) DEFAULT NULL,
  `city` varchar(45) NOT NULL,
  `state` varchar(45) NOT NULL,
  `zip` varchar(45) NOT NULL,
  `manager_id` int(11) NOT NULL,
  `prop_img_href` varchar(500) DEFAULT NULL,
  `beds` float NOT NULL DEFAULT '0',
  `baths` float NOT NULL DEFAULT '0',
  `type_id` int(11) NOT NULL DEFAULT '0',
  `distance` float NOT NULL DEFAULT '0',
  `campus_id` int(11) NOT NULL,
  `avg_prop_rating` float NOT NULL DEFAULT '0',
  `review_count` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`property_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `properties`
--

LOCK TABLES `properties` WRITE;
/*!40000 ALTER TABLE `properties` DISABLE KEYS */;
INSERT INTO `properties` VALUES (1,NULL,'1311','E 19th Ave','4','Eugene','OR','97403',6,NULL,2,1,4,0,1,21.4,0),(2,'The Columbia','574','E 12th Ave',NULL,'Eugene','OR','94017',7,NULL,3,2,4,0,1,36,0),(3,NULL,'1463','E 21st Ave',NULL,'Eugene','OR','97403',0,NULL,3,2,1,0,1,0,0),(4,'Broadway Place Apartments','255','West Broadway',NULL,'Eugene','OR','97401',1,NULL,2,1,2,1,1,0,0),(7,'The 1840','1840','Agate','','Eugene','OR','97401',2,'',1,1,2,0.44,1,0,0),(8,'Pairadice','640','E 15th','102','Eugene','OR','97401',2,'',2,2,2,0.65,1,0,0),(9,NULL,'2209','Agate St',NULL,'Eugene','OR','97401',2,'',4,2,1,0.73,1,0,0);
/*!40000 ALTER TABLE `properties` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-04  1:02:40
