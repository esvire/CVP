-- ----------------------------------------------------------------
-- PROCEDIMIENTOS ALMACENADOS                                    --
--                                                               --
-- Info: lista de procedimientos almacenados del proyecto CVP    --
-- ----------------------------------------------------------------

-- -------------------------------------- --
--  sp: Consultar Un Usuario              --
-- -------------------------------------- --
CREATE PROCEDURE `listarUnUsuario` (in id_usr int)
BEGIN
	SELECT * FROM tbl_usuario AS USR 
	INNER JOIN tbl_rol AS ROL ON ROL.id_rol=USR.tbl_rol_id_rol;
	where id_usuario = id_usr;
END

-- -------------------------------------- --
--  sp: Validar Unico Documento           --
-- -------------------------------------- --
CREATE PROCEDURE `validarUnicoDocumento` (in doc int)
BEGIN
	SELECT documento FROM tbl_usuario WHERE documento = doc;
END

-- -------------------------------------- --
--  sp: listar una pregunta                --
-- -------------------------------------- --
CREATE PROCEDURE `listarUnaPregunta` (in id_usr int)
BEGIN
	Select pregunta FROM tbl_usuario WHERE documento = id_usr; 
END

-- -------------------------------------- --
--  sp: listar una Respuesta              --
-- -------------------------------------- --
CREATE PROCEDURE `listarUnaRespuestas` (in doc VARCHAR(100))
BEGIN
	Select respuesta,clave FROM tbl_usuario WHERE documento = doc; 
END

-- -------------------------------------- --
--  sp: Modificar Un Usuario              --
-- -------------------------------------- --
CREATE PROCEDURE `modificarUsuario` (in nombreUsr VARCHAR(25),in apellidoUsr VARCHAR(25),in telefonoUsr VARCHAR(25),in direccionUsr VARCHAR(25),in id_usr int)
BEGIN
	UPDATE tbl_usuario 
	SET nombre=nombreUsr, apellido=apellidoUsr, telefono=telefonoUsr, direccion=direccionUsr
	WHERE id_usuario = id_usr;
END

-- -------------------------------------- --
--  sp: Modificar clave                   --
-- -------------------------------------- --
CREATE PROCEDURE `modificarClave` (in new_pass INT)
BEGIN
	UPDATE tbl_usuario SET clave = new_pass;
END

-- -------------------------------------- --
--  sp: Modificar Pregunta                --
-- -------------------------------------- --
CREATE PROCEDURE `modificarPregunta` (in pre VARCHAR(100),in res VARCHAR(100) )
BEGIN
	UPDATE tbl_usuario SET pregunta = pre, respuesta = res ;
END
