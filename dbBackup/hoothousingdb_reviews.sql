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
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `text` text,
  `manager_rating` int(45) NOT NULL,
  `property_rating` int(45) NOT NULL,
  `recommended` tinyint(1) NOT NULL,
  `property_id` int(11) NOT NULL,
  `user_href` varchar(100) NOT NULL,
  `rent_share` int(11) NOT NULL,
  `create_dtm` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,'this place sucks','lmdsflgkjdsflkgjsdflkgjdlgjdfslkgjdlkgjdlkdfj',1,0,1,1,'ljpjpokpokpok@wasdd.com',234,'2015-04-02 05:11:06'),(2,'Hello','Hello',10,2,1,1,'Hello user',500,'2015-04-02 05:17:18'),(3,'Hello','Hello',10,2,1,1,'Hello user',500,'2015-04-02 05:17:53'),(4,'nice','its nice',1,3,1,1,'lknl',234,'2015-04-02 18:36:16'),(5,'asfs','sdzf',21,36,1,2,'esfd',15,'2015-04-02 21:13:15'),(6,'asfs','sdzf',21,36,1,2,'esfd',15,'2015-04-02 21:19:41'),(7,'dq','SDFGD',41,100,1,1,'SDF',14,'2015-04-02 21:28:10');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-04  1:02:38
