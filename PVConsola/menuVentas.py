import VentasDAO as ventaDAO

def consultar():
    ventas = ventaDAO.consultarVentas()
    for v in ventas:
        print(f"ID Venta: {v[0]}, ID Detalle: {v[1]}, Cliente: {v[4]}, Producto: {v[5]}, Cantidad: {v[7]}, Método de Pago: {v[3]}, Total: {v[2]}")

def agregar():
    ventaDAO.agregarVenta()

def modificar():
    ventaDAO.modificarVenta()

def eliminar():
    ventaDAO.eliminarVenta()

def menu_ventas():
    while True:
        print("\n--- VENTAS ---")
        print("1. Consultar ventas")
        print("2. Agregar venta")
        print("3. Modificar venta")
        print("4. Eliminar venta")
        print("5. Volver al menú principal")

        opcion = int(input("Seleccione opción: "))

        if opcion == 1:
            consultar()
        elif opcion == 2:
            agregar()
        elif opcion == 3:
            modificar()
        elif opcion == 4:
            eliminar()
        elif opcion == 5:
            break
        else:
            print("Opción inválida")