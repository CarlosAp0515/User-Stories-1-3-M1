def agregar_producto(inventario,nombre,precio,cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto.
    precio (float): Precio del producto.
    cantidad (int): Cantidad disponible.

    Retorna:
    bool: True si se agregó correctamente.
    """
    while precio < 0:
        try:
            if precio < 0:
                print("El precio no puede ser negativo")
                precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("El precio debe ser un valor numérico")
            precio = float(input("Ingrese el precio del producto: "))   
    while cantidad < 0:
        try:
            if cantidad < 0:
                print("La cantidad no puede ser negativa")
                cantidad = int(input("Ingrese la cantidad del producto: "))
        except ValueError:  
            print("La cantidad debe ser un valor numérico")
            cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    return True
    

def buscar_producto(inventario,nombre):
    """
    Busca un producto por nombre en el inventario.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto a buscar.

    Retorna:
    dict | None: Producto encontrado o None si no existe.
    """
    for producto in inventario:
        if producto["nombre"].lower().strip() == nombre.lower().strip():
            return producto
    return None
    
    

def actualizar_producto(inventario,nombre,nuevo_precio = None,nueva_cantidad = None):
    """
    Actualiza el precio y/o la cantidad de un producto.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto.
    nuevo_precio (float, opcional): Nuevo precio.
    nueva_cantidad (int, opcional): Nueva cantidad.

    Retorna:
    bool: True si se actualizó, False si no se encontró.
    """
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        return False

    if nuevo_precio is not None:
        while nuevo_precio < 0:
            print("El precio no puede ser negativo")
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            except ValueError:
                print("El precio debe ser un valor numérico")
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        while nueva_cantidad < 0:
            print("La cantidad no puede ser negativa")
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            except ValueError:
                print("La cantidad debe ser un valor numérico")
        producto["cantidad"] = nueva_cantidad

    return True
    
    
def eliminar_producto(inventario,nombre):
    """
    Elimina un producto del inventario.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto a eliminar.

    Retorna:
    bool: True si se eliminó, False si no se encontró.
    """
    producto = buscar_producto(inventario,nombre)
    if producto is None:
        return False
    
    inventario.remove(producto)
    return True
    

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.

    Parámetros:
    inventario (list): Lista de productos.

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
    Calcula estadísticas del inventario.

    Parámetros:
    inventario (list): Lista de productos.

    Retorna:
    dict | None: Diccionario con estadísticas o None si está vacío.
    """
    if not inventario:
        return None
    
    
    valor_total = 0
    unidades_totales = 0
    producto_mayor_stock = None
    producto_mas_caro = None
    

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        unidades_totales += producto["cantidad"]
        if producto_mayor_stock is None or producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

        if producto_mas_caro is None or producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

    return {
        "valor_total": valor_total,
        "unidades_totales": unidades_totales,
        "producto_mayor_stock": producto_mayor_stock,
        "producto_mas_caro": producto_mas_caro
    }
    
