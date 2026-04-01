def pedir_precio(mensaje="Ingrese el precio: ", opcional=False):
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        
        if not entrada and opcional: # Si es opcional y está vacío, sale
            return None
        if not entrada and not opcional: # Si NO es opcional y está vacío, error
            print("Error: Este campo es obligatorio.")
            continue
            
        try:
            precio = float(entrada)
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
            else:
                return precio
        except ValueError:
            print("Error: Ingrese un número válido.")

def pedir_cantidad(mensaje="Ingrese la cantidad: ", opcional=False):
    while True:
        entrada = input(mensaje).strip()
        
        if not entrada and opcional:
            return None
        if not entrada and not opcional:
            print("Error: Este campo es obligatorio.")
            continue
            
        try:
            cantidad = int(entrada)
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa.")
            else:
                return cantidad
        except ValueError:
            print("Error: Ingrese un número entero.")