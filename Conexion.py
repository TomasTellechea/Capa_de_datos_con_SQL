import sys
from logger_base import log
import mysql.connector
from mysql.connector import pooling


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'root'
    _PASSWORD = 'root'
    _HOST = 'localhost'
    _PORT = '3306'
    _MIN_CONEXIONES = 1
    _MAX_CONEXIONES = 5
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name="mypool",
                    pool_size=cls._MAX_CONEXIONES,
                    host=cls._HOST,
                    database=cls._DATABASE,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=int(cls._PORT)
                )
                log.debug(f'Creación del pool exitosa: {cls._pool}')
            except Exception as e:
                log.error(f"Ocurrió un error al crear el pool: {e}")
                raise  # Lanzar la excepción para manejarla fuera del método
        return cls._pool

    @classmethod
    def obtener_conexion(cls):
        try:
            conexion = cls.obtener_pool().get_connection()
            log.debug(f"Conexión obtenida del pool: {conexion}")
            return conexion
        except Exception as e:
            log.error(f"Ocurrió un error al obtener la conexión: {e}")
            return None

    @classmethod
    def liberar_conexion(cls, conexion):
        try:
            if conexion and conexion.is_connected():
                conexion.close()
                log.debug(f"Conexión liberada al pool: {conexion}")
        except Exception as e:
            log.error(f"Ocurrió un error al liberar la conexión: {e}")

    @classmethod
    def cerrar_pool(cls):
        if cls._pool is not None:
            try:
                cls._pool.close()
                log.debug("Pool cerrado")
            except Exception as e:
                log.error(f"Ocurrió un error al cerrar el pool: {e}")


if __name__ == "__main__":
    # Prueba de la clase Conexion
    conexion_1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion_1)
    conexion_2 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion_2)
