# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:08:42 2021

@author: sigri
"""
# Creo un diccionario con los datos de mi mascota.
Hamster = {'Nombre': 'Biggs', 'Edad': 1, 'Peso': 0.4,
           'Hungry': False, 'Mood' : 'Happy','Photo': "Foto del Hamster" }

def feed (Nombre):
    if Hamster ["Hungry"] == False:
        Hamster["Hungry"] = False
        Hamster["Peso"] += 0.4 
    else:
     print(f"La mascota {Hamster['Nombre']} no tiene hambre\n")
feed("Biggs")
print(Hamster)


# Datos mascota
print("Datos mascota")
print("-------------------")
print(f"Nombre: {Hamster['Nombre']}")
print(f"Edad: {Hamster['Edad']}")
print(f"Peso: {Hamster['Peso']}")
#condicion si Hamster es exactamente Falso, entonces(:)
if Hamster["Hungry"]== False: 
    print("No tiene hambre.")
elif Hamster["Mood"] == "sad" or Hamster["Mood"] == "Sad":
    print("Está triste.")
else:
    print("Estado de ánimo: Feliz")
    print(f"Foto: {Hamster['photo']} \n")
# cambiamos los valores de false a true.
def cambiar_valores(Hamster):
    Hamster["hungry"] = True
    Hamster["mood"] = "sad"
    Hamster(Hamster)
    return Hamster
def alimentar_mascota(Hamster):
    # recorremos el diccionario con for
    for k,y in Hamster.items():
            
            if str(k) == "hungry": 
                y = False          
            elif str(k) == "Peso":
                y += 0.4
    Hamster(Hamster)
    return Hamster
def play(Hamster):
    Hamster["Mood"]="Happy"
    Hamster["Peso"] -= 0.4
    
    if (Hamster["Peso"] < 0.4):
        Hamster["hungry"] = True
        print("---> Biggs está cansado y hambriento. <--- \n")
        
    Hamster(Hamster)
    return Hamster

    

 
    
    

        
        


