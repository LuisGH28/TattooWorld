-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema FashionTec
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema FashionTec
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `FashionTec` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;
USE `FashionTec` ;

-- -----------------------------------------------------
-- Table `FashionTec`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FashionTec`.`clientes` (
  `idCliente` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCliente` VARCHAR(45) NULL DEFAULT NULL,
  `apellidoPaterno` VARCHAR(45) NULL DEFAULT NULL,
  `apellidoMaterno` VARCHAR(45) NULL DEFAULT NULL,
  `Telefono` VARCHAR(25) NULL DEFAULT NULL,
  `RFC` VARCHAR(25) NULL DEFAULT NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `FashionTec`.`contraseña`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FashionTec`.`contraseña` (
  `idPassword` INT(11) NOT NULL AUTO_INCREMENT,
  `empleado` VARCHAR(45) NULL DEFAULT NULL,
  `contraseña` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idPassword`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `FashionTec`.`empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FashionTec`.`empleado` (
  `idEmpleado` INT(11) NOT NULL,
  `nombreEmpleado` VARCHAR(45) NULL DEFAULT NULL,
  `apellidoPaterno` VARCHAR(45) NULL DEFAULT NULL,
  `apellidoMaterno` VARCHAR(45) NULL DEFAULT NULL,
  `genero` VARCHAR(25) NULL DEFAULT NULL,
  `Telefono` VARCHAR(25) NULL DEFAULT NULL,
  `idPassword` INT(11) NOT NULL,
  PRIMARY KEY (`idEmpleado`),
  INDEX `idPassword` (`idPassword` ASC) VISIBLE,
  CONSTRAINT `empleado_ibfk_1`
    FOREIGN KEY (`idPassword`)
    REFERENCES `FashionTec`.`contraseña` (`idPassword`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `FashionTec`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FashionTec`.`productos` (
  `idProductos` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProdcuto` VARCHAR(45) NULL DEFAULT NULL,
  `Categoria` VARCHAR(45) NULL DEFAULT NULL,
  `Proveedores` VARCHAR(45) NULL DEFAULT NULL,
  `Precio` DOUBLE NULL DEFAULT NULL,
  `Unidades` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idProductos`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `FashionTec`.`ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FashionTec`.`ventas` (
  `idVenta` INT(11) NOT NULL AUTO_INCREMENT,
  `idProductos` INT(11) NOT NULL,
  `idFactura` INT(11) NOT NULL,
  `precio` DOUBLE NULL DEFAULT NULL,
  `cantidadProducto` INT(11) NOT NULL,
  `subtotal` DOUBLE NULL DEFAULT NULL,
  PRIMARY KEY (`idVenta`),
  INDEX `idProductos` (`idProductos` ASC) VISIBLE,
  INDEX `idFactura` (`idFactura` ASC) VISIBLE,
  CONSTRAINT `ventas_ibfk_1`
    FOREIGN KEY (`idProductos`)
    REFERENCES `FashionTec`.`productos` (`idProductos`),
  CONSTRAINT `ventas_ibfk_2`
    FOREIGN KEY (`idFactura`)
    REFERENCES `FashionTec`.`factura` (`idFactura`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `FashionTec`.`factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `FashionTec`.`factura` (
  `idFactura` INT(11) NOT NULL AUTO_INCREMENT,
  `Fecha` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
  `Hora` TIME NULL DEFAULT NULL,
  `Total` DOUBLE NULL DEFAULT NULL,
  `idCliente` INT(11) NOT NULL,
  `idEmpleado` INT NOT NULL,
  `idVenta` INT(11) NOT NULL,
  PRIMARY KEY (`idFactura`),
  INDEX `idCliente` (`idCliente` ASC) VISIBLE,
  INDEX `idEmpleado` (`idEmpleado` ASC) VISIBLE,
  INDEX `idVenta` () VISIBLE,
  CONSTRAINT `factura_ibfk_1`
    FOREIGN KEY (`idCliente`)
    REFERENCES `FashionTec`.`clientes` (`idCliente`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_idEmpleado`
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `FashionTec`.`empleado` (`idEmpleado`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `kf_idVenta`
    FOREIGN KEY ()
    REFERENCES `FashionTec`.`ventas` ()
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
