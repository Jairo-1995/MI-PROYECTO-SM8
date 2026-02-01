import os
import subprocess
# Servicio para ejecutar scripts
# Creacion de la clase EjecucionService

class EjecucionService: #Herencia de la clase ejecucion service

    @staticmethod
    def ejecutar_script(ruta_script):# Ejecutar un script en una nueva terminal
        try: #polimorfismo en el metodo ejecutar script
            if os.name == 'nt':
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        except Exception as e:
            print(f"Error al ejecutar: {e}") 