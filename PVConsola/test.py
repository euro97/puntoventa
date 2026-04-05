import VentasDAO as vd
import Ventas as v

datos = vd.consultarVentas()

for i in datos:
    print(i)
