import os
from pathlib import Path

def inicio(ruta): 

    os.system("cls")
    print("-" * 47)
    print("-" * 6 + "| Bienvenidos al libro de recetas |" + "-" * 6)
    print("-" * 47)
    print(f"\nLas recetas se encuentran en: {ruta}")
    print(f"El numero de recetas es de: {sum(1 for r in ruta.rglob("*") if r.is_file())}")
    input("\nPresiona Enter para continuar...")
    os.system("cls")

def menu_op(): 
    
    print("""MENU:
          [1] Leer Receta
          [2] Crear Receta
          [3] Crear Categoría 
          [4] Eliminar Receta
          [5] Eliminar Categoría
          [6] Salir""")
    return input("\nDigita una opción: ")

def mostrar_categorias(ruta):

    os.system("cls") 
    print("Categorías: ")
    categorias = Path(ruta)
    lista_categorías = []

    for i, carpeta in enumerate(categorias.iterdir()): 
        print(f"[{i + 1}]. {carpeta.name}")
        lista_categorías.append(carpeta)
    
    eleccion = input("Elige una categoría: ")
    eleccion = int(eleccion) - 1
    return lista_categorías[eleccion]

def mostrar_recetas(eleccion_categoria): 
    
    os.system("cls")
    print("Recetas: ")
    recetas = Path(eleccion_categoria)
    lista_recetas = []

    for i, receta in enumerate(recetas.glob("*.txt")):
        print(f"[{i + 1}]. {receta.stem}")
        lista_recetas.append(receta)
    
    eleccion = input("Escoge una receta: ")
    eleccion = int(eleccion) - 1
    return lista_recetas[eleccion]
      
def leer_receta (eleccion_receta): 
    
    os.system("cls")

    file = open(eleccion_receta, 'r')
    print(file.read())

    file.close()

    input("\nPresiona Enter para continuar...")

def crear_receta(eleccion_categoria): 

    os.system("cls")
    nombre = input("Digita el nombre de la nueva receta: ")
    nombre += ".txt"

    nueva_receta = Path(eleccion_categoria, nombre)
    print(nueva_receta)
    file = open(nueva_receta, 'w')

    file.write(input("Ingresa la nueva receta: \n"))
    file.close()

    print("¡Receta guardada!")

def crear_categoría(ruta):

    os.system("cls")
    nombre = input("Ingresa el nombre de la nueva categoría: ")
    ruta_nueva = Path(ruta, nombre)
    os.makedirs(ruta_nueva)
    print("¡Nueva categoría creada!")

def eliminar_receta(eleccion_receta): 

    os.remove(eleccion_receta)
    print("Receta Eliminada ")

def eliminar_categoria(eleccion_categoria): 

    os.rmdir(eleccion_categoria)
    print("¡Categoría eliminada!")


ruta = Path(Path.home(), "Recetas")
inicio(ruta)

menu = 0

while(menu != 6):

    menu = menu_op()
    menu = int(menu)

    match menu: 
        case 1: 
            eleccion_categoria = mostrar_categorias(ruta)
            eleccion_receta = mostrar_recetas(eleccion_categoria)
            leer_receta(eleccion_receta)

        case 2: 
            eleccion_categoria = mostrar_categorias(ruta)
            crear_receta(eleccion_categoria)

        case 3: 
            crear_categoría(ruta)

        case 4: 
            eleccion_categoria = mostrar_categorias(ruta)
            eleccion_receta = mostrar_recetas(eleccion_categoria)
            eliminar_receta(eleccion_receta)

        case 5: 
            eleccion_categoria = mostrar_categorias(ruta)
            eliminar_categoria(eleccion_categoria)
        
        case 6: 
            pass 
            
        case _:
            print("Opción invalida")

    os.system("cls")