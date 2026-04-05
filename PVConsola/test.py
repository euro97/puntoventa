import VentasDAO as vd
import Ventas as v

datos = vd.consultarVentas()

for i in datos:
    print(f"ID Venta: {i[0]}, ID Detalle: {i[1]}, Cliente: {i[4]}, Producto: {i[5]}, Cantidad: {i[7]}, Método de Pago: {i[3]}, Total: {i[2]}")