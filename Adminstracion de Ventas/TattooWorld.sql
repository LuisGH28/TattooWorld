Create database TattooWorld;

use TattooWorld;

-- -----------------------------------------------------
-- Table `TattooWorld`.`Area`
-- -----------------------------------------------------
CREATE TABLE Area(
  `idArea` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(45)
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Repartidor`
-- -----------------------------------------------------
CREATE TABLE Repartidor(
  `idRepartidor` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(45) ,
  `Apellido` VARCHAR(80),
  `Celular` INT NOT NULL,
  `Ubicacion` VARCHAR(80)
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Style_Tattoo`
-- -----------------------------------------------------
CREATE TABLE Style_Tattoo(
  `idStyle` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(45),
  `Descripcion` VARCHAR(45)
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE Clientes(
  `idCliente` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(45),
  `Edad` INT NOT NULL,
  `Celular` INT NOT NULL
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Tatuadores`
-- -----------------------------------------------------
CREATE TABLE Tatuadores(
  `idTatuadores` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(45),
  `Apellido_M` VARCHAR(45),
  `Apellido_P` VARCHAR(45),
  `idStyle` INT,
  `idArea` INT,
    CONSTRAINT fk_style FOREIGN KEY (idStyle) REFERENCES Style_Tattoo(idStyle)
    ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_area FOREIGN KEY (idArea) REFERENCES Area(idArea)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Stock`
-- -----------------------------------------------------
CREATE TABLE Stock(
  `idStock` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(45),
  `Cantidad` INT NOT NULL,
  `idTatuadores` INT,
    CONSTRAINT fk_tatuador FOREIGN KEY (idTatuadores) REFERENCES Tatuadores (idTatuadores)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Portafolio`
-- -----------------------------------------------------
CREATE TABLE Portafolio(
  `idPortafolio` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Tatuador` VARCHAR(45),
  `Imagen` LONGBLOB NOT NULL,
  `idTatuador` INT,
    CONSTRAINT fk_tatuadores FOREIGN KEY (idTatuador) REFERENCES Tatuadores(idTatuadores)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Recepcionista`
-- -----------------------------------------------------
CREATE TABLE Recepcionista(
  `idRecepcionista` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Nombre` VARCHAR(45),
  `Apellido_M` VARCHAR(45),
  `Apellido_P` VARCHAR(45),
  `Celular` INT NOT NULL,
  `idArea` INT,
    CONSTRAINT fk_areas FOREIGN KEY (idArea) REFERENCES Area(idArea)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Citas`
-- -----------------------------------------------------
CREATE TABLE Citas (
  `idCitas` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `Recepcionista` VARCHAR(45) ,
  `Tatuador` VARCHAR(45),
  `Cliente` VARCHAR(45),
  `idCliente` INT,
  `idTatuador` INT,
  `idRecepcionista` INT,
  CONSTRAINT fk_reps FOREIGN KEY (idRecepcionista) REFERENCES Recepcionista(idRecepcionista)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT  fk_tatuadors FOREIGN KEY (idTatuador) REFERENCES Tatuadores(idTatuadores)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_clientes FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table `TattooWorld`.`Login`
-- -----------------------------------------------------
CREATE TABLE Login(
  `idLogin` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `User` VARCHAR(45),
  `Password` VARCHAR(45),
  `idTatuador` INT,
  `idRecepcionista` INT,
  CONSTRAINT fk_tatuadore FOREIGN KEY (idTatuador) REFERENCES Tatuadores(idTatuadores)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_repce FOREIGN KEY (idRecepcionista) REFERENCES Recepcionista(idRecepcionista)
    ON DELETE CASCADE ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table `TattooWorld`.`Login_Tables`
-- -----------------------------------------------------
CREATE TABLE Login_Tables(
  `idLogin` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `User` VARCHAR(45),
  `Password` VARCHAR(45),
  `idTatuador` INT,
  `idRecepcionista` INT,
  CONSTRAINT fk_tatuado FOREIGN KEY (idTatuador) REFERENCES Tatuadores(idTatuadores)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_repcep FOREIGN KEY (idRecepcionista) REFERENCES Recepcionista(idRecepcionista)
    ON DELETE CASCADE ON UPDATE CASCADE
);














