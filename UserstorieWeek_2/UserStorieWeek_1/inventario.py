# Función para pedir el precio
def pedir_precio():
    sw = True
    while sw:
        try:
            # Reemplazamos coma por punto por si el usuario usa formato decimal regional
            precio = float(input("\nIngrese el precio del producto:\n").replace(",", ".").strip())
            
            if precio <= 0:
                print("El precio debe ser mayor que 0")
            else:
                sw = False
                return precio # CRÍTICO: Retornar el valor para usarlo fuera
                
        except ValueError:
            print("Digite solo números válidos")

# Función para pedir la cantidad
def pedir_cantidad():
    sw = True
    while sw:
        try:
            # Convertimos a int() como pide el TASK 2
            cantidad = int(input("\nIngrese la cantidad del producto: \n").strip())
            
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                sw = False
                return cantidad # CRÍTICO: Retornar el valor
            
        except ValueError:
            print("Digite solo números enteros válidos")

# Función para calcular el costo total
def costo_total(precio, cantidad):
    return precio * cantidad

# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
print("BIENVENIDO AL INVENTARIO")

# Solicitar nombre del producto
nombre = input("Ingrese el nombre del producto: \n").strip()

# Solicitar datos validados
precio = pedir_precio()
cantidad = pedir_cantidad()

# Calcular el costo total (Task 3)
total = costo_total(precio, cantidad)

# Mostrar resultados (Task 4)
print("\n--------RESUMEN---------\n")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {total}")

# -------------------------
# DESCRIPCIÓN GENERAL (Task 5)
# -------------------------
# Este programa solicita al usuario el nombre, precio y cantidad de un producto,
# valida que los datos numéricos sean correctos mediante ciclos y excepciones, 
# calcula el costo total y muestra un resumen formateado.