import os
from modelos.menu_unidades import MenuUnidades
from servicios.archivo_serivice import ArchivoService
from servicios.ejecucion_service import EjecucionService

# Clase principal del menú 
class Menu: #cambio realizado por clases
    def __init__(self):
        self.modelo = MenuUnidades()
        self.ruta_base = os.path.dirname(__file__)
        self.unidades = self.modelo.obtener_unidades()
# Iniciar el menú de unidades
    def iniciar(self):
        while True:
            self.mostrar_menu_principal()
            eleccion = input("Elige una unidad: ")

            if eleccion == '0':
                print("Saliendo...")
                break
            elif eleccion in self.unidades:
                self.mostrar_sub_menu(os.path.join(self.ruta_base, self.unidades[eleccion]))
            else:
                print("Opción no válida")

    def mostrar_menu_principal(self):
        print("\n=== Menu Principal de Unidades ===")
        for key in self.unidades:
            print(f"{key} - {self.unidades[key]}")
        print("0 - Salir")

    def mostrar_sub_menu(self, ruta_unidad):
        sub_carpetas = ArchivoService.listar_carpetas(ruta_unidad)

        while True:
            print("\n=== Submenú de Carpetas ===") # cambio realizado por submenú de carpetas
            for i, carpeta in enumerate(sub_carpetas, 1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar")

            eleccion = input("Elige carpeta: ")

            if eleccion == '0':
                break
            try:
                self.mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[int(eleccion)-1]))
            except:
                print("Opción inválida")

    def mostrar_scripts(self, ruta_sub): # cambio realizado por mostrar scripts
        scripts = ArchivoService.listar_scripts(ruta_sub)

        while True:
            print("\n=== Scripts ===")
            for i, script in enumerate(scripts, 1):
                print(f"{i} - {script}")
            print("0 - Regresar")

            eleccion = input("Elige script: ")

            if eleccion == '0':
                break

            try:
                ruta_script = os.path.join(ruta_sub, scripts[int(eleccion)-1])
                codigo = ArchivoService.leer_codigo(ruta_script)

                if codigo:
                    if input("¿Ejecutar? (1=Sí): ") == '1':
                        EjecucionService.ejecutar_script(ruta_script)

            except:
                print("Opción inválida")


# Arranque del sistema
if __name__ == "__main__":
    menu = Menu()
    menu.iniciar()
