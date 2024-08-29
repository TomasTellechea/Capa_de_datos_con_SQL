from logger_base import log
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

opcion = None

while opcion != 5:
    try:
        print("Opciones:")
        print("1. Listar Usuarios")
        print("2. Agregar Usuario")
        print("3. Modificar Usuario")
        print("4. Eliminar Usuario")
        print("5. Salir")
        opcion = int(input("Elige tu opcion (1-5): "))

        if opcion == 1:
            db_users = UsuarioDAO.seleccionar()
            for u in db_users:
                print(u)
                # log.info(u) 
                # con log mandamos la informacion a la vitácora logger base
        elif opcion == 2:
            username = input("ingrese el nombre de usuario: ")
            password = input("ingrese la contraseña: ")
            nuevo_usuario = Usuario(username=username, password=password)
            usuario_insertado = UsuarioDAO.insertar(nuevo_usuario)
            print(f'Usuario insertado: {usuario_insertado}')
        elif opcion == 3:
            id_usuario = input(
                "ingrese el id del usuario que quiere modificar: ")
            username = input("ingrese el nuevo nombre de usuario: ")
            password = input("ingrese la nueva contraseña: ")
            nuevo_usuario = Usuario(
                id_usuario=id_usuario, username=username, password=password)
            user_act = UsuarioDAO.actualizar(nuevo_usuario)
            print(f'Usuario actualizado: {nuevo_usuario}')
        elif opcion == 4:
            id_usuario = input("ingrese el id del usuario a eliminar: ")
            user_a_eliminar = Usuario(id_usuario=id_usuario)
            user_eliminado = UsuarioDAO.eliminar(user_a_eliminar)
            print(f'Usuario eliminado: {user_eliminado}')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None

else:
    print("Saliendo del programa...")
