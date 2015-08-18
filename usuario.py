__author__ = 'paladin'

class Usuario():
    ID_USUARIO = int
    NOMBRE = str
    ROL = ""
    DOCUMENTO = str
    CLAVE = str
    DIRECCION = str
    TELEFONO = str
    PREGUNTA = str
    RESPUESTA = str
    def __init__(self, name):
       Usuario.NOMBRE = name
"""
    def setear(self, clave=str, valor=str):

        if clave == "ID_USUARIO":
            ID_USUARIO = valor
        elif clave == "NOMBRE":
            NOMBRE = valor
        elif clave == "ROL":
            self.ROL = valor
        elif clave == "DOCUMENTO":
            self.DOCUMENTO = valor
        elif clave == "DIRECCION":
            self.DIRECCION = valor
        elif clave =="PREGUNTA":
            self.PREGUNTA = valor
        elif clave == "RESPUESTA":
            self.RESPUESTA = valor

        return

    def geter(self, clave = str):
        if clave == "ID_USUARIO":
            return  Usuario.ID_USUARIO
        elif clave == "NOMBRE":
            return Usuario.NOMBRE
        elif clave == "ROL":
            return self.ROL
        elif clave == "DOCUMENTO":
            return self.DOCUMENTO
        elif clave == "DIRECCION":
            return self.DIRECCION
        elif clave =="PREGUNTA":
            return self.PREGUNTA
        elif clave == "RESPUESTA":
            return self.RESPUESTA
"""