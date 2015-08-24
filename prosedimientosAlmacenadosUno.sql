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
CREATE PROCEDURE `listarUnaRespuesta`(in id_usr int)
BEGIN
	Select respuesta FROM tbl_usuario WHERE id_usuario = id_usr; 
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
CREATE PROCEDURE `modificarClave` (IN id_usr INT, IN new_pass VARCHAR(20))
BEGIN
	UPDATE tbl_usuario SET clave = new_pass WHERE id_usuario = id_usr;
END
$$

DELIMITER ;

-- -------------------------------------- --
--  sp7: Modificar Pregunta               --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `modificarPregunta` (IN id_usr INT, in pre VARCHAR(100), in res VARCHAR(100) )
BEGIN
	UPDATE tbl_usuario SET pregunta = pre, respuesta = res WHERE id_usuario = id_usr;
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



-- -------------------------------------- --
--  sp15: Crear Cliente                   --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `crearCliente` (IN nombreCl VARCHAR(45), IN apellidoCl VARCHAR(45), IN documentoCl VARCHAR(20), IN telefonoCl VARCHAR(12))
BEGIN
	insert into tbl_cliente(nombre, apellido, documento, telefono, estado_cliente) values(nombreCl,apellidoCl,documentoCl,telefonoCl,1);
END$$
DELIMITER ;


-- ------------------------------------------------ --
--  sp16: Numero De Celdas Por Tipo de Vehiculo     --
-- ------------------------------------------------ --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `celdasOcupadasPorTipoDeVehiculo` (IN id_tVehiculo INT)
BEGIN
	SELECT COUNT(*) FROM tbl_celda WHERE tbl_tipo_vehiculo_id_tipo_vehiculo = id_tVehiculo AND estado != 1;
END$$

DELIMITER ;

-- -------------------------------------------- --
--  sp17: modificar Tipo de Vehiculo            --
-- -------------------------------------------- --

DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `modificarTipoDeVehiculo` (IN id_TVehiculo INT, IN fraccionVhl INT, IN horaVhl INT, IN diaVhl INT, IN mesVhl INT,IN especialVhl INT, IN numCeldas INT,IN estadoVhl INT)
BEGIN
	DECLARE interadorUno INT;
	DECLARE interadorDos INT;
	DECLARE celdasActuales INT;
	DECLARE menosCeldas INT;
	DECLARE numeroC INT;
	SET interadorUno = 1;
	SET interadorDos = 1;	
	
	SELECT count(*) INTO celdasActuales FROM tbl_celda WHERE tbl_tipo_vehiculo_id_tipo_vehiculo = id_TVehiculo;
	
	IF celdasActuales < numCeldas THEN
		SET menosCeldas = numCeldas - celdasActuales;		
		WHILE menosCeldas>=interadorUno DO
			SET numeroC = celdasActuales + interadorUno;
			INSERT INTO tbl_celda(numero, estado, tbl_tipo_vehiculo_id_tipo_vehiculo) VALUES(numeroC, 1,id_TVehiculo);
			SET interadorUno = interadorUno + 1;
		END WHILE;
	END IF;

	IF celdasActuales > numCeldas THEN
		SET menosCeldas = celdasActuales - numCeldas;		
		WHILE menosCeldas >= interadorDos DO			
			DELETE FROM tbl_celda WHERE tbl_tipo_vehiculo_id_tipo_vehiculo = id_TVehiculo AND numero > numCeldas;
			SET interadorDos = interadorDos + 1;
		END WHILE;
	END IF;

	UPDATE tbl_tipo_vehiculo set minuto = fraccionVhl, hora = horaVhl, día = diaVhl, mes = mesVhl, tarifaEspecial = especialVhl, estado = estadoVhl
	WHERE id_tipo_vehiculo = id_TVehiculo;
END$$

DELIMITER ;



-- -------------------------------------- --
--  sp18: Listar Un Cliente               --
-- -------------------------------------- --

DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarUnCliente`(IN documentoCl VARCHAR(30))
BEGIN
	SELECT * FROM tbl_cliente WHERE documento = documentoCl;
END$$

DELIMITER ;


-- -------------------------------------- --
--  sp19: Modificar Un Cliente            --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `modificarCliente` (IN documentoclUno VARCHAR(20), IN nombreCl VARCHAR(45), IN apellidoCl VARCHAR(45), IN documentoCl VARCHAR(20), IN telefonoCl VARCHAR(12), IN estadoCl INT)
BEGIN
	UPDATE tbl_cliente
	SET nombre = nombreCl, apellido = apellidoCl, documento = documentoCl, telefono = telefonoCl, estado_cliente = estadoCl
	WHERE documento = documentoClUno;
END$$

DELIMITER ;



-- -------------------------------------- --
--  sp20: listar operarios                --
-- -------------------------------------- --
DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarOperarios` ()
BEGIN
	SELECT * FROM tbl_usuario WHERE tbl_rol_id_rol = 2;
END$$

DELIMITER ;



-- ------------------------------------------ --
--  sp21: listar usuario por documento        --
-- ------------------------------------------ --

DELIMITER $$
USE `db_CVP`$$
CREATE PROCEDURE `listarUsuarioPorDocumento`(in doc_usr int)
BEGIN
	SELECT * FROM tbl_usuario 
	where documento = doc_usr;
END
$$

DELIMITER ;

-- --------------------------------------------- --
--  sp22: Modofocar usuario por documento        --
-- --------------------------------------------- --


DELIMITER $$
USE `db_CVP`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `modificarUsuarioCompleto`(in id_actUsr VARCHAR(20),in nombreUsr VARCHAR(25),in apellidoUsr VARCHAR(25), in documentoUsr VARCHAR(25),in telefonoUsr VARCHAR(25), in direccionUsr VARCHAR(25), in claveUsr VARCHAR(25),IN preguntaUsr VARCHAR(200),in respuestaUsr VARCHAR(25),in estadoUsr INT)
BEGIN
	UPDATE tbl_usuario 
	SET nombre=nombreUsr, apellido=apellidoUsr, telefono=telefonoUsr, direccion=direccionUsr, estado_usuario = estadoUsr, documento = documentoUsr, clave = claveUsr, pregunta=preguntaUsr, respuesta = respuestaUsr
	WHERE documento = id_actUsr;
END$$

DELIMITER ;



