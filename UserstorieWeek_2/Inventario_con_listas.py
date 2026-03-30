def agregar_producto(inventario):
    """
    User Story 2: Como administrador quiero poder agregar productos al inventario 
    para mantener un registro actualizado.

    Funcionalidad:
    - Solicita al usuario el nombre, precio y cantidad del producto.
    - Valida que el precio y la cantidad sean mayores a 0 y numéricos.
    - Agrega el producto al inventario.

    Parámetros:
    inventario (list): Lista donde se almacenan los productos.

    Retorna:
    None
    """
    nombre = input("Ingrese el nombre del producto: ").strip()

    # Validar precio
    valido = False
    while not valido:
        try:
            precio = float(input("Ingrese el precio del producto: ").replace(",",".").strip())
            if precio <= 0:
                print("El precio debe ser mayor a 0.")
            else:
                valido = True
        except ValueError:
            print("El precio debe ser un número")

    # Validar cantidad
    valido = False
    while not valido:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: ").strip())
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
            else:
                valido = True
        except ValueError:
            print("La cantidad debe ser un número")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente")


def mostrar_inventario(inventario):
    """
    User Story 2: Como administrador quiero poder ver todos los productos 
    registrados en el inventario para verificar su existencia y cantidades.

    Parámetros:
    inventario (list): Lista de productos registrados.

    Retorna:
    None
    """
    if not inventario:
        print("El inventario está vacío")
        return
    
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']:.2f} | Cantidad: {producto['cantidad']}")


def calcular_estadisticas(inventario):
    """
    User Story 2: Como administrador quiero poder calcular estadísticas del inventario 
    para conocer el valor total y cantidad de productos disponibles.

    Funcionalidad:
    - Calcula el valor total del inventario.
    - Cuenta el número de productos registrados.
    - Suma la cantidad total de unidades.

    Parámetros:
    inventario (list): Lista de productos registrados.

    Retorna:
    None
    """
    if not inventario:
        print("No hay productos para calcular estadísticas")
        return
    
    valor_total = 0
    cantidad_productos = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        cantidad_productos += producto["cantidad"]

    print(f"Valor total del inventario: ${valor_total}")
    print(f"Número de productos registrados: {len(inventario)}")
    print(f"Cantidad total de unidades: {cantidad_productos}")


def main():
    """
    Función principal del programa.

    User Story 2: Como usuario quiero poder interactuar con el sistema mediante un menú
    para agregar productos, mostrar el inventario y calcular estadísticas.

    Funcionalidad:
    - Muestra un menú con opciones.
    - Permite agregar productos, mostrar inventario, calcular estadísticas o salir.
    - Valida la opción ingresada por el usuario.

    Retorna:
    None
    """
    menu = ""
    inventario = []

    while menu != "4":
        menu = input(
            "Ingrese el número de la opción deseada:\n"
            "1. Agregar producto\n"
            "2. Mostrar inventario\n"
            "3. Calcular estadísticas\n"
            "4. Salir\n"
        )

        if menu == "1":
            agregar_producto(inventario)
        elif menu == "2":
            mostrar_inventario(inventario)
        elif menu == "3":
            calcular_estadisticas(inventario)
        elif menu == "4":
            print("Gracias por usar nuestro programa")
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


# Ejecutar programa
main()