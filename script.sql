-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Style_Tattoo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Style_Tattoo` (
  `idStyle_Tattoo` INT NOT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`idStyle_Tattoo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Area` (
  `idArea` INT NOT NULL,
  `Nombre_Area` VARCHAR(45) NULL,
  PRIMARY KEY (`idArea`))
ENGINE = InnoDB
COMMENT = '		\n\n';


-- -----------------------------------------------------
-- Table `mydb`.`Tatuadores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Tatuadores` (
  `idTatuador` INT NOT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Apellido_P` VARCHAR(45) NULL,
  `Apellido_M` VARCHAR(45) NULL,
  `Estilo` INT NULL,
  `Area` INT NULL,
  PRIMARY KEY (`idTatuador`),
  INDEX `fk_Area_idx` (`Area` ASC) ,
  CONSTRAINT `fk_Style`
    FOREIGN KEY (`Estilo`)
    REFERENCES `mydb`.`Style_Tattoo` (`idStyle_Tattoo`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Area`
    FOREIGN KEY (`Area`)
    REFERENCES `mydb`.`Area` (`idArea`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Clientes` (
  `idClientes` INT NOT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Edad` INT NULL,
  `Celular` INT NULL,
  PRIMARY KEY (`idClientes`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Capturista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Capturista` (
  `idCapturista` INT NOT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Apellido_P` VARCHAR(45) NULL,
  `Apellido_M` VARCHAR(45) NULL,
  `Area` INT NULL,
  PRIMARY KEY (`idCapturista`),
  INDEX `fk_Area` (`Area` ASC) ,
  CONSTRAINT `fk_Area`
    FOREIGN KEY (`Area`)
    REFERENCES `mydb`.`Area` (`idArea`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Ticket`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Ticket` (
  `idTicket` INT NOT NULL,
  `idCliente` INT NULL,
  `idTrabajadores` INT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Tatuador` VARCHAR(45) NULL,
  `Precio` INT NULL,
  PRIMARY KEY (`idTicket`),
  INDEX `fkTrabajador_idx` (`idTrabajadores` ASC) ,
  CONSTRAINT `fkCliente`
    FOREIGN KEY (`idCliente`)
    REFERENCES `mydb`.`Clientes` (`idClientes`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fkTrabajador`
    FOREIGN KEY (`idTrabajadores`)
    REFERENCES `mydb`.`Capturista` (`idCapturista`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Porfolio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Porfolio` (
  `idPorfolio` INT NOT NULL,
  `idTatuador` INT NULL,
  `Tatuador` VARCHAR(45) NULL,
  `Image` LONGBLOB NULL,
  PRIMARY KEY (`idPorfolio`),
  CONSTRAINT `fk_tatuador`
    FOREIGN KEY (`idTatuador`)
    REFERENCES `mydb`.`Tatuadores` (`idTatuador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Repartido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Repartido` (
  `idRepartidor` INT NOT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Telefono` INT NULL,
  `Direccion` VARCHAR(45) NULL,
  PRIMARY KEY (`idRepartidor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Stock`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Stock` (
  `idStock` INT NOT NULL,
  `Colores de Tinta` VARCHAR(45) NULL,
  `Agujas` VARCHAR(45) NULL,
  `Guantes` VARCHAR(45) NULL,
  `Cubrebocas` VARCHAR(45) NULL,
  `Playo` VARCHAR(45) NULL,
  `Servilletas` VARCHAR(45) NULL,
  `Jabon` VARCHAR(45) NULL,
  `Crema` VARCHAR(45) NULL,
  `Rastrillo` VARCHAR(45) NULL,
  `idTatuador` INT not NULL,
  `idRepartidor` INT not NULL,
  PRIMARY KEY (`idStock`),

    FOREIGN KEY (`idTatuador`)
    REFERENCES `mydb`.`Tatuadores` (`idTatuador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (`idRepartidor`)
    REFERENCES `Repartido` (`idRepartidor`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `mydb`.`Page`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Page` (
  `idPage` INT NOT NULL,
  `idTicket` INT NULL,
  `Tipo de pago` VARCHAR(45) NULL,
  PRIMARY KEY (`idPage`),
  CONSTRAINT `fk_ticket`
    FOREIGN KEY (`idTicket`)
    REFERENCES `mydb`.`Ticket` (`idTicket`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Citas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Citas` (
  `idCitas` INT NOT NULL,
  `idCliente` INT NULL,
  `idTatuador` INT NULL,
  `Nombre` VARCHAR(45) NULL,
  `Tatuador` VARCHAR(45) NULL,
  PRIMARY KEY (`idCitas`),
  CONSTRAINT `fk_cliente`
    FOREIGN KEY (`idCliente`)
    REFERENCES `mydb`.`Clientes` (`idClientes`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tatuador`
    FOREIGN KEY (`idTatuador`)
    REFERENCES `mydb`.`Tatuadores` (`idTatuador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

