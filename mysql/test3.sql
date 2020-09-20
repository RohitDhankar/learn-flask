CREATE TABLE IF NOT EXISTS `schema_flask`.`users_has_location` (
  `users_id` INT NOT NULL,
  `location_location_id` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`users_id`, `location_location_id`),
  INDEX `fk_users_has_location_location1_idx` (`location_location_id` ASC),
  INDEX `fk_users_has_location_users_idx` (`users_id` ASC),
  CONSTRAINT `fk_users_has_location_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `mydb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_location_location1`
    FOREIGN KEY (`location_location_id`)
    REFERENCES `mydb`.`location` (`location_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;