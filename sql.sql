/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 8.0.31 : Database - arts_program
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`arts_program` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `arts_program`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(25,'Can add candidate',7,'add_candidate'),
(26,'Can change candidate',7,'change_candidate'),
(27,'Can delete candidate',7,'delete_candidate'),
(28,'Can view candidate',7,'view_candidate'),
(29,'Can add groups',8,'add_groups'),
(30,'Can change groups',8,'change_groups'),
(31,'Can delete groups',8,'delete_groups'),
(32,'Can view groups',8,'view_groups'),
(33,'Can add judge',9,'add_judge'),
(34,'Can change judge',9,'change_judge'),
(35,'Can delete judge',9,'delete_judge'),
(36,'Can view judge',9,'view_judge'),
(37,'Can add login',10,'add_login'),
(38,'Can change login',10,'change_login'),
(39,'Can delete login',10,'delete_login'),
(40,'Can view login',10,'view_login'),
(41,'Can add program',11,'add_program'),
(42,'Can change program',11,'change_program'),
(43,'Can delete program',11,'delete_program'),
(44,'Can view program',11,'view_program'),
(45,'Can add rulesandregulation',12,'add_rulesandregulation'),
(46,'Can change rulesandregulation',12,'change_rulesandregulation'),
(47,'Can delete rulesandregulation',12,'delete_rulesandregulation'),
(48,'Can view rulesandregulation',12,'view_rulesandregulation'),
(49,'Can add programschedule',13,'add_programschedule'),
(50,'Can change programschedule',13,'change_programschedule'),
(51,'Can delete programschedule',13,'delete_programschedule'),
(52,'Can view programschedule',13,'view_programschedule'),
(53,'Can add programjudgeallocation',14,'add_programjudgeallocation'),
(54,'Can change programjudgeallocation',14,'change_programjudgeallocation'),
(55,'Can delete programjudgeallocation',14,'delete_programjudgeallocation'),
(56,'Can view programjudgeallocation',14,'view_programjudgeallocation'),
(57,'Can add programenrollment',15,'add_programenrollment'),
(58,'Can change programenrollment',15,'change_programenrollment'),
(59,'Can delete programenrollment',15,'delete_programenrollment'),
(60,'Can view programenrollment',15,'view_programenrollment'),
(61,'Can add groupleaders',16,'add_groupleaders'),
(62,'Can change groupleaders',16,'change_groupleaders'),
(63,'Can delete groupleaders',16,'delete_groupleaders'),
(64,'Can view groupleaders',16,'view_groupleaders'),
(65,'Can add feedback',17,'add_feedback'),
(66,'Can change feedback',17,'change_feedback'),
(67,'Can delete feedback',17,'delete_feedback'),
(68,'Can view feedback',17,'view_feedback'),
(69,'Can add complaint',18,'add_complaint'),
(70,'Can change complaint',18,'change_complaint'),
(71,'Can delete complaint',18,'delete_complaint'),
(72,'Can view complaint',18,'view_complaint'),
(73,'Can add award',19,'add_award'),
(74,'Can change award',19,'change_award'),
(75,'Can delete award',19,'delete_award'),
(76,'Can view award',19,'view_award'),
(77,'Can add candidateresult',20,'add_candidateresult'),
(78,'Can change candidateresult',20,'change_candidateresult'),
(79,'Can delete candidateresult',20,'delete_candidateresult'),
(80,'Can view candidateresult',20,'view_candidateresult'),
(81,'Can add groupresult',21,'add_groupresult'),
(82,'Can change groupresult',21,'change_groupresult'),
(83,'Can delete groupresult',21,'delete_groupresult'),
(84,'Can view groupresult',21,'view_groupresult');

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
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'Myapp','candidate'),
(8,'Myapp','groups'),
(9,'Myapp','judge'),
(10,'Myapp','login'),
(11,'Myapp','program'),
(12,'Myapp','rulesandregulation'),
(13,'Myapp','programschedule'),
(14,'Myapp','programjudgeallocation'),
(15,'Myapp','programenrollment'),
(16,'Myapp','groupleaders'),
(17,'Myapp','feedback'),
(18,'Myapp','complaint'),
(19,'Myapp','award'),
(20,'Myapp','candidateresult'),
(21,'Myapp','groupresult');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'Myapp','0001_initial','2023-12-16 06:40:35.455230'),
(2,'contenttypes','0001_initial','2023-12-16 06:40:35.518126'),
(3,'auth','0001_initial','2023-12-16 06:40:36.388462'),
(4,'admin','0001_initial','2023-12-16 06:40:36.704674'),
(5,'admin','0002_logentry_remove_auto_add','2023-12-16 06:40:36.720284'),
(6,'admin','0003_logentry_add_action_flag_choices','2023-12-16 06:40:36.736024'),
(7,'contenttypes','0002_remove_content_type_name','2023-12-16 06:40:36.814873'),
(8,'auth','0002_alter_permission_name_max_length','2023-12-16 06:40:36.864557'),
(9,'auth','0003_alter_user_email_max_length','2023-12-16 06:40:36.927148'),
(10,'auth','0004_alter_user_username_opts','2023-12-16 06:40:36.949300'),
(11,'auth','0005_alter_user_last_login_null','2023-12-16 06:40:36.993929'),
(12,'auth','0006_require_contenttypes_0002','2023-12-16 06:40:36.993929'),
(13,'auth','0007_alter_validators_add_error_messages','2023-12-16 06:40:37.005436'),
(14,'auth','0008_alter_user_username_max_length','2023-12-16 06:40:37.053564'),
(15,'auth','0009_alter_user_last_name_max_length','2023-12-16 06:40:37.117798'),
(16,'auth','0010_alter_group_name_max_length','2023-12-16 06:40:37.163330'),
(17,'auth','0011_update_proxy_permissions','2023-12-16 06:40:37.178968'),
(18,'auth','0012_alter_user_first_name_max_length','2023-12-16 06:40:37.231026'),
(19,'sessions','0001_initial','2023-12-16 06:40:37.306689'),
(20,'Myapp','0002_alter_programschedule_date','2023-12-16 08:37:21.701918'),
(21,'Myapp','0003_programjudgeallocation_programeshedule','2023-12-16 09:25:31.303782'),
(22,'Myapp','0004_remove_programenrollment_programme_and_more','2023-12-24 09:41:24.398793'),
(23,'Myapp','0005_alter_feedback_date_candidateresult','2024-01-22 09:46:42.624488'),
(24,'Myapp','0006_rename_year_award_grade','2024-01-22 10:46:58.942841'),
(25,'Myapp','0007_rename_awardtype_award_chessnumber_and_more','2024-01-27 07:26:39.796581'),
(26,'Myapp','0008_rename_groups_award_groups','2024-01-27 08:07:03.813540'),
(27,'Myapp','0009_remove_award_position','2024-01-31 10:46:07.028950'),
(28,'Myapp','0010_groupresult','2024-02-01 07:19:54.626131');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('rm46amy0wsf28crzw53shtfwtydw81sp','eyJsaWQiOjF9:1rEOQG:g_Jdmae-yGOgjDoqXiZG1Kb2ZEc7i0P_mla7r8iOvM0','2023-12-30 06:45:16.856898'),
('kss7hvjcj5x3ofipulxyo879z36e9cht','eyJsaWQiOjR9:1rI1JY:cT6WslxrS5uC35ua7asR-Wp6Q8vsehSK0cAUJYajNes','2024-01-09 06:53:20.263206'),
('ixkm8o59rjne6koiz6cw7r7vn97r5dm9','eyJsaWQiOjZ9:1rJVKs:cKJ_rmBpJvTNJsaVeBGkz-1wwFGdw9ET67pcdzvIbxo','2024-01-13 09:08:50.440931'),
('qgw0h77jnptz7qqevwah0czz9cien47m','eyJsaWQiOjF9:1rVTET:tWb86_eCNLJhJoWgSIr9tj7w9SAZ6QBvjQkztM6Tj4k','2024-02-15 09:19:41.476554');

/*Table structure for table `myapp_award` */

DROP TABLE IF EXISTS `myapp_award`;

CREATE TABLE `myapp_award` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `chessnumber` varchar(100) NOT NULL,
  `grade` varchar(100) NOT NULL,
  `CANDIDATE_id` bigint NOT NULL,
  `GROUPS_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_award_CANDIDATE_id_49a1b0fd` (`CANDIDATE_id`),
  KEY `Myapp_award_groups_id_5049c8a9` (`GROUPS_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_award` */

/*Table structure for table `myapp_candidate` */

DROP TABLE IF EXISTS `myapp_candidate`;

CREATE TABLE `myapp_candidate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phoneno` varchar(100) NOT NULL,
  `GROUP_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `PROGRAM_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_candidate_GROUP_id_328be37e` (`GROUP_id`),
  KEY `Myapp_candidate_LOGIN_id_f4154cd7` (`LOGIN_id`),
  KEY `Myapp_candidate_PROGRAM_id_c3fd16a5` (`PROGRAM_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_candidate` */

insert  into `myapp_candidate`(`id`,`name`,`gender`,`course`,`email`,`phoneno`,`GROUP_id`,`LOGIN_id`,`PROGRAM_id`) values 
(1,'c1','female','bca','c1@gmail.com','111111',1,6,1),
(2,'c2','male','bba','c2@gmail.com','123456789',3,7,2),
(3,'cl1','male','bba','cl1@gmail.com','123456789',3,10,1);

/*Table structure for table `myapp_candidateresult` */

DROP TABLE IF EXISTS `myapp_candidateresult`;

CREATE TABLE `myapp_candidateresult` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mark` varchar(10) NOT NULL,
  `CANDIDATE_id` bigint NOT NULL,
  `JUDGE_id` bigint NOT NULL,
  `PROGRAMME_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_candidateresult_CANDIDATE_id_cd351696` (`CANDIDATE_id`),
  KEY `Myapp_candidateresult_JUDGE_id_47ebbb43` (`JUDGE_id`),
  KEY `Myapp_candidateresult_PROGRAMME_id_a53b39b4` (`PROGRAMME_id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_candidateresult` */

insert  into `myapp_candidateresult`(`id`,`mark`,`CANDIDATE_id`,`JUDGE_id`,`PROGRAMME_id`) values 
(27,'10',3,4,1),
(26,'9',1,4,1),
(25,'10',3,3,1),
(24,'7',1,3,1),
(23,'10',3,2,1),
(22,'10',1,2,1);

/*Table structure for table `myapp_complaint` */

DROP TABLE IF EXISTS `myapp_complaint`;

CREATE TABLE `myapp_complaint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `replay` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_complaint_LOGIN_id_0c893bb9` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaint` */

insert  into `myapp_complaint`(`id`,`complaint`,`date`,`status`,`replay`,`type`,`LOGIN_id`) values 
(21,'no','2024-01-13','pending','pending','candidate',6),
(20,'no','2024-01-13','pending','pending','candidate',6),
(19,'no','2024-01-13','pending','pending','candidate',6),
(18,'no','2024-01-13','pending','pending','candidate',6),
(17,'no good','2024-01-13','pending','pending','candidate',6),
(16,'qwertyuioihgf','2023-12-30','pending','pending','candidate',4),
(15,'llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll','2023-12-19','replied','qqwqqrtyuhi','groupleaders',2),
(14,'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj','2023-12-19','pending','pending','candidate',6),
(13,'cccccccccccccccccccccccccccccccccccccc','2023-12-19','pending','pending','candidate',6),
(22,'hellooooo','2024-01-20','pending','pending','candidate',6);

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_feedback_LOGIN_id_1823bf34` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`feedback`,`date`,`type`,`LOGIN_id`) values 
(1,'dxfcgvhbjnkm','2023-12-16','groupleaders',2),
(2,'asxcvbnmko','2023-12-16','judge',4),
(3,'k','2023-12-16','judge',4),
(6,'yuh','2024-01-20','candidate',6),
(5,'sdfghjklkjhgfdcvbnm............','2023-12-18','candidate',6),
(7,'week','2024-01-20','candidate',6);

/*Table structure for table `myapp_groupleaders` */

DROP TABLE IF EXISTS `myapp_groupleaders`;

CREATE TABLE `myapp_groupleaders` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phoneno` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `GROUP_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_groupleaders_GROUP_id_68e83d5d` (`GROUP_id`),
  KEY `Myapp_groupleaders_LOGIN_id_7b745719` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_groupleaders` */

insert  into `myapp_groupleaders`(`id`,`name`,`course`,`email`,`phoneno`,`gender`,`GROUP_id`,`LOGIN_id`) values 
(1,'anu','bca','anu@gmail.com','111111','male',1,2),
(2,'l2','bba','l2@gmail.com','111','male',3,9);

/*Table structure for table `myapp_groupresult` */

DROP TABLE IF EXISTS `myapp_groupresult`;

CREATE TABLE `myapp_groupresult` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `point` varchar(100) NOT NULL,
  `GROUP_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_groupresult_GROUP_id_552c13d1` (`GROUP_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_groupresult` */

/*Table structure for table `myapp_groups` */

DROP TABLE IF EXISTS `myapp_groups`;

CREATE TABLE `myapp_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `groupname` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_groups` */

insert  into `myapp_groups`(`id`,`groupname`) values 
(1,'group A'),
(3,'group B');

/*Table structure for table `myapp_judge` */

DROP TABLE IF EXISTS `myapp_judge`;

CREATE TABLE `myapp_judge` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `hname` varchar(100) NOT NULL,
  `proffession` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phoneno` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_judge_LOGIN_id_1dee6c8e` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_judge` */

insert  into `myapp_judge`(`id`,`name`,`place`,`hname`,`proffession`,`email`,`phoneno`,`gender`,`LOGIN_id`) values 
(3,'j2','ss','ss','dance','j2@gmail.com','333','Male',5),
(2,'jidge1','aaaa','aaaaa','dance','judge1@gmail.com','111111','Male',4),
(4,'j3','aaa','aaa','aa','j3@gmail.com','123456789','Male',8);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`Password`,`type`) values 
(1,'admin','admin','admin'),
(2,'anu@gmail.com','111111','groupleaders'),
(4,'judge1@gmail.com','222222','judge'),
(5,'j2@gmail.com','333','judge'),
(6,'c1@gmail.com','111','candidate'),
(7,'c2@gmail.com','123456789','candidate'),
(8,'j3@gmail.com','123456789','judge'),
(9,'l2@gmail.com','111','groupleaders'),
(10,'cl1@gmail.com','123456789','candidate');

/*Table structure for table `myapp_program` */

DROP TABLE IF EXISTS `myapp_program`;

CREATE TABLE `myapp_program` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `programname` varchar(100) NOT NULL,
  `programtype` varchar(100) NOT NULL,
  `groupprogram` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_program` */

insert  into `myapp_program`(`id`,`programname`,`programtype`,`groupprogram`,`description`) values 
(1,'oppana','girls','yes','8-10'),
(2,'folk dance','girls','yes','6-8');

/*Table structure for table `myapp_programenrollment` */

DROP TABLE IF EXISTS `myapp_programenrollment`;

CREATE TABLE `myapp_programenrollment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `CANDIDATE_id` bigint NOT NULL,
  `PROGRAMMESCHEDULE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_programenrollment_CANDIDATE_id_b595227a` (`CANDIDATE_id`),
  KEY `Myapp_programenrollment_PROGRAMMESCHEDULE_id_0ff20324` (`PROGRAMMESCHEDULE_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_programenrollment` */

insert  into `myapp_programenrollment`(`id`,`CANDIDATE_id`,`PROGRAMMESCHEDULE_id`) values 
(1,1,1);

/*Table structure for table `myapp_programjudgeallocation` */

DROP TABLE IF EXISTS `myapp_programjudgeallocation`;

CREATE TABLE `myapp_programjudgeallocation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `JUDGE_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `PROGRAMME_id` bigint NOT NULL,
  `PROGRAMESHEDULE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_programjudgeallocation_JUDGE_id_3823e0fb` (`JUDGE_id`),
  KEY `Myapp_programjudgeallocation_LOGIN_id_90156b39` (`LOGIN_id`),
  KEY `Myapp_programjudgeallocation_PROGRAMME_id_648f223f` (`PROGRAMME_id`),
  KEY `Myapp_programjudgeallocation_PROGRAMESHEDULE_id_97e89719` (`PROGRAMESHEDULE_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_programjudgeallocation` */

insert  into `myapp_programjudgeallocation`(`id`,`JUDGE_id`,`LOGIN_id`,`PROGRAMME_id`,`PROGRAMESHEDULE_id`) values 
(3,2,1,1,1),
(4,3,1,1,1),
(5,4,1,1,1);

/*Table structure for table `myapp_programschedule` */

DROP TABLE IF EXISTS `myapp_programschedule`;

CREATE TABLE `myapp_programschedule` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `fromtime` varchar(100) NOT NULL,
  `totime` varchar(100) NOT NULL,
  `stage` varchar(100) NOT NULL,
  `PROGRAM_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_programschedule_PROGRAM_id_47a0b95d` (`PROGRAM_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_programschedule` */

insert  into `myapp_programschedule`(`id`,`date`,`fromtime`,`totime`,`stage`,`PROGRAM_id`) values 
(1,'2023-12-21','12:30','1:30','stage1',1),
(2,'2023-12-11','12:30','1:30','stage3',1);

/*Table structure for table `myapp_rulesandregulation` */

DROP TABLE IF EXISTS `myapp_rulesandregulation`;

CREATE TABLE `myapp_rulesandregulation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rules` varchar(100) NOT NULL,
  `PROGRAMME_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Myapp_rulesandregulation_PROGRAMME_id_7be39967` (`PROGRAMME_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_rulesandregulation` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
