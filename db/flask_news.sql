-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: flask_news
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

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
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `types` varchar(10) NOT NULL,
  `img_url` varchar(300) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `view_count` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `is_valid` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (2,'男子长得像\"祁同伟\"挨打 打人者:为何加害检察官','新闻内容','百家','/static/img/news/02.png','zhougy',NULL,'2018-09-29 10:18:46','2018-09-29 10:18:46',1),(3,'导弹来袭怎么办？日本政府呼吁国民躲入地下通道','新闻内容','本地','/static/img/news/03.png','zhougy',NULL,'2018-09-29 10:18:46','2018-09-29 10:18:46',1),(4,'美媒:朝在建能发射3发以上导弹的3000吨级新潜艇','新闻内容','推荐','/static/img/news/04.png','zhougy',NULL,'2018-09-29 10:18:46','2018-09-29 10:18:46',1),(5,'证监会:前发审委员冯小树违法买卖股票被罚4.99亿','新闻内容','百家','/static/img/news/08.png','zhougy',NULL,'2018-09-29 10:18:46','2018-09-29 10:18:46',1),(6,'外交部回应安倍参拜靖国神社:同军国主义划清界限','新闻内容','推荐','/static/img/news/new1.jpg','zhougy',NULL,'2018-09-29 10:18:46','2018-09-29 10:18:46',1),(7,'外交部回应安倍参拜靖国神社:同军国主义划清界限','新闻内容','百家','/static/img/news/new1.jpg','zhougy',NULL,'2018-09-29 10:18:46','2018-09-29 10:18:46',1),(8,'\"萨德\"供地违法？韩民众联名起诉要求撤回供地','新闻内容','百家','/static/img/news/new1.jpg','zhougy',NULL,'2018-09-29 10:18:46','2018-09-29 10:18:46',1),(9,'吴秀波崩塌的何止\"人设\"，还有过亿代言和背后的两家上市公司！','最近，吴秀波大概有点焦头烂额！\r\n“情人”爆料后，人们恍然大悟，原来戏里的吴秀波才是吴秀波，生活中的吴秀波一直在演戏。\r\n大家都说吴秀波“人设崩塌”，其实崩塌的何止“人设”，还有过亿的代言和背后的两家上市公司！\r\n\r\n','推荐','/static/img/news/20180929105153.jpeg',NULL,0,'2018-09-29 10:51:54','2018-09-29 10:51:54',0);
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-14 19:02:51
