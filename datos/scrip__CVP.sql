SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `db_CVP` ;
CREATE SCHEMA IF NOT EXISTS `db_CVP` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `db_CVP` ;

-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_rol` (
  `id_rol` INT NOT NULL COMMENT 'este campo contiene la clave primaria de la tabla rol',
  `tipoRol` VARCHAR(30) NOT NULL COMMENT 'Este campo contiene los tipos de Roles disponibles.',
  `estado` TINYINT(1) NOT NULL COMMENT 'este campo contiene el estado del rol.',
  PRIMARY KEY (`id_rol`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_usuario` (
  `id_usuario` INT NOT NULL COMMENT 'este campo contiene la clave primaria de la tabla usuario.',
  `nombre` VARCHAR(45) NOT NULL COMMENT 'este es el campo nombre, donde se guardara dicho del usuario ',
  `apellido` VARCHAR(30) NOT NULL COMMENT 'este campo contiene el apellido del usuario.',
  `documento` VARCHAR(12) NOT NULL COMMENT 'en eeste campo  se guarda el documento del usuario.',
  `direccion` VARCHAR(45) NOT NULL COMMENT 'en este campo se guarda la direcion del cada uno de los usuarios.',
  `telefono` VARCHAR(20) NOT NULL COMMENT 'Este campo contiene el telefono del usuariio.',
  `clave` VARCHAR(45) NOT NULL,
  `pregunta` VARCHAR(100) NULL,
  `respuesta` VARCHAR(100) NULL,
  `tbl_rol_id_rol` INT NOT NULL COMMENT 'este campo contiene la clave de la tabla rol, la cual trae el rol de cada usuario, indicando cuales los permisos que puede tener dentro de la aplicasion.',
  PRIMARY KEY (`id_usuario`),
  INDEX `fk_tbl_usuario_tbl_rol_idx` (`tbl_rol_id_rol` ASC),
  CONSTRAINT `fk_tbl_usuario_tbl_rol`
    FOREIGN KEY (`tbl_rol_id_rol`)
    REFERENCES `db_CVP`.`tbl_rol` (`id_rol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tblL_parqueadero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tblL_parqueadero` (
  `id_Parqueadero` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `nit` VARCHAR(45) NULL,
  `Direccion` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `estado` TINYINT(1) NULL,
  PRIMARY KEY (`id_Parqueadero`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_tipo_vehiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_tipo_vehiculo` (
  `id_tipo_vehiculo` INT NOT NULL COMMENT 'este campo contiene la clave primaria de la tabla tarifa',
  `nombre` VARCHAR(45) NULL COMMENT 'este campo contiene el nombre del tipo de vehiculo',
  `estado` TINYINT(1) NULL COMMENT 'este campo contiene el estado de cada tipo de vehiculo.',
  `minuto` INT NULL COMMENT 'en este campo se indica el costo del minuto dependiendo la temporada',
  `día` INT NULL COMMENT 'Este campo contiene el precio de un dia en el parqueadero dependiendo en tipo de vehiculo. ',
  `hora` INT NULL COMMENT 'en este campo  indica el costo de la hora durante la semana ',
  `mes` INT NULL COMMENT 'Este campo contiene el precio del servicio mensual ',
  `tarifaFinSemana` INT NULL COMMENT 'Este campo contiene el precio durante el fin de semana.',
  `tarifaEspecial` INT NULL COMMENT 'En este campo se indica las tarifas ya que en ocaciones hay descuentos o prioridad en los precios.',
  `tblL_parqueadero_id_Parqueadero` INT NOT NULL,
  PRIMARY KEY (`id_tipo_vehiculo`),
  INDEX `fk_tbl_tipo_vehiculo_tblL_parqueadero1_idx` (`tblL_parqueadero_id_Parqueadero` ASC),
  CONSTRAINT `fk_tbl_tipo_vehiculo_tblL_parqueadero1`
    FOREIGN KEY (`tblL_parqueadero_id_Parqueadero`)
    REFERENCES `db_CVP`.`tblL_parqueadero` (`id_Parqueadero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_vehiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_vehiculo` (
  `id_vehiculo` INT NOT NULL COMMENT 'Este campo contiene la clave foranea de la tabla tipo de vehiculo.',
  `matricula` VARCHAR(45) NOT NULL COMMENT 'En este campo se guarda l amatricula delccarro.',
  `estado` TINYINT(1) NULL COMMENT 'este campo es el estado del vehiculo.',
  `tbl_tipo_vehiculo_id_tipo_vehiculo` INT NOT NULL COMMENT 'este campo contiene como clave forane la clave primaria de tipo de vehiculo con el cual se trae la informacion necesaria de dicha tabla.',
  PRIMARY KEY (`id_vehiculo`),
  INDEX `fk_tbl_vehiculo_tbl_tipo_vehiculo1_idx` (`tbl_tipo_vehiculo_id_tipo_vehiculo` ASC),
  CONSTRAINT `fk_tbl_vehiculo_tbl_tipo_vehiculo1`
    FOREIGN KEY (`tbl_tipo_vehiculo_id_tipo_vehiculo`)
    REFERENCES `db_CVP`.`tbl_tipo_vehiculo` (`id_tipo_vehiculo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_tipoVehiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_tipoVehiculo` (
  `id_tipoVehiculo` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `estado` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id_tipoVehiculo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_cliente` (
  `id_cliente` INT NOT NULL COMMENT 'este sera un campo ocasional en el que depende el tipo de servicio se registrara el campo del cliente.',
  `nombre` VARCHAR(45) NOT NULL COMMENT 'en este campo se adquire el nombre de ccasa cliente.',
  `apellido` VARCHAR(45) NOT NULL COMMENT 'n este campo contiene el apellido del cliente.',
  `documento` VARCHAR(12) NOT NULL COMMENT 'en este cmapo se guardara el numero de documento de cada cliente.',
  `telefono` VARCHAR(20) NOT NULL COMMENT 'en este campo se contiene el telefono del cliente.\n',
  PRIMARY KEY (`id_cliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_servicio` (
  `id_servicio` INT NOT NULL COMMENT 'este campo contiene la calve primaria de la tabla servicio.',
  `fechaInicio` TIMESTAMP NOT NULL COMMENT 'este campo contiene la fecha de inicio del servicio, lo cual permire calcular el tiempo transcurrido.',
  `fechaFinal` TIMESTAMP NULL COMMENT 'este campo conriene la fecha en la que finalisa el servicio. ',
  `tipo` VARCHAR(45) NULL,
  `tbl_vehiculo_id_vehiculo` INT NOT NULL COMMENT 'este campo contiene la clave foranea de la tabal vehiculo.',
  `tbl_cliente_id_cliente` INT NOT NULL COMMENT 'este campo trae la clave foranea del cliente, lo que permite indicar el dieño de dicho vehiculo.',
  PRIMARY KEY (`id_servicio`),
  INDEX `fk_servicio_tbl_vehiculo1_idx` (`tbl_vehiculo_id_vehiculo` ASC),
  INDEX `fk_tbl_servicio_tbl_cliente1_idx` (`tbl_cliente_id_cliente` ASC),
  CONSTRAINT `fk_servicio_tbl_vehiculo1`
    FOREIGN KEY (`tbl_vehiculo_id_vehiculo`)
    REFERENCES `db_CVP`.`tbl_vehiculo` (`id_vehiculo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_servicio_tbl_cliente1`
    FOREIGN KEY (`tbl_cliente_id_cliente`)
    REFERENCES `db_CVP`.`tbl_cliente` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_celda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_celda` (
  `id_celda` INT NOT NULL COMMENT 'este campo contiene la clave primaria de la tabla (celda)	',
  `numero` INT NOT NULL DEFAULT 0 COMMENT 'este campo indica la camidad de celdas disponibles',
  `estado` TINYINT(1) NOT NULL DEFAULT 1 COMMENT 'en este campo se indica el estado de cada celda (ocupada o llibre)',
  `tbl_tipo_vehiculo_id_tipo_vehiculo` INT NOT NULL,
  PRIMARY KEY (`id_celda`),
  INDEX `fk_tbl_celda_tbl_tipo_vehiculo1_idx` (`tbl_tipo_vehiculo_id_tipo_vehiculo` ASC),
  CONSTRAINT `fk_tbl_celda_tbl_tipo_vehiculo1`
    FOREIGN KEY (`tbl_tipo_vehiculo_id_tipo_vehiculo`)
    REFERENCES `db_CVP`.`tbl_tipo_vehiculo` (`id_tipo_vehiculo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_regimen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_regimen` (
  `id_regimen` INT NOT NULL COMMENT 'este campo contiene la clave primaria de la tabla tegimen.',
  `fechaInicio` TIMESTAMP NOT NULL COMMENT 'Este campo contiene la fecha de inicio de dicho regimen.			',
  `fechaFinal` TIMESTAMP NOT NULL COMMENT 'este campo contiene  la fecha final del regimen.',
  `numeroInicio` INT NOT NULL COMMENT 'este campo contiene el numero inicial del regimen.',
  `numeroFinal` INT NOT NULL COMMENT 'Este campo contiene el numero final del regimen.',
  PRIMARY KEY (`id_regimen`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_factura` (
  `id_factura` INT NOT NULL COMMENT 'Este campo contiene la clave primaria de la tabla factura.',
  `subtotal` DOUBLE NOT NULL,
  `iva` DOUBLE NOT NULL,
  `descuento` DOUBLE NULL,
  `total` INT NOT NULL COMMENT 'en este campo se calculara el total de los servicios.',
  `tbl_regimen_id_regimen` INT NOT NULL,
  `tbl_usuario_id_usuario` INT NOT NULL COMMENT 'este campo trae el id de la tabla usuario, por medio de cual se permite traer toda la informacion del usuario.',
  `tbl_servicio_id_servicio` INT NOT NULL COMMENT 'este campo contiene la clave foranea de la tabla servicio, por medios de la cual se tra la informacion del srvicio.',
  PRIMARY KEY (`id_factura`),
  INDEX `fk_tbl_factura_tbl_servicio1_idx` (`tbl_servicio_id_servicio` ASC),
  INDEX `fk_tbl_factura_tbl_usuario1_idx` (`tbl_usuario_id_usuario` ASC),
  INDEX `fk_tbl_factura_tbl_regimen1_idx` (`tbl_regimen_id_regimen` ASC),
  CONSTRAINT `fk_tbl_factura_tbl_servicio1`
    FOREIGN KEY (`tbl_servicio_id_servicio`)
    REFERENCES `db_CVP`.`tbl_servicio` (`id_servicio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_factura_tbl_usuario1`
    FOREIGN KEY (`tbl_usuario_id_usuario`)
    REFERENCES `db_CVP`.`tbl_usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_factura_tbl_regimen1`
    FOREIGN KEY (`tbl_regimen_id_regimen`)
    REFERENCES `db_CVP`.`tbl_regimen` (`id_regimen`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = '			';


-- -----------------------------------------------------
-- Table `db_CVP`.`dfadsfa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`dfadsfa` (
  `id_Adasda` INT NOT NULL,
  PRIMARY KEY (`id_Adasda`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`table1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`table1` (
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_acceso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_acceso` (
  `id_acceso` INT NOT NULL,
  `controlador` VARCHAR(45) NULL,
  `estado` TINYINT(1) NULL,
  `tbl_rol_id_rol` INT NOT NULL,
  PRIMARY KEY (`id_acceso`),
  INDEX `fk_tbl_acceso_tbl_rol1_idx` (`tbl_rol_id_rol` ASC),
  CONSTRAINT `fk_tbl_acceso_tbl_rol1`
    FOREIGN KEY (`tbl_rol_id_rol`)
    REFERENCES `db_CVP`.`tbl_rol` (`id_rol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_CVP`.`tbl_turno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_CVP`.`tbl_turno` (
  `id_turno` INT NOT NULL AUTO_INCREMENT,
  `horaInicio` TIMESTAMP NOT NULL,
  `horaFin` TIMESTAMP NULL,
  `base` INT NULL,
  `recaudo` VARCHAR(45) NULL,
  `tbl_usuario_id_usuario` INT NOT NULL,
  PRIMARY KEY (`id_turno`),
  INDEX `fk_tbl_turno_tbl_usuario1_idx` (`tbl_usuario_id_usuario` ASC),
  CONSTRAINT `fk_tbl_turno_tbl_usuario1`
    FOREIGN KEY (`tbl_usuario_id_usuario`)
    REFERENCES `db_CVP`.`tbl_usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
