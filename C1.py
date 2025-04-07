def mostrar_menu():
    print("===== Menú Principal =====")
    print("1. Opción 1: Pasta")
    print("2. Opción 2: Lasagna")
    print("3. Opción 3: Limonada")
    print("4. Opción 4: Agua mineral")
    print("5. Salir")
    print("===========================")


def ejecutar_menu():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            
            if opcion == 1:
                print("Has seleccionado 'Ver información'.")
            elif opcion == 2:
                print("Has seleccionado 'Agregar datos'.")
            elif opcion == 3:
                print("Has seleccionado 'Actualizar datos'.")
            elif opcion == 4:
                print("Has seleccionado 'Eliminar datos'.")
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, selecciona entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
        
        print("\n")  # Espacio para mejor legibilidad entre iteraciones