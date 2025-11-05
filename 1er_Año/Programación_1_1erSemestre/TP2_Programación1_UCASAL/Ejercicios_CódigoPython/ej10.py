'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

Ej 10:
Solicitar al usuario los datos de inicio de sesión, como lo son Nombre
de Usuario y Contraseña. Luego validar los datos ingresados.
- Si el nombre es “Franco” y la contraseña “2022”, mostrar “Bienvenido
Franco! Inicio de sesión válido!”.
- Si alguno de los datos es incorrecto, mostrar el mensaje que
corresponda: “Nombre de usuario incorrecto, ¡no se puede iniciar sesión!” o
“Contraseña incorrecta, no se puede iniciar sesión!”.
- Si ambos datos son incorrectos, mostrar el mensaje “Usuario totalmente
desconocido! Fuera hacker!!”.
'''

usuario = input("Nombre de Usuario: ")
contraseña = input("Contraseña: ")

if usuario == "Franco" and contraseña == "2022":
    print("Bienvenido Franco! Inicio de sesión válido!")
elif usuario == "Franco":
    print("Contraseña incorrecta, no se puede iniciar sesión!")
elif contraseña == "2022":
    print("Nombre de usuario incorrecto, no se puede iniciar sesión!")
else:
    print("Usuario totalmente desconocido! Fuera hacker!!")