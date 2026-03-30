from servicios import *
from archivos import *
from helpers import *

inventario = cargar_csv("inventario.csv")
if inventario is None:
    inventario = []

option = ""

while option != "7":
    option = input("Ingrese la opcion que desea: \n"
                   "1. Agregar producto\n"
                   "2. Mostrar inventario\n"
                   "3. Buscar producto\n"
                   "4. Actualizar producto\n"
                   "5. Eliminar producto\n"
                   "6. Calcular estadisticas\n"
                   "7. Salir\n"
                   "=> : ")
    if option == "1":
        nombre = input("Ingrese el nombre del producto: ").capitalize().strip()
        precio = pedir_precio()
        cantidad = pedir_cantidad()
        agregar_producto(inventario, nombre, precio, cantidad)
        print("Producto agregado exitosamente")
    elif option == "2":
        mostrar_inventario(inventario)
    elif option == "3":
        nombre = input("Ingrese el nombre del producto: ").capitalize().strip()
        producto = buscar_producto(inventario, nombre)
        if producto:
            print(f"Producto encontrado: {producto['nombre']} - Precio: ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")
        else:
            print("Producto no encontrado")
            
    elif option == "4":
        nombre = input("Ingrese el nombre del producto: ").capitalize().strip()
        
        nuevo_precio_input = input("Ingrese el nuevo precio del producto: ").strip()
        nueva_cantidad_input = input("Ingrese la nueva cantidad del producto: ").strip()
        
        #convertir solo si el usuario escribe algo
        nuevo_precio = pedir_precio() if nuevo_precio_input.strip() != "" else None
        nueva_cantidad = pedir_cantidad() if nueva_cantidad_input.strip() != "" else None
        
        actualizado =actualizar_producto(inventario,nombre,nuevo_precio,nueva_cantidad)
        
        if actualizado:
            print("Producto actualizado exitosamente")
        else:
            print("Producto no encontrado")
    elif option == "5":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        
        eliminado =eliminar_producto(inventario, nombre)
        if eliminado:
            print("Producto eliminado correctamente")
        else:
            print("Producto no encontrado")
    elif option == "6":
        estadisticas = calcular_estadisticas(inventario)
        if estadisticas is None:
            print("No hay productos en el inventario")
        else:
            print("------Resumen del inventario------")
            print(f"Unidades totales: {estadisticas['unidades_totales']}")
            print(f"Valor total: {estadisticas['valor_total']}")
            print(f"Producto mas caro: {estadisticas['producto_mas_caro']['nombre']} con ${estadisticas['producto_mas_caro']['precio']:.2f}")
            print(f"Producto mayor stock: {estadisticas['producto_mayor_stock']['nombre']} con {estadisticas['producto_mayor_stock']['cantidad']} unidades")
    elif option == "7":
        guardar_csv(inventario, "inventario.csv")
        print("Gracias por usar el programa")
    else:
        print("Opcion no valida")

