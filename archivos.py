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
    """
    Carga productos desde un CSV. Omite filas inválidas e informa errores.
    """
    inventario_cargado = []
    filas_omitidas = 0
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            # Saltar encabezado
            next(archivo)
            
            for linea in archivo:
                linea = linea.strip()
                if not linea: continue
                
                datos = linea.split(",")
                
                # TASK 5: Validar exactamente 3 columnas
                if len(datos) != 3:
                    filas_omitidas += 1
                    continue
                
                try:
                    producto = {
                        "nombre": datos[0].strip(),
                        "precio": float(datos[1]),
                        "cantidad": int(datos[2])
                    }
                    # Validar no negativos
                    if producto["precio"] < 0 or producto["cantidad"] < 0:
                        filas_omitidas += 1
                        continue
                        
                    inventario_cargado.append(producto)
                except ValueError:
                    filas_omitidas += 1
                    
        if filas_omitidas > 0:
            print(f"Advertencia: {filas_omitidas} filas inválidas fueron omitidas.")
            
        return inventario_cargado
    
    except FileNotFoundError:
        print(f"Error: El archivo en {ruta} no existe.")
        return None # Retornar None ayuda a diferenciar entre "archivo vacío" y "archivo no existe"
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
