#practica
from collections.abc import KeysView
nuevoNum=""
nuevoNom=""
consultas ={
  "jose":"302944",
  "mario":"829455",
  "angel":"829405",
  "luis":"930594"
  }
menu=("1","2","3","4","5")
menuOpciones = {
    "1":"consultar",
    "2":"agregar",
    "3":"modificar",
    "4":"Borrar",
    "5":"salir"
}
print(menuOpciones)
seleccionMenu= input(f"Ingrse el vlaor de la opcion que desea ejecutar: \n")
if seleccionMenu == menu[0]:#consulta
  nombre = str(input(f"ingrese un nombre : \n"))
  if nombre in consultas:
   print(f"consultas {nombre}:{consultas[nombre]} ")
  else:
   print(f"{nombre} no existe ")
if seleccionMenu == menu[1]:#añdir
  nuevoNom = input(f"ingrese un nuevo usuario : \n")
  while nuevoNom in consultas.keys():
    print(f"{nuevoNom} ya existe ")
    nuevoNom = input(f"ingrese un nuevo usuario : \n")
  nuevoNum = input(f"ingrese un nuevo numero : \n")
  if nuevoNum in consultas.items():
   print(f"el numero {nuevoNum} ya existe")
   nuevoNum = input(f"ingrese un nuevo numero : \n")
  else:
    if  nuevoNum in consultas.values():
      print(f"el numero {nuevoNum} ya existe")
      nuevoNum = input(f"ingrese un nuevo numero : \n") 
consultas[nuevoNom]=nuevoNum
print(consultas)

if seleccionMenu == menu[2]:#modificar
  nuevoNom = str(input(f"ingrese un nombre : \n"))
  if nuevoNom in consultas.keys():
     nuevoNum = input(f"ingrese el nuevo numero : \n")
     consultas[nuevoNom]=nuevoNum
     print(consultas)
  else:
     print(f"el nombre  {nuevoNom} no existe")
  print(consultas)
if seleccionMenu == menu[3]:#borrar
  nuevoNom = str(input(f"ingrese un nombre : \n"))
  if nuevoNom in consultas.keys():
     consultas[nuevoNom]=""
     print(consultas)
  else:
     print(f"el nombre  {nuevoNom} no existe")
     print(consultas)
if seleccionMenu == menu[4]:#salir
  print("saliendo del programa")
  exit()