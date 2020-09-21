CREATE TABLE IF NOT EXISTS `flask_schema`.`location` (
  `city` CHAR(1) NULL,
  `country` VARCHAR(45) NULL,
  `location_id` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`location_id`))
ENGINE = InnoDB;