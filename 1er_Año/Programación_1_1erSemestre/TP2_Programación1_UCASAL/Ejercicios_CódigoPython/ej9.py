'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

Ej 9:
Solicitar al usuario el ingreso de la Edad de una persona y una variable
que indique si tiene entrada al cine o no, luego valide si la persona es
mayor o igual a 16 años y si tiene entrada. Caso afirmativo muestre el
mensaje “Usted SI puede entrar a la sala de cine, que disfrute la película!”.
Si cualquiera de los dos requisitos no se cumple muestra el cartel “Usted
NO puede entrar a la sala de cine, lo siento mucho!”.
'''
edad_persona = int(input("Ingresa tu edad: "))
entrada = input("¿Tienes entrada? (Y si es asi, de lo contrario N): ").upper()


if edad_persona > 0:
    if (entrada == "Y"):
        if (edad_persona >= 16):
            print("Usted SI puede entrar a la sala de cine, que disfrute la película!")
        
        else:
            print("Usted NO puede entrar a la sala de cine, lo siento mucho!")
    
    elif (entrada == "N"):
        print("Usted NO puede entrar a la sala de cine, lo siento mucho!")
        
    else:
        print("Respuesta no válida. Debe ingresar Y o N.")

else:
    print("Edad no válida.")
