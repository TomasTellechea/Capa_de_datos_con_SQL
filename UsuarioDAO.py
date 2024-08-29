from Conexion import Conexion
from Cursor_del_pool import Cursor_del_pool
from Usuario import Usuario
from logger_base import log

"""DAO es un patron de diseño, significa DATA ACCESS OBJECT
CRUD: Create, Read, Update, Delete, que son las acciones hacia una base da datos"""


class UsuarioDAO:
    _SELECCIONAR = "SELECT * FROM usuarios ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE usuarios SET username =%s, password = %s WHERE id_usuario = %s"
    _ELIMINAR = "DELETE FROM usuarios WHERE id_usuario = %s"

    # SELECT
    @classmethod
    def seleccionar(cls):
        with Cursor_del_pool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            log.debug(f'Número de registros obtenidos: {len(registros)}')
            lista_de_usuarios = []
            for registro in registros:
                user = Usuario(registro[0], registro[1],
                               registro[2])  # n de registros en lista = n columnas en db
                # guardamos en la lista el cliente descargado
                lista_de_usuarios.append(user)
            # cursor.close()  # cerramos el cursor
            return lista_de_usuarios  # devolvemos la lista de clientes

    # INSERT
    @classmethod
    def insertar(cls, user):
        with Cursor_del_pool() as cursor:
            valores = (user.username, user.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona insertada: {user}")
            return cursor.rowcount

    # UPDATE
    @classmethod
    def actualizar(cls, user):
        with Cursor_del_pool() as cursor:
            valores = (user.username, user.password, user.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona actualizada: {user}")
            return cursor.rowcount

    # DELETE
    @classmethod
    def eliminar(cls, user):
        with Cursor_del_pool() as cursor:
            valores = (user.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Persona eliminada: {user}")
            return cursor.rowcount


# pruebas
if __name__ == "__main__":

    # # metodo seleccionar
    # db_users = UsuarioDAO.seleccionar()
    # for u in db_users:
    #     log.debug(u)

    # metodo insert
    #    # Crear una instancia de Usuario
    #     nuevo_usuario = Usuario(username="KKclust", password="34523")

    #     # Insertar el nuevo usuario en la base de datos
    #     usuario_insertado = UsuarioDAO.insertar(nuevo_usuario)

    # actualizar:

    # nueva_data = Usuario(id_usuario=1, username="justo", password="whit")
    # # Actualizar el usuario en la base de datos
    # user_act = UsuarioDAO.actualizar(nueva_data)

    # eliminar:
    user_a_eliminar = Usuario(id_usuario=4)
    user_eliminado = UsuarioDAO.eliminar(user_a_eliminar)
