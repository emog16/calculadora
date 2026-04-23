import math

def calculadora():
    print("--- Calculadora Pro ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz Cuadrada")
    print("6. Elevar al cuadrado")
    print("7. Ver valor de PI")
    print("8. Salir")

    while True:
        opcion = input("\nSelecciona una opción (1-8): ")

        if opcion == '8':
            print("¡Nos vemos!")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))

            if opcion == '1': print(f"Resultado: {num1 + num2}")
            elif opcion == '2': print(f"Resultado: {num1 - num2}")
            elif opcion == '3': print(f"Resultado: {num1 * num2}")
            elif opcion == '4': 
                if num2 != 0: print(f"Resultado: {num1 / num2}")
                else: print("Error: No se puede dividir por cero.")

        elif opcion == '5':
            num = float(input("Número para raíz cuadrada: "))
            if num >= 0:
                print(f"Resultado: {math.sqrt(num)}")
            else:
                print("Error: No existe raíz de número negativo.")

        elif opcion == '6':
            num = float(input("Número a elevar al cuadrado: "))
            print(f"Resultado: {num**2}")

        elif opcion == '7':
            print(f"El valor de PI es: {math.pi}")

        else:
            print("Opción no válida.")

calculadora()
