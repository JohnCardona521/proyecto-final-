
from ast import While
from pickle import TRUE

#se crea una lista vacia para poder guardar las palabras
palabras=[]
for i in range (20):
    palabra=input (f"ingrese la palabra {i+1:}")
    palabras.append(palabra)
    
#se utiliza la funcion para que ordene la lista de palabras por su tamaño

def ordenar_por_tamaño(palabras):
  return sorted(palabras,key=len,reverse=True)


#se le muestra un menu de opciones al usuario

while True:
 print("\n Seleccione una opcion: ")
 print("1.Orden alfabetico")
 print("2.Orden de tamaño,de las mas larga a la mas corta")
 print("3.Orden aleatorio")
 print("4.Orden inverso al ingresado")
 print("5.Orden igual al ingresado")
 print("6.Salir")
 seleccion=input("elija una opcion:")
 
 match seleccion:
         case "1":
             palabras_ordenadas=sorted(palabras) 
         case "2":
             palabras_ordenadas=ordenar_por_tamaño(palabras)
         case "3":
             import random
             random.shuffle(palabras)
             palabras_ordenadas=palabras
         case "4":
             palabras_ordenadas=list(reversed(palabras))
         case "5":
             palabras_ordenadas=palabras
         case "6":
             print("salir")
         case"_":
             print("Opcion no valida. Elija una opcion de 1 al 6.")
             continue

#se observa la lista de palabras segun la opcion elegida por el usuario

 print("\npalabras ordenadas")
 for palabra in palabras_ordenadas:
        print(palabra)