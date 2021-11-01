#34.	Escribe un algoritmo o el respectivo diagrama de flujo que, dado un usuario y una contraseña predefinida (por ejemplo usuario=”carlos" y contraseña=”1234”, le permita a un usuario digital su usuario y contraseña y enviar un mensaje de inicio de sesión si lo digitado corresponde al usuario y contraseña predefinida.
sesion={"usuario":"carlos","contraseña":"1234"}
usuario=input("Ingrese su usuario: ")
contraseña=input("Ingrese su contraseña: ")
if sesion.get("usuario")==usuario and sesion.get("contraseña")==contraseña:
    print("La sesión ha sido iniciada")
else:
    print("El usuario o contraseña está mal...no se ha iniciado sesión")