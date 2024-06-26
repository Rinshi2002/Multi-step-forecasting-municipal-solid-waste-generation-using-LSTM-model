/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.32 : Database - solidwaste
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`solidwaste` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `solidwaste`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add agent',7,'add_agent'),
(26,'Can change agent',7,'change_agent'),
(27,'Can delete agent',7,'delete_agent'),
(28,'Can view agent',7,'view_agent'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add order',9,'add_order'),
(34,'Can change order',9,'change_order'),
(35,'Can delete order',9,'delete_order'),
(36,'Can view order',9,'view_order'),
(37,'Can add product',10,'add_product'),
(38,'Can change product',10,'change_product'),
(39,'Can delete product',10,'delete_product'),
(40,'Can view product',10,'view_product'),
(41,'Can add request',11,'add_request'),
(42,'Can change request',11,'change_request'),
(43,'Can delete request',11,'delete_request'),
(44,'Can view request',11,'view_request'),
(45,'Can add work',12,'add_work'),
(46,'Can change work',12,'change_work'),
(47,'Can delete work',12,'delete_work'),
(48,'Can view work',12,'view_work'),
(49,'Can add user',13,'add_user'),
(50,'Can change user',13,'change_user'),
(51,'Can delete user',13,'delete_user'),
(52,'Can view user',13,'view_user'),
(53,'Can add payment',14,'add_payment'),
(54,'Can change payment',14,'change_payment'),
(55,'Can delete payment',14,'delete_payment'),
(56,'Can view payment',14,'view_payment'),
(57,'Can add orderdetails',15,'add_orderdetails'),
(58,'Can change orderdetails',15,'change_orderdetails'),
(59,'Can delete orderdetails',15,'delete_orderdetails'),
(60,'Can view orderdetails',15,'view_orderdetails'),
(61,'Can add feedback',16,'add_feedback'),
(62,'Can change feedback',16,'change_feedback'),
(63,'Can delete feedback',16,'delete_feedback'),
(64,'Can view feedback',16,'view_feedback'),
(65,'Can add complaint',17,'add_complaint'),
(66,'Can change complaint',17,'change_complaint'),
(67,'Can delete complaint',17,'delete_complaint'),
(68,'Can view complaint',17,'view_complaint'),
(69,'Can add wrequest',18,'add_wrequest'),
(70,'Can change wrequest',18,'change_wrequest'),
(71,'Can delete wrequest',18,'delete_wrequest'),
(72,'Can view wrequest',18,'view_wrequest'),
(73,'Can add viewpickupstatus',19,'add_viewpickupstatus'),
(74,'Can change viewpickupstatus',19,'change_viewpickupstatus'),
(75,'Can delete viewpickupstatus',19,'delete_viewpickupstatus'),
(76,'Can view viewpickupstatus',19,'view_viewpickupstatus'),
(77,'Can add item',20,'add_item'),
(78,'Can change item',20,'change_item'),
(79,'Can delete item',20,'delete_item'),
(80,'Can view item',20,'view_item'),
(81,'Can add picup_ request',11,'add_picup_request'),
(82,'Can change picup_ request',11,'change_picup_request'),
(83,'Can delete picup_ request',11,'delete_picup_request'),
(84,'Can view picup_ request',11,'view_picup_request'),
(85,'Can add work_assign',12,'add_work_assign'),
(86,'Can change work_assign',12,'change_work_assign'),
(87,'Can delete work_assign',12,'delete_work_assign'),
(88,'Can view work_assign',12,'view_work_assign'),
(89,'Can add waste',21,'add_waste'),
(90,'Can change waste',21,'change_waste'),
(91,'Can delete waste',21,'delete_waste'),
(92,'Can view waste',21,'view_waste');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$OtpSccOZW0lLsBxmZCG5bg$kz7YKFxI+Yu6JxRgCO5na0GC95YHVh8bLkZXUH1H9Vg=','2024-04-06 09:31:21.793011',1,'admin','','','admin@gmail.com',1,1,'2024-02-08 04:48:09.237146');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'forecaster','agent'),
(17,'forecaster','complaint'),
(16,'forecaster','feedback'),
(20,'forecaster','item'),
(8,'forecaster','login'),
(9,'forecaster','order'),
(15,'forecaster','orderdetails'),
(14,'forecaster','payment'),
(11,'forecaster','picup_request'),
(10,'forecaster','product'),
(13,'forecaster','user'),
(19,'forecaster','viewpickupstatus'),
(21,'forecaster','waste'),
(12,'forecaster','work_assign'),
(18,'forecaster','wrequest'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-11-23 10:19:45.217398'),
(2,'auth','0001_initial','2023-11-23 10:19:45.523450'),
(3,'admin','0001_initial','2023-11-23 10:19:45.604636'),
(4,'admin','0002_logentry_remove_auto_add','2023-11-23 10:19:45.616549'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-11-23 10:19:45.616549'),
(6,'contenttypes','0002_remove_content_type_name','2023-11-23 10:19:45.662448'),
(7,'auth','0002_alter_permission_name_max_length','2023-11-23 10:19:45.693863'),
(8,'auth','0003_alter_user_email_max_length','2023-11-23 10:19:45.725815'),
(9,'auth','0004_alter_user_username_opts','2023-11-23 10:19:45.725815'),
(10,'auth','0005_alter_user_last_login_null','2023-11-23 10:19:45.760948'),
(11,'auth','0006_require_contenttypes_0002','2023-11-23 10:19:45.760948'),
(12,'auth','0007_alter_validators_add_error_messages','2023-11-23 10:19:45.760948'),
(13,'auth','0008_alter_user_username_max_length','2023-11-23 10:19:45.804868'),
(14,'auth','0009_alter_user_last_name_max_length','2023-11-23 10:19:45.836190'),
(15,'auth','0010_alter_group_name_max_length','2023-11-23 10:19:45.851742'),
(16,'auth','0011_update_proxy_permissions','2023-11-23 10:19:45.851742'),
(17,'auth','0012_alter_user_first_name_max_length','2023-11-23 10:19:45.883456'),
(18,'forecaster','0001_initial','2023-11-23 10:19:46.312748'),
(19,'sessions','0001_initial','2023-11-23 10:19:46.326753'),
(20,'forecaster','0002_wrequest_viewpickupstatus','2023-11-25 09:09:18.813064'),
(21,'forecaster','0003_item','2023-11-25 10:02:12.244123'),
(22,'forecaster','0004_alter_item_product','2023-11-25 10:04:35.550093'),
(23,'forecaster','0005_rename_request_picup_request_rename_work_work_assign_and_more','2023-11-28 07:35:05.540995'),
(24,'forecaster','0006_waste','2023-12-02 05:14:40.170533'),
(25,'forecaster','0007_remove_orderdetails_status','2023-12-14 09:02:22.719787'),
(26,'forecaster','0008_remove_feedback_user','2024-02-08 07:07:57.266872'),
(27,'forecaster','0009_product_description','2024-04-06 08:00:32.717755'),
(28,'forecaster','0010_auto_20240406_1440','2024-04-06 09:10:59.434123');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('8ikzrc2w61pe3gbh0c6jtlh8573mxqfo','.eJxVjDsOwjAQBe_iGllZf9eU9DmDtfZaOIAcKU4qxN1JpBTQzsx7bxFpW2vcelnixOIqQFx-WaL8LO0Q_KB2n2We27pMSR6JPG2X48zldTvbv4NKve5rh37AoSiEkClrH5xHa8EBOk5WKc2Kd6YpFKvRoGYGBG2UMZQIvfh8AaH4Njs:1rsxqZ:KIxv3IFMmQFno11Q88fdaUmG8x1nSOTlIa3wifD7NwI','2024-04-20 04:40:07.495010'),
('ab6gi2tobpgonrebfnzgrjaas3eitvpd','.eJxVjDsOwjAQBe_iGllZf9eU9DmDtfZaOIAcKU4qxN1JpBTQzsx7bxFpW2vcelnixOIqQFx-WaL8LO0Q_KB2n2We27pMSR6JPG2X48zldTvbv4NKve5rh37AoSiEkClrH5xHa8EBOk5WKc2Kd6YpFKvRoGYGBG2UMZQIvfh8AaH4Njs:1rt2OP:ROo1D-rnla5YCkuq6BXIA5PkCBJMWgA58Cgvrgxte5U','2024-04-20 09:31:21.802394'),
('axiz8ceb4ubo5f3js9w28ebxa6yyybhs','.eJyrVkrMTFGyMtJRKoDSRSDaUEcpOT8XyirPj4exipSszHSUckBc01oA_6gQvw:1rDfCu:_nBoK6VsMzrYNQXn7xBPiQUpqkzfXyWuZOuNLlbm5Zs','2023-12-28 06:28:28.311800'),
('r4wfan2dz7687teegnwpkexfe9yd4yfs','.eJxVjjsOwyAQRO9CHSF-G3DK9D4DWmAJTiwsGbuKcvcYyUXSzpt5mjfzuG_F741WPyV2Y5JdfrOA8UW1g_TE-lh4XOq2ToH3Cj9p4-OSaL6f3T9BwVaONTlrUGcHOkRHqGGATANIfTU5RZtRGE0qGynRqRSFAUuKKJBQWYPDQzr3f_D5ArZ-Ok8:1rfzfM:cWQZT0ZzoQFrDQkSqB0zS6uNy34VGOWLTisVzvraPuc','2024-03-15 09:58:56.919920');

/*Table structure for table `forecaster_agent` */

DROP TABLE IF EXISTS `forecaster_agent`;

CREATE TABLE `forecaster_agent` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_agent_LOGIN_id_747fc920_fk_forecaster_login_id` (`LOGIN_id`),
  CONSTRAINT `forecaster_agent_LOGIN_id_747fc920_fk_forecaster_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `forecaster_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_agent` */

insert  into `forecaster_agent`(`id`,`name`,`photo`,`place`,`post`,`pin`,`phone`,`email`,`LOGIN_id`) values 
(8,'Rinshida.K','2.jpeg','Thuvvakkad','Pannippar',676541,9605695126,'rinshidak2002@gmail.com',21),
(9,'Asna E','th.jpeg','Payyand','pyd',676122,7736998477,'asnae2001@gmail.com',26),
(10,'Raniya','th (1).jpeg','Malappuram','mlp',676122,7736998477,'raniya@gmail.com',27);

/*Table structure for table `forecaster_complaint` */

DROP TABLE IF EXISTS `forecaster_complaint`;

CREATE TABLE `forecaster_complaint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_complaint_USER_id_eff8eb57_fk_forecaster_user_id` (`USER_id`),
  CONSTRAINT `forecaster_complaint_USER_id_eff8eb57_fk_forecaster_user_id` FOREIGN KEY (`USER_id`) REFERENCES `forecaster_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_complaint` */

insert  into `forecaster_complaint`(`id`,`Complaint`,`date`,`reply`,`USER_id`) values 
(1,'not picked','2023-11-25','good',1),
(2,'okk','2024-02-20','waiting',1),
(3,'okk','2024-02-20','waiting',1),
(4,'okk','2024-02-20','waiting',1),
(5,'okk','2024-02-20','waiting',1),
(6,'kkk','2024-02-20','waiting',1),
(7,'kkk','2024-02-20','waiting',1),
(8,'kkk','2024-02-20','waiting',1),
(9,'kkk','2024-02-20','waiting',1),
(10,'kkk','2024-02-20','waiting',1),
(11,'not good','2024-02-20','waiting',1),
(12,'','2024-02-21','waiting',1),
(13,'bad service ','2024-03-05','waiting',1),
(14,'','2024-03-05','waiting',1);

/*Table structure for table `forecaster_feedback` */

DROP TABLE IF EXISTS `forecaster_feedback`;

CREATE TABLE `forecaster_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_feedback_USER_id_567637d4_fk_forecaster_user_id` (`USER_id`),
  CONSTRAINT `forecaster_feedback_USER_id_567637d4_fk_forecaster_user_id` FOREIGN KEY (`USER_id`) REFERENCES `forecaster_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_feedback` */

insert  into `forecaster_feedback`(`id`,`date`,`feedback`,`USER_id`) values 
(1,'2023-11-25','good',1),
(2,'2024-02-20','okk',1),
(3,'2024-02-20','gd',1),
(4,'2024-02-20','gd',1),
(5,'2024-02-20','gd',1),
(6,'2024-02-20','gd',1),
(7,'2024-02-20','very good',1),
(8,'2024-02-20','very good',1),
(9,'2024-02-21','okk',1),
(10,'2024-03-05','good service ',1),
(11,'2024-03-05','1',1),
(12,'2024-03-05','',1),
(13,'2024-03-05','',1),
(14,'2024-03-21','very good service ',1);

/*Table structure for table `forecaster_login` */

DROP TABLE IF EXISTS `forecaster_login`;

CREATE TABLE `forecaster_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_login` */

insert  into `forecaster_login`(`id`,`username`,`password`,`type`) values 
(3,'asna','1234567','company'),
(4,'hanna','1234567','agent'),
(5,'raniya','123123','agent'),
(6,'12233','12345678','Agent'),
(7,'rinshida','12345678','Agent'),
(8,'asna','12345678','Agent'),
(9,'rinshi','12345678','Agent'),
(10,'user','user','user'),
(12,'rinshi','rinshi','User'),
(13,'maya','maya@123','User'),
(14,'maya','maya@123','User'),
(15,'rinshi','rinshi','User'),
(16,'rinshi','rinshi','User'),
(17,'rinshi','rinshi','User'),
(19,'hhh','hhh','User'),
(20,'asna','asna','User'),
(21,'rinshida','12345678','Agent'),
(22,'hanna','hanna','User'),
(23,'hanna','hanna','User'),
(24,'hanna','hanna','User'),
(25,'hanna','hanna','User'),
(26,'asna','asna','Agent'),
(27,'raniya','raniya','Agent');

/*Table structure for table `forecaster_order` */

DROP TABLE IF EXISTS `forecaster_order`;

CREATE TABLE `forecaster_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `amount` double NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_order_USER_id_0fa7b300_fk_forecaster_user_id` (`USER_id`),
  CONSTRAINT `forecaster_order_USER_id_0fa7b300_fk_forecaster_user_id` FOREIGN KEY (`USER_id`) REFERENCES `forecaster_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_order` */

insert  into `forecaster_order`(`id`,`date`,`status`,`amount`,`USER_id`) values 
(15,'2024-03-01','accept',90,1),
(16,'2024-03-01','ORDERD',420,5),
(18,'2024-03-01','accept',45,5),
(19,'2024-03-01','ORDERD',45,1),
(20,'2024-03-05','ORDERD',85,1),
(21,'2024-03-05','accept',5955,1),
(22,'2024-03-05','ORDERD',120,1),
(23,'2024-03-05','ORDERD',135,1),
(24,'2024-03-05','ORDERD',2420,1),
(25,'2024-03-05','ORDERD',800,1),
(26,'2024-03-21','reject',650,1),
(27,'2024-03-21','CART',120,1),
(28,'2024-03-21','accept',1450,1);

/*Table structure for table `forecaster_orderdetails` */

DROP TABLE IF EXISTS `forecaster_orderdetails`;

CREATE TABLE `forecaster_orderdetails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `quantity` int NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_orderdetails_ORDER_id_ceaf545a_fk_forecaster_order_id` (`ORDER_id`),
  KEY `forecaster_orderdeta_PRODUCT_id_f8cdcdf3_fk_forecaste` (`PRODUCT_id`),
  CONSTRAINT `forecaster_orderdeta_PRODUCT_id_f8cdcdf3_fk_forecaste` FOREIGN KEY (`PRODUCT_id`) REFERENCES `forecaster_product` (`id`),
  CONSTRAINT `forecaster_orderdetails_ORDER_id_ceaf545a_fk_forecaster_order_id` FOREIGN KEY (`ORDER_id`) REFERENCES `forecaster_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_orderdetails` */

insert  into `forecaster_orderdetails`(`id`,`date`,`quantity`,`ORDER_id`,`PRODUCT_id`,`amount`) values 
(19,'2024-03-19',10,21,7,5000),
(20,'2024-03-21',1,26,10,650),
(21,'2024-03-21',2,27,6,60),
(22,'2024-03-21',1,28,10,650),
(23,'2024-03-21',1,28,13,500),
(24,'2024-03-21',1,28,19,300);

/*Table structure for table `forecaster_payment` */

DROP TABLE IF EXISTS `forecaster_payment`;

CREATE TABLE `forecaster_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `amount` double NOT NULL,
  `ORDER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_payment_ORDER_id_4455289c_fk_forecaster_order_id` (`ORDER_id`),
  CONSTRAINT `forecaster_payment_ORDER_id_4455289c_fk_forecaster_order_id` FOREIGN KEY (`ORDER_id`) REFERENCES `forecaster_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_payment` */

/*Table structure for table `forecaster_picup_request` */

DROP TABLE IF EXISTS `forecaster_picup_request`;

CREATE TABLE `forecaster_picup_request` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `request` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `latitude` varchar(50) NOT NULL,
  `longitude` varchar(50) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_request_USER_id_e1a97391_fk_forecaster_user_id` (`USER_id`),
  CONSTRAINT `forecaster_request_USER_id_e1a97391_fk_forecaster_user_id` FOREIGN KEY (`USER_id`) REFERENCES `forecaster_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_picup_request` */

insert  into `forecaster_picup_request`(`id`,`request`,`date`,`status`,`latitude`,`longitude`,`USER_id`) values 
(1,'req1','2023-11-25','yes','34','67',1);

/*Table structure for table `forecaster_product` */

DROP TABLE IF EXISTS `forecaster_product`;

CREATE TABLE `forecaster_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `quantity` int NOT NULL,
  `price` double NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_product` */

insert  into `forecaster_product`(`id`,`name`,`image`,`quantity`,`price`,`description`) values 
(6,'Bag','bag.jpg',998,60,'cotton bags,1 kg capacity,different color are available'),
(7,'Backup Bag','backup bag.jpg',990,500,'1'),
(8,'Brush','brush.webp',1000,20,'1'),
(9,'Chair','chair.jpg',1000,800,'1'),
(10,'Chair Set','chairset.jpeg',998,650,'1'),
(11,'Chappal','chappal.jpg',1000,100,'1'),
(12,'Frock','dress.jpg',1000,150,'1'),
(13,'winebottle','winebottle.jpg',999,500,'1'),
(14,'Toy Car','toy.JPG',1000,50,'1'),
(15,'Tool Basket','tool basket.jpg',1000,65,'1'),
(16,'Paper Basket','paperbasket.jpg',1000,90,'1'),
(17,'Paper Bag','paper.webp',1000,45,'1'),
(18,'Bulb','light.jpg',1000,200,'1'),
(19,'Dress','frockk.jpg',999,300,'1'),
(20,'Flower Vase','flowervase.jpg',1000,140,'1'),
(21,'nnnnnnn','8940c6e5-421a-4a55-8239-4fcdfa9d74d3.jpeg',77,666,'nn');

/*Table structure for table `forecaster_user` */

DROP TABLE IF EXISTS `forecaster_user`;

CREATE TABLE `forecaster_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `phoneno` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `email` varchar(15) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_user_LOGIN_id_1d80ebda_fk_forecaster_login_id` (`LOGIN_id`),
  CONSTRAINT `forecaster_user_LOGIN_id_1d80ebda_fk_forecaster_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `forecaster_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_user` */

insert  into `forecaster_user`(`id`,`name`,`age`,`phoneno`,`LOGIN_id`,`email`,`image`) values 
(1,'rinshida',21,9605695126,10,'0','0'),
(2,'maya',18,9878987898,13,'maya@gmail.com',''),
(3,'maya',18,9878987898,14,'maya@gmail.com','d1517c9b5f72b915f7652779859c2224_i4vWAoT.jpg'),
(4,'hhh',19,9898989898,19,'hhhh@gmail.com','d1517c9b5f72b915f7652779859c2224_2dZkBYW.jpg'),
(5,'Asna',22,7736998477,20,'eee@gmail.com','IMG-20240227-WA0013_KLRIeyq.jpg'),
(6,'Hanna',22,7758669933,25,'hanna@gmail.com','Screenshot_20231015_103239_scQVYOH.jpg');

/*Table structure for table `forecaster_waste` */

DROP TABLE IF EXISTS `forecaster_waste`;

CREATE TABLE `forecaster_waste` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `image` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_waste_USER_id_371894c8_fk_forecaster_user_id` (`USER_id`),
  CONSTRAINT `forecaster_waste_USER_id_371894c8_fk_forecaster_user_id` FOREIGN KEY (`USER_id`) REFERENCES `forecaster_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_waste` */

insert  into `forecaster_waste`(`id`,`date`,`image`,`USER_id`) values 
(1,'2023-12-02','a_z0GTXUW.jpg',1),
(2,'2024-02-21','Screenshot_20240104_215124_ch2zGrJ.jpg',1),
(3,'2024-02-21','Screenshot_20240104_215124_CeGBAtc.jpg',1),
(4,'2024-02-27','Screenshot_20240104_215124_UnGKtx1.jpg',1),
(5,'2024-03-05','Screenshot_20240219-114804.png',1),
(6,'2024-03-05','ada7f90525e574559f74c682aba2c1ce.jpg',1),
(7,'2024-03-05','IMG-20240303-WA0015.jpg',1),
(8,'2024-03-05','7874a52527b6610d92cbb9330e71ab76.jpg',1),
(9,'2024-03-05','IMG-20240304-WA0023.jpg',1),
(10,'2024-03-05','IMG-20240304-WA0023_Ef1J04o.jpg',1),
(11,'2024-03-05','IMG-20240303-WA0014.jpg',1),
(12,'2024-03-19','IMG-20240318-WA0071.jpg',1),
(13,'2024-03-19','lets-rid-the-world-of-gross-used-plastic-bandaids-609209_1600x.jpg',1),
(14,'2024-03-19','batteries-scaled.jpg',1),
(15,'2024-03-19','Electric_batteries.jpg',1),
(16,'2024-03-19','themovegarbagebowl.jpg',1),
(17,'2024-03-19','WASTEBOWL33bis.jpg',1),
(18,'2024-03-19','old_bread1_1125_768-760x490.jpg',1),
(19,'2024-03-19','light-bulb-recycling-waste-legacy-tungsten-on-white-background-GJ5BDK.jpg',1),
(20,'2024-03-19','light-bulb-recycling-waste-legacy-tungsten-on-white-background-GJ5BDK_f7nHqP4.jpg',1),
(21,'2024-03-19','How-to-dispose-of-mercury-containing-light-bulbs-.jpg',1),
(22,'2024-03-19','isolated-shot-of-opened-blank-cardboard-box-on-white-background.jpg',1),
(23,'2024-03-19','71UWDcGtotL._AC_UF1000,1000_QL80_.jpg',1),
(24,'2024-03-19','31p3b5VBbwL._AC_UF894,1000_QL80_.jpg',1),
(25,'2024-03-01','Chopsticks.jpg',1),
(26,'2024-03-05','cigarette-butt-platt-1.jpg',1),
(27,'2024-03-05','51yl8DfxAoS._AC_UF1000,1000_QL80_.jpg',1),
(28,'2024-03-14','618XSczfoCL._AC_UF894,1000_QL80_.jpg',1),
(29,'2024-03-14','adheretech_bottle_640.1419978907.png',1),
(30,'2024-03-15','887b93376e36920d605e5875cb098125.jpg',1),
(31,'2024-03-15','red-nail-polish-bottle-on-600w-128549054.jpg',1),
(32,'2024-03-16','collection-newspapers.jpg',1),
(33,'2024-03-18','40288173_1-brodees-cotton-kitchentable-napkin-red-checked-45-x-45-cm-easy-wash.jpg',1),
(34,'2024-03-19','-1117Wx1400H-465706589-offwhite-MODEL.jpg',1),
(35,'2024-03-21','napkin.jpg',1),
(36,'2024-03-21','napkin_VVAruUp.jpg',1),
(37,'2024-03-21','IMG-20240321-WA0034.jpg',1),
(38,'2024-03-21','IMG_20240313_110934875.jpg',1),
(39,'2024-03-25','landfill-site-waste-glass-close-up-WDF00393.jpg',1),
(40,'2024-04-06','IMG-20240405-WA0023.jpg',1),
(41,'2024-04-06','Screenshot_20240403-135840.png',1),
(42,'2024-04-06','batteries-scaled_qZzWQSw.jpg',1),
(43,'2024-04-06','ImageForNews_59851_16615112202202141_C4qgkU3.jpg',1),
(44,'2024-04-06','IMG-20240406-WA0051.jpg',1),
(45,'2024-04-06','2nd-blog.jpg',1),
(46,'2024-04-06','a9364530-f04d-4706-a9e0-9a8e4714281e.jpg',1),
(47,'2024-04-06','IMG-20240406-WA0050.jpg',1),
(48,'2024-04-06','IMG-20240406-WA0050_c7xBZVp.jpg',1),
(49,'2024-04-06','9a8ff333-dbea-4051-9714-1c8a94a986c6__t.jpg',1),
(50,'2024-04-06','9a8ff333-dbea-4051-9714-1c8a94a986c6__t_umJOZQE.jpg',1),
(51,'2024-04-06','newsprint-backdrop.jpg',1),
(52,'2024-04-06','How-to-dispose-of-mercury-containing-light-bulbs-_d0M8qE3.jpg',1),
(53,'2024-04-06','How-to-dispose-of-mercury-containing-light-bulbs-_7pddDlM.jpg',1);

/*Table structure for table `forecaster_work_assign` */

DROP TABLE IF EXISTS `forecaster_work_assign`;

CREATE TABLE `forecaster_work_assign` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `wtype` varchar(50) NOT NULL,
  `AGENT_id` bigint NOT NULL,
  `REQUEST_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forecaster_work_AGENT_id_f087d555_fk_forecaster_agent_id` (`AGENT_id`),
  KEY `forecaster_work_REQUEST_id_d63a8be7_fk_forecaste` (`REQUEST_id`),
  CONSTRAINT `forecaster_work_AGENT_id_f087d555_fk_forecaster_agent_id` FOREIGN KEY (`AGENT_id`) REFERENCES `forecaster_agent` (`id`),
  CONSTRAINT `forecaster_work_REQUEST_id_d63a8be7_fk_forecaste` FOREIGN KEY (`REQUEST_id`) REFERENCES `forecaster_picup_request` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `forecaster_work_assign` */

insert  into `forecaster_work_assign`(`id`,`date`,`status`,`wtype`,`AGENT_id`,`REQUEST_id`) values 
(12,'2024-03-21','pending','pickup',8,1),
(16,'2024-03-25','completed','collection',8,1),
(17,'2024-03-25','completed','waste collection',8,1),
(18,'2024-03-25','completed','waste collection',8,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
