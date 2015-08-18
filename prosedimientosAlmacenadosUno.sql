-- ------------------------------------------------------------- --
-- ------------------------------------------------------------- --
--                                                               --
--                  PROCEDIMIENTOS ALMACENADOS                   --
--                                                               --
-- Info: lista de procedimientos almacenados del proyecto CVP    --
--                                                               --
-- ------------------------------------------------------------- --
-- ------------------------------------------------------------- --

-- -------------------------------------- --
--  sp1: Consultar Un Usuario             --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarUnUsuario` (in id_usr int)
BEGIN
	SELECT * FROM tbl_usuario AS USR 
	INNER JOIN tbl_rol AS ROL ON ROL.id_rol=USR.tbl_rol_id_rol
	where id_usuario = id_usr;
END
$$

DELIMITER ;
-- -------------------------------------- --
--  sp2: Validar Unico Documento          --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `validarUnicoDocumento` (in doc int)
BEGIN
	SELECT documento FROM tbl_usuario WHERE documento = doc;
END
$$

DELIMITER ;
-- -------------------------------------- --
--  sp3: listar una pregunta              --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarUnaPregunta` (in id_usr int)
BEGIN
	Select pregunta FROM tbl_usuario WHERE documento = id_usr; 
END
$$

DELIMITER ;
-- -------------------------------------- --
--  sp4: listar una Respuesta             --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarUnaRespuesta` (in id_usr int)
BEGIN
	Select respuesta FROM tbl_usuario WHERE documento = id_usr; 
END
$$

-- -------------------------------------- --
--  sp5: Modificar Un Usuario             --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `modificarUsuario` (in nombreUsr VARCHAR(25),in apellidoUsr VARCHAR(25),in telefonoUsr VARCHAR(25),in direccionUsr VARCHAR(25),in id_usr int)
BEGIN
	UPDATE tbl_usuario 
	SET nombre=nombreUsr, apellido=apellidoUsr, telefono=telefonoUsr, direccion=direccionUsr
	WHERE id_usuario = id_usr;
END
$$

DELIMITER ;
-- -------------------------------------- --
--  sp6: Modificar clave                  --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `modificarClave` (in new_pass INT)
BEGIN
	UPDATE tbl_usuario SET clave = new_pass;
END
$$

DELIMITER ;

-- -------------------------------------- --
--  sp7: Modificar Pregunta               --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `modificarPregunta` (in pre VARCHAR(100),in res VARCHAR(100) )
BEGIN
	UPDATE tbl_usuario SET pregunta = pre, respuesta = res ;
END
$$

DELIMITER ;

-- -------------------------------------- --
--  sp: Modificar Parqueadero             --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `modificarParqueadero` (in nombrePar VARCHAR(25),in nitPar VARCHAR(25),in telefonoPar VARCHAR(25),in direccionPar VARCHAR(25))
BEGIN
	UPDATE tbl_parqueadero SET nombre = nombrePar, nit = nitPar, telefono = telefonoPar, direccion = direccionPar
	WHERE id_parqueadero = 1;
END
$$

DELIMITER ;

-- -------------------------------------- --
--  sp8: Listar Parqueadero               --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarElParquedero` ()
BEGIN
	SELECT * FROM tbl_parqueadero WHERE id_parqueadero = 1; 
END$$

DELIMITER ;

-- -------------------------------------- --
--  sp9: Listar Todos los Vehiculos       --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarVehiculos`()
BEGIN
	SELECT * FROM tbl_tipo_vehiculo;
END$$

DELIMITER ;

-- ------------------------------------------------ --
--  sp10: Listar un Tipo de Vehiculo por Nombre     --
-- ------------------------------------------------ --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarUntipoVehiculoPorNombre` (in nombreVeh VARCHAR(25))
BEGIN
	SELECT * FROM tbl_tipo_vehiculo WHERE nombre = LOWER(nombreVeh);
END$$

DELIMITER ;

-- -------------------------------------------- --
--  sp11: Numero de Celdas Por Vehiculo         --
-- -------------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `celdasPorVehiculo` (IN tipoVehiculo VARCHAR(45))
BEGIN
	DECLARE idVehiculo INT;
	SELECT id_tipo_vehiculo 
	INTO idVehiculo
	FROM tbl_tipo_vehiculo 
	WHERE nombre = tipoVehiculo;

	SELECT COUNT(numero) AS 'celsdas' 
	FROM tbl_celda 
	WHERE tbl_tipo_vehiculo_id_tipo_vehiculo = idVehiculo;
END$$

DELIMITER ;

-- -------------------------------------- --
--  sp12: Crear Tipo de Vehiculo          --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `crearTipoDeVehiculo` (IN nombreVhl VARCHAR(25), IN fraccionVhl INT, IN horaVhl INT, IN diaVhl INT, IN mesVhl INT,IN especialVhl INT)
BEGIN
	INSERT INTO tbl_tipo_vehiculo(nombre, minuto, hora, mes, tarifaEspecial, estado, tblL_parqueadero_id_Parqueadero)
	VALUES(nombreVhl, fraccionVhl, horaVhl, diaVhl, mesVhl, especialVhl, 1,1);
END$$

DELIMITER ;

-- -------------------------------------- --
--  sp13: Insertar Tipo de Vehiculo       --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `insertarTipoDeVehiculo` (IN nombreVhl VARCHAR(25), IN fraccionVhl INT, IN horaVhl INT, IN diaVhl INT, IN mesVhl INT,IN especialVhl INT, IN numCeldas INT)
BEGIN
	DECLARE interador INT;
	DECLARE idVehiculo INT;
	SET interador = 1;
	INSERT INTO tbl_tipo_vehiculo(nombre, minuto, hora, día, mes, tarifaEspecial, estado, tblL_parqueadero_id_Parqueadero)
	VALUES(lower(nombreVhl), fraccionVhl, horaVhl, diaVhl, mesVhl, especialVhl, 1,1);
	-- SELECT @@identity INTO idVehiculo FROM tbl_tipo_vehiculo;
	SELECT last_insert_id() INTO idVehiculo;
	WHILE numCeldas>=interador DO
		INSERT INTO tbl_celda(numero, estado, tbl_tipo_vehiculo_id_tipo_vehiculo) VALUES(interador, 1,idVehiculo);
		SET interador = interador + 1;
	END WHILE;
END$$
DELIMITER ;
	


-- -------------------------------------- --
--  sp14: Validar Tipo de Vehiculo        --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `validarTipoDeVehiculo`(IN nombreVhl VARCHAR(25))
BEGIN
	SELECT nombre FROM db_CVP.tbl_tipo_vehiculo WHERE nombre = lower(nombreVhl);
END$$

DELIMITER ;


