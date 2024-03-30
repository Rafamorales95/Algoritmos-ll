#1. Pide al usuario que ingrese una palabra o frase
def contar_vocales(frase):
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in frase:
        if letra.lower() in conteo_vocales:
            conteo_vocales[letra.lower()] += 1
    return conteo_vocales

def main():
    frase = input("Ingrese una palabra o frase: ")
    resultado = contar_vocales(frase)

    print("Conteo de vocales:")
    for vocal, conteo in resultado.items():
        print(f"{vocal}: {conteo}")

if __name__ == "__main__":
    main()

#2. Escribe un programa que lea una lista de nombres
def main():
    entrada = input("Ingrese una lista de nombres separados por comas: ")

    lista_nombres = entrada.split(",")

    lista_nombres = [nombre.strip() for nombre in lista_nombres]

    lista_nombres.sort()

    print("Lista de nombres en orden alfabético:")
    for nombre in lista_nombres:
        print(nombre)

if __name__ == "__main__":
    main()
#3. Escribe un programa que lea una lista de palabras
def palabras_que_comienzan_con_letra(lista_palabras, letra):
    palabras_coincidentes = [palabra for palabra in lista_palabras if palabra.startswith(letra)]
    return palabras_coincidentes

def main():
     entrada = input("Ingrese una lista de palabras separadas por comas: ")

    lista_palabras = entrada.split(",")

    letra_inicio = input("Ingrese la letra con la que deben comenzar las palabras: ")

    palabras_coincidentes = palabras_que_comienzan_con_letra(lista_palabras, letra_inicio)

    print(f"Palabras que comienzan con '{letra_inicio}':")
    for palabra in palabras_coincidentes:
        print(palabra.strip())

if __name__ == "__main__":
    main()

#4. Escribe un programa lea una lista de números e imprima la suma de los números pares.
def suma_numeros_pares(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:  # Verificar si el número es par
            suma += numero
    return suma

def main():
    # Solicitar al usuario que ingrese una lista de números separados por comas
    entrada = input("Ingrese una lista de números separados por comas: ")

    # Convertir la entrada en una lista de números
    lista_numeros = [int(numero.strip()) for numero in entrada.split(",")]

    # Calcular la suma de los números pares
    suma_pares = suma_numeros_pares(lista_numeros)

    # Imprimir la suma de los números pares
    print("La suma de los números pares es:", suma_pares)

if __name__ == "__main__":
    main()

