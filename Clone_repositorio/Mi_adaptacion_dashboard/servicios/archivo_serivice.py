import os
# Servicio para manejar operaciones de archivos
# Creacion de la clase ArchivoService

class ArchivoService: #Herencia de la clase archivo service

    @staticmethod
    def listar_carpetas(ruta): # cambio ralizado por listar carpetas
        return [f.name for f in os.scandir(ruta) if f.is_dir()]

    @staticmethod
    def listar_scripts(ruta):# Listar archivos .py en una ruta dada
        return [f.name for f in os.scandir(ruta) if f.is_file() and f.name.endswith('.py')]

    @staticmethod
    def leer_codigo(ruta_script): # Leer el contenido de un archivo de script
        try:
            with open(ruta_script, 'r') as archivo: 
                codigo = archivo.read()
                print(f"\n--- Código de {ruta_script} ---\n")
                print(codigo)
                return codigo
        except Exception as e:
            print(f"Error: {e}")
            return None
