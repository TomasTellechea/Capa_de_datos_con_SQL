
from logger_base import log


class Usuario:

    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'''
        Id_usuario: {self.id_usuario}, 
        Username: {self._username},
        Password: {self._password}'''

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_cliente = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

# Pruebas de la clase persona:


if __name__ == "__main__":

    usuario_3 = Usuario(1, "EduEdu", "2345")
    log.debug(usuario_3)
