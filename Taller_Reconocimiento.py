#1 Elaborar un algoritmo y su debido proceso

def calcular_factorial(n):
    factorial = 1

    if n == 0 or n == 1:
        return factorial

    for i in range(2, n + 1):
        factorial *= i

    return factorial


numero = 5
resultado_esperado = 120

resultado = calcular_factorial(numero)
print("El factorial de", numero, "es:", resultado)

assert resultado == resultado_esperado, "El resultado no coincide con el esperado"

print("Prueba exitosa!")



#2 Se desea conocer para un grupo de 10 personas

def contar_personas_por_rango_edades(edades):
    conteo = {'0-20': 0, '20-30': 0, '30-40': 0, '40-60': 0, '60+': 0}

    for edad in edades:
        if edad <= 20:
            conteo['0-20'] += 1
        elif 20 < edad <= 30:
            conteo['20-30'] += 1
        elif 30 < edad <= 40:
            conteo['30-40'] += 1
        elif 40 < edad <= 60:
            conteo['40-60'] += 1
        else:
            conteo['60+'] += 1

    return conteo

edades = [18, 25, 33, 42, 55, 65, 16, 28, 36, 48]
resultado_esperado = {'0-20': 2, '20-30': 3, '30-40': 2, '40-60': 3, '60+': 0}

resultado = contar_personas_por_rango_edades(edades)
print("Total de personas por rango de edades:")
for rango, cantidad in resultado.items():
    print(rango + ":", cantidad)

assert resultado == resultado_esperado, "El resultado no coincide con el esperado"

print("Prueba exitosa!")

#3 tablas de multiplica

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

# Entrada del usuario
numero_ingresado = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Generar la tabla de multiplicar
tabla_multiplicar(numero_ingresado)


def calcular_precio_iva(precio_sin_iva, tasa_iva):
    precio_con_iva = precio_sin_iva * (1 + tasa_iva)
    return precio_con_iva


def main():
    total_sin_iva = 0

    # Ingreso de los precios de los 10 productos
    for i in range(1, 11):
        precio = float(input(f"Ingrese el precio del producto {i}: "))
        total_sin_iva += precio

    # Cálculo del total antes del IVA y después del IVA (suponiendo una tasa del 16%)
    tasa_iva = 0.16
    total_con_iva = calcular_precio_iva(total_sin_iva, tasa_iva)

    # Mostrar los resultados
    print("\nTotal antes de IVA:", total_sin_iva)
    print("Total después de IVA (16%):", total_con_iva)


if __name__ == "__main__":
    main()
#4 Realice un programa que permita saber el costo total de 10 producto

def calcular_precio_iva(precio_sin_iva, tasa_iva):
    precio_con_iva = precio_sin_iva * (1 + tasa_iva)
    return precio_con_iva


def main():
    total_sin_iva = 0

    for i in range(1, 11):
        precio = float(input(f"Ingrese el precio del producto {i}: "))
        total_sin_iva += precio

    tasa_iva = 0.16
    total_con_iva = calcular_precio_iva(total_sin_iva, tasa_iva)

    # Mostrar los resultados
    print("\nTotal antes de IVA:", total_sin_iva)
    print("Total después de IVA (16%):", total_con_iva)


if __name__ == "__main__":
    main()

