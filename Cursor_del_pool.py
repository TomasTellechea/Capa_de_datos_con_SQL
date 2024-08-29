from logger_base import log
from Conexion import Conexion
import traceback


class Cursor_del_pool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Inicio del método __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción: {valor_excepcion}')
            log.error('Detalle de la excepción:')
            log.error(traceback.format_exc())
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')

        # Aseguramos que el cursor se cierre incluso si ocurre un error
        try:
            if self._cursor:
                self._cursor.close()
                log.debug('Cursor cerrado')
        except Exception as e:
            log.error(f'Error al cerrar el cursor: {e}')

        # Liberar la conexión
        Conexion.liberar_conexion(self._conexion)
        log.debug('Conexión liberada al pool')


if __name__ == "__main__":
    with Cursor_del_pool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM usuarios')
        log.debug(cursor.fetchall())
