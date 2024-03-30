#1 Crear un programa que pida al usuario una contraseña
def main():
    contraseña_correcta = "1234"
    while True:
        contraseña = input("Introduce la contraseña: ")
        if contraseña == contraseña_correcta:
            print("Bienvenido.")
            break
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

#2 Crea un programa que genere dos números al azar entre el 0 y el 10

import random

def main():
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)
    suma_correcta = numero1 + numero2

    while True:
        respuesta_usuario = int(input(f"¿Cuál es la suma de {numero1} y {numero2}? "))
        if respuesta_usuario == suma_correcta:
            print("¡Respuesta correcta!")
            break
        else:
            print("Respuesta incorrecta. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

