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
-- Dumping events for database 'hoothousingdb'
--

--
-- Dumping routines for database 'hoothousingdb'
--
/*!50003 DROP PROCEDURE IF EXISTS `add_property` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`HootDB`@`%` PROCEDURE `add_property`(
		IN	_prop_name		VARCHAR(100),
        IN	_street_number	VARCHAR(45),
		IN	_street_name	VARCHAR(45),
		IN	_unit			VARCHAR(45),
		IN	_city			VARCHAR(45),
		IN	_state			VARCHAR(45),
		IN	_zip			VARCHAR(45),
		IN	_manager_id		INT(11),
        IN	_img_href		VARCHAR(500),
        IN	_beds			FLOAT,
        IN	_baths			FLOAT,
        IN	_type_id		INT(11),
        IN	_distance		FLOAT,
        IN	_campus_id		INT(11)
    )
BEGIN

		INSERT INTO properties
        (
			prop_name,
            street_number,
            street_name,
            unit,
            city,
            state,
            zip,
            manager_id,
            prop_img_href,
            beds,
            baths,
            type_id,
            distance,
            campus_id
           
        
        )
        VALUES
        (
			_prop_name,
            _street_number,
            _street_name,
            _unit,
            _city,
            _state,
            _zip,
            _manager_id,
            _img_href,
            _beds,
            _baths,
            _type_id,
            _distance,
            _campus_id
            
            
        );
        



END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_management_info` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`HootDB`@`%` PROCEDURE `get_management_info`(

		IN		_manager_id		INT(11)

)
BEGIN

	SELECT
		managers.manager_id,
        managers.mgmt_name,
        
        CONCAT(managers.street_number, 
			' ',
			managers.street_name, 
			' ', 
			IFNULL(managers.unit,'')), 
		CONCAT(managers.city, 
			', ', 
			managers.state,
            ', ', 
            managers.zip),
        
        CONCAT('(', SUBSTR(managers.phone,1,3), ') ', SUBSTR(managers.phone,4,3), '-', SUBSTR(managers.phone,7,4)),

        managers.avg_mgmt_rating,
        managers.avg_prop_rating,
        managers.avg_recommend,
        managers.mgmt_img_href
	FROM managers
    WHERE managers.manager_id = _manager_id;
        
        
        
	SELECT
		properties.property_id,
        properties.prop_name,
        
        CONCAT(properties.street_number, 
			' ',
			properties.street_name, 
			' ', 
			IFNULL(properties.unit,'')), 
		
        properties.avg_prop_rating, 
		properties.prop_img_href,
        properties.manager_id,
        managers.mgmt_name,
		properties.review_count,
        properties.type_id
        
	FROM properties
    INNER JOIN managers ON properties.manager_id = managers.manager_id
    WHERE properties.manager_id = _manager_id;
        
		


END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_properties` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`HootDB`@`%` PROCEDURE `get_properties`(

	IN		_campus_id 		INT(11),
	IN		_distance		FLOAT,
	IN		_beds			FLOAT,
    IN		_baths			FLOAT,
	IN		_min_rent		INT(11),
	IN		_max_rent		INT(11),
    IN		_type_id		INT(11),
    IN		_manager_id		INT(11),
    IN		_property_id	INT(11)

)
BEGIN
	
	SELECT 
		properties.property_id,
		properties.prop_name, 
		
		CONCAT(properties.street_number, 
			' ',
			properties.street_name, 
			' ', 
			IFNULL(properties.unit,'')), 
		CONCAT(properties.city, 
			', ', 
			properties.state,
            ', ', 
            properties.zip),
		properties.avg_prop_rating, 
		properties.prop_img_href,
        properties.manager_id,
        managers.mgmt_name,
		properties.review_count,
        properties.type_id
        
    FROM properties
    INNER JOIN managers ON properties.manager_id = managers.manager_id
    
    WHERE 
		(_campus_id 	is null OR properties.campus_id 		= 	_campus_id	) 	AND
        (_distance 		is null OR properties.distance 			< 	_distance	)	AND
		(_beds			is null OR properties.beds 				>= 	_beds		)	AND
        (_baths			is null OR properties.baths 			>= 	_baths		)	AND
        (_min_rent		is null OR properties.avg_prop_rating	>= 	_min_rent	)	AND
        (_max_rent		is null OR properties.avg_prop_rating	<= 	_max_rent	)	AND
		(_type_id 		is null OR properties.type_id			=	_type_id	)	AND
		(_manager_id	is null OR properties.manager_id		=	_manager_id	)	AND
        (_property_id	is null OR properties.property_id		=	_property_id)	;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_properties_by_search` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`HootDB`@`%` PROCEDURE `get_properties_by_search`(

	IN		_campus_id 		INT(11),
	IN		_keyword		VARCHAR(100)

)
BEGIN
	
	SELECT 
		properties.property_id,
		properties.prop_name, 
		
		CONCAT(properties.street_number, 
			' ',
			properties.street_name, 
			' ', 
			IFNULL(properties.unit,'')), 
		CONCAT(properties.city, 
			', ', 
			properties.state,
            ', ', 
            properties.zip),
		properties.avg_prop_rating, 
		properties.prop_img_href,
        properties.manager_id,
        managers.mgmt_name,
		properties.review_count
        
    FROM properties
    INNER JOIN managers ON properties.manager_id = managers.manager_id
    
    WHERE 
		(_campus_id 	is null OR properties.campus_id 		= 	_campus_id	) 	AND
			(
				(properties.prop_name LIKE CONCAT('%',_keyword,'%')	)	OR
                
				(CONCAT(properties.street_number, ' ', properties.street_name, ' ', IFNULL(properties.unit,'')) LIKE CONCAT('%',_keyword,'%'))		OR
                
                (managers.mgmt_name LIKE CONCAT('%',_keyword,'%')	)
            )
        ;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_property_info` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`HootDB`@`%` PROCEDURE `get_property_info`(
		IN		_property_id	INT(11)

)
BEGIN

	SELECT
		properties.property_id,
        properties.prop_name,
        
        CONCAT(properties.street_number, 
			' ',
			properties.street_name, 
			' ', 
			IFNULL(managers.unit,'')), 
		CONCAT(properties.city, 
			', ', 
			properties.state,
            ', ', 
            properties.zip),

        properties.manager_id,
        managers.mgmt_name,
        properties.avg_prop_rating,
        properties.prop_img_href,
        properties.review_count,
        properties.type_id
	
    FROM properties
    INNER JOIN managers ON properties.manager_id = managers.manager_id
    WHERE properties.property_id = _property_id;
        
        
	SELECT
		reviews.review_id,
        reviews.title,
        
        CONCAT(reviews.user_href, 
			' ',
			reviews.create_dtm),
		
        reviews.property_rating, 
		reviews.manager_rating,
        reviews.rent_share,
        reviews.recommended,
        reviews.text,
		reviews.property_id
        
	FROM reviews
    WHERE reviews.property_id = _property_id;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `save_review` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`HootDB`@`%` PROCEDURE `save_review`(
	IN 			_title				VARCHAR(100),
    IN			_text				TEXT,
    IN			_manager_rating 	INT(11),
    IN			_property_rating 	INT(11),
    IN			_recommended		TINYINT(1),
	IN			_property_id		INT(11),
    IN			_user_href			VARCHAR(100),
    IN			_rent_share			INT(11)
)
BEGIN


INSERT INTO reviews
         (
		title, 
        text,
        manager_rating,
        property_rating,
		recommended,
        property_id,
		user_href,
		rent_share
		)
	
    VALUES 
		(
		_title, 
        _text,
		_manager_rating,
        _property_rating,
		_recommended,
        _property_id,
		_user_href,
		_rent_share
		);
        
CALL update_prop_rating(_property_id);


END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_prop_rating` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`HootDB`@`%` PROCEDURE `update_prop_rating`(
		IN		_property_id	INT(11)

)
BEGIN 

/* GET PROPERTY AVERAGE RATING 
	Calculated by averaging property ratings from all reviews of this property */    
    
    SET @prop_average = (
		SELECT 
			AVG(reviews.property_rating) 
			FROM reviews
			WHERE reviews.property_id = _property_id LIMIT 1);
        
	IF(@prop_average IS NULL) THEN
        SET @prop_average = 0;
    END IF;
    
    
/* UPDATE PROPERTY AVERAGE RATING
	Update this property with the newly calculated property average rating*/    
	
    UPDATE properties 
		SET properties.avg_prop_rating = @prop_average
		WHERE properties.property_id = _property_id;


/* GET MANAGER ID
	Of this property*/
	
    SET @manager_id = (
		SELECT
			manager_id
		FROM properties
        WHERE properties.property_id = _property_id LIMIT 1);

	IF(@manager_id IS NULL) THEN
        SET @manager_id = 0;
    END IF;


/* GET MANAGMENT AVERAGE RATING */  
    
    SET @managment_average = (
		SELECT 
			AVG(reviews.manager_rating) 
			FROM reviews
            INNER JOIN properties ON properties.property_id = reviews.property_id
			WHERE properties.manager_id = @manager_id LIMIT 1);
		
    IF(@managment_average IS NULL) THEN
        SET @managment_average = 0;
    END IF;
    

/* GET AVERAGE PROPERTY RATING FOR MANAGMENT */  
    
    SET @managment_property_average = (
		SELECT 
			AVG(properties.avg_prop_rating) 
			FROM properties
			WHERE properties.manager_id = @manager_id LIMIT 1);
		
    IF(@managment_property_average IS NULL) THEN
        SET @managment_property_average = 0;
    END IF;
    
   
/* GET RECOMMEND AVERAGE FOR PROPERTY */     
   
   SET @property_recommend_average = (
		SELECT 
			AVG(reviews.recommended) 
			FROM reviews
			WHERE properties.manager_id = @manager_id LIMIT 1);
		
    IF(@property_recommend_average IS NULL) THEN
        SET @property_recommend_average = 0;
    END IF;
   
   
/* UPDATE MANAGER AVERAGE RATING */
    
    UPDATE managers 
		SET managers.avg_mgmt_rating = @managment_average,
			managers.avg_prop_rating = @managment_property_average
		WHERE managers.manager_id = @manager_id;


  
	




END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-04  1:02:42
