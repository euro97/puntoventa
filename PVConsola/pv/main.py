import Producto
import productoDAO

ciclo = True

def consultar():
    productos = productoDAO.consultarProductos()
    for i in productos:
        print(f"{i[0]} \t {i[1]}")
    

def agregar():
    nombre = input("Nombre: ")
    marca = input("Marca: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    tamano = input("Tamaño: ")
    p = Producto.Producto(nombre,precio,marca,cantidad,tamano)
    productoDAO.agregarProducto(p)
    return "Agregado"


def modificar():
    productoDAO.modificarProducto()
    

def eliminar():
    productoDAO.eliminarProducto()


def salir():
    global ciclo 
    ciclo = False
    return "Saliendo ..."


def productos(opcion):
    
    switcher = {
        1: consultar,
        2: agregar,
        3: modificar,
        4: eliminar,
        5: salir
    }
    
    handler   = switcher.get(opcion, lambda: "Unknown Status")
    return handler()

while ciclo:
    print("\n--- POS Consola ---")
    print("1. Consultar")
    print("2. Agregar producto")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = int(input("Seleccione opción: "))
    productos(opcion)


