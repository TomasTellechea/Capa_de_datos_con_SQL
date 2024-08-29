import logging as log


log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s | %(levelname)s | [%(filename)s:%(lineno)s] | %(message)s',
    datefmt='%I:%m:%S %p',
    handlers=[
        log.FileHandler(
            'C:\\Users\\tomas\\Desktop\\PROGRAMACION\\python\\Curso_Udemy_Universidad_Python\\22_Laboratorio_final_Capa_de_datos_usuarios\\capa_de_datos.log'),
        # También enviamos los mensajes de log a la consola (flujo estándar de salida).
        log.StreamHandler()
    ]
)


if __name__ == "__main__":
    log.debug("Este es el nivel DEBUG")
    log.info("Este es el nivel INFO")
    log.warning("Este es el nivel WARNING")
    log.error("Este es el nivel ERROR")
    log.critical("Este es el nivel CRITICAL")
