import math

def calculadora_avanzada():
    print("--- Calculadora Python: Edición Científica ---")
    print("Opciones:")
    print("1. Suma (+) | 2. Resta (-) | 3. Multiplicación (*)")
    print("4. División (/) | 5. Raíz Cuadrada (√) | 6. Usar Pi (π)")
    print("7. Elevar al cuadrado (x²) | 8. Salir")

    while True:
        opcion = input("\nSelecciona una opción (1-8): ")

        if opcion == '8':
            print("¡Hasta luego!")
            break

        try:
            # Operaciones básicas que requieren dos números
            if opcion in ['1', '2', '3', '4']:
                n1 = float(input("Primer número: "))
                n2 = float(input("Segundo número: "))
                
                if opcion == '1': print(f"Resultado: {n1 + n2}")
                elif opcion == '2': print(f"Resultado: {n1 - n2}")
                elif opcion == '3': print(f"Resultado: {n1 * n2}")
                elif opcion == '4':
                    if n2 == 0: print("Error: No se puede dividir por cero.")
                    else: print(f"Resultado: {n1 / n2}")

            # Raíz Cuadrada
            elif opcion == '5':
                n = float(input("Número para extraer raíz: "))
                if n < 0:
                    print("Error: No existe raíz real de un número negativo.")
                else:
                    print(f"Resultado: √{n} = {math.sqrt(n)}")

            # Constante Pi
            elif opcion == '6':
                print(f"El valor de Pi es aproximadamente: {math.pi}")
                multiplicar = input("¿Quieres multiplicarlo por algún número? (s/n): ")
                if multiplicar.lower() == 's':
                    n = float(input("Multiplicar π por: "))
                    print(f"Resultado: {n} * π = {n * math.pi}")

            # Elevar al cuadrado (LO NUEVO)
            elif opcion == '7':
                n = float(input("Número a elevar al cuadrado: "))
                resultado = n ** 2  # También podrías usar math.pow(n, 2)
                print(f"Resultado: {n}² = {resultado}")

            else:
                print("Opción no válida.")
                
        except ValueError:
            print("Error: Entrada no válida. Por favor, usa números.")

# ¡No olvides esta línea! Es la que hace que el programa arranque.
calculadora_avanzada()