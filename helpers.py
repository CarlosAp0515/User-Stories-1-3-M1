def pedir_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo")
            else:
                return precio
        except ValueError:
            print("El precio debe ser un valor numérico")

def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa")
            else:
                return cantidad
        except ValueError:
            print("La cantidad debe ser un número entero")
            