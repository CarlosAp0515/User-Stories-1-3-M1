def guardar_csv(inventario,ruta):
    if not inventario:
        print("El inventario esta vacio")
        return False
    try:
        with open(ruta, "w") as archivo:
            archivo.write("nombre,precio,cantidad\n")
            
            for producto in inventario:
                archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
                
        return True
    
    except Exception as e:
        print("Error:", e)
        return False
    
def cargar_csv(ruta):
    
    inventario =[]
    
    try:
        with open(ruta, "r") as archivo:
            next(archivo)
            
            for linea in archivo:
                linea = linea.strip()
                
                if not linea:
                    continue
                
                datos = linea.split(",")
                
                producto = {
                    "nombre": datos[0],
                    "precio": float(datos[1]),
                    "cantidad": int(datos[2])
                }
                inventario.append(producto)
        return inventario
    
    except Exception as e:
        print("Error:", e)
        return []
    
