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
-- Table structure for table `managers`
--

DROP TABLE IF EXISTS `managers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `managers` (
  `manager_id` int(11) NOT NULL AUTO_INCREMENT,
  `mgmt_name` varchar(100) NOT NULL,
  `mgmt_img_href` varchar(500) DEFAULT NULL,
  `street_number` varchar(45) NOT NULL,
  `street_name` varchar(45) NOT NULL,
  `unit` varchar(45) DEFAULT NULL,
  `city` varchar(45) NOT NULL,
  `state` varchar(45) NOT NULL,
  `zip` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `avg_mgmt_rating` float NOT NULL DEFAULT '0',
  `avg_prop_rating` float NOT NULL DEFAULT '0',
  `avg_recommend` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`manager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `managers`
--

LOCK TABLES `managers` WRITE;
/*!40000 ALTER TABLE `managers` DISABLE KEYS */;
INSERT INTO `managers` VALUES (1,'Greystar',NULL,'1500','SW First Ave','225','Portland','OR','97201','9717035015',0,0,0),(2,'Jennings Group Inc.',NULL,'488','E 11th Ave',NULL,'Eugene','OR','97401','5416835983',0,0,0),(3,'Campus Connection Property Management',NULL,'236','E 13th Ave',NULL,'Eugene','OR','97401','4415561144',0,0,0),(4,'Bell Real Estate',NULL,'630','River Rd',NULL,'Eugene','OR','97404','5416882060',0,0,0),(5,'Von Klein Property Management',NULL,'1301','Ferry St',NULL,'Eugene','OR','97401','5414857776',0,0,0),(6,'Sterling Management Group',NULL,'977','Willagillespie Rd',NULL,'Eugene','OR','97401','5416848141',0,0,0),(7,'Mallard Properties',NULL,'1953','Garden Ave',NULL,'Eugene','OR','97403','5414653825',21,36,0);
/*!40000 ALTER TABLE `managers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-04  1:02:39
