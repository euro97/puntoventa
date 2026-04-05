from inventario import menu_productos
from menuVentas import menu_ventas

def main():
    while True:
        print("\n--- POS Consola ---")
        print("1. Inventario (Productos)")
        print("2. Ventas")
        print("3. Salir")

        opcion = int(input("Seleccione opción: "))

        if opcion == 1:
            menu_productos()
        elif opcion == 2:
            menu_ventas()
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()