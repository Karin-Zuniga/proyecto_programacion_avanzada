from comunidad import Comunidad
from enfermedad import Enfermedad
from ciudadano import Ciudadano

import numpy as np
import pandas as pd
import csv
import random






# def crear_enfermedad():
#     lista_enfermedades = ["Diabetes tipo 2", "Hipertensión arterial", "Enfermedad pulmonar obstructiva crónica (EPOC)", "Enfermedad renal crónica", "Artritis reumatoide", "Enfermedades cardiovasculares", "Cáncer crónico", "Obesidad mórbida", "Fibrosis quística", "Esclerosis múltiple", "Enfermedad de Crohn", "Esquizofrenia", "VIH/SIDA", "Enfermedad de Parkinson", "Alzheimer", "Hepatitis crónica", "Epilepsia", "Lupus eritematoso sistémico", "Hemofilia", "Osteoporosis"]
#     enfermedades_creadas = []
#     for enfermedad in lista_enfermedades:
#         nueva_enfermedad = Enfermedad(enfermedad)
#         enfermedades_creadas.append([nueva_enfermedad.get_nombre(),nueva_enfermedad.get_infeccion_probable(),nueva_enfermedad.get_promedio_pasos(),nueva_enfermedad.get_enfermo(), nueva_enfermedad.get_contador()])
#     headers = ["Nombre", "Infeccion probable", "Promedio pasos", "Enfermo", "Contador"]
#     df = pd.DataFrame(enfermedades_creadas, columns = headers)
#     df.to_csv("enfermedades.csv")
#     print("Creado archivo csv")
# #-----------------------Ciudadano-----------------

def crear_ciudadano():

    n = 100
    file_nombres = pd.read_csv("nombres_apellidos.csv")

    nombre_apellido = pd.DataFrame(file_nombres).to_numpy()

    archivo = []
    
    lista_ciudadanos = []
    for nombre,apellido in nombre_apellido:
        ciudadano = Ciudadano( n, nombre +" "+ apellido, asignar_comunidad())

        #ciudadano = asignar_enfermedades(ciudadano)
        lista_ciudadanos.append(ciudadano)
        n +=1 
    lista_ciudadanos = asignar_contactos(lista_ciudadanos)
    for ciudadano in lista_ciudadanos:
        lista_contactos = []
        print(ciudadano.get_contactos())
        for contacto in ciudadano.get_contactos():
           lista_contactos.append(contacto.get_nombre_apellido())
        print(lista_contactos)
        archivo.append([ciudadano.get_id(), ciudadano.get_nombre_apellido(), ciudadano.get_enfermedad(), ciudadano.get_comunidad(), lista_contactos, ciudadano.get_estado()])
    #lista_ciudadanos = reorganizar_contactos(lista_ciudadanos)

    headers = ["ID","Nombre", "enfermedades", "Comunidad", "Contactos", "Estado"]

    df = pd.DataFrame(archivo, columns=headers)
    df.to_csv("ciudadano.csv")
    print("Archivo CSV generado con exito")
    

        
        #----creando lista con nombres y apellidos----
def crea_nombres():
    nombres = ["Ana", "Juan", "María", "Carlos", "Laura", "José", "Andrea", "David", "Sofía", "Alejandro", "Claudia", "Pedro", "Gabriela", "Fernando", "Natalia", "Luis", "Valeria", "Miguel", "Paola", "Jorge", "Daniela", "Ricardo", "Andrea", "Javier", "Adriana", "Diego", "Patricia", "Manuel", "Vanessa", "Marco", "Verónica", "Martín", "Carolina", "Óscar", "Pamela", "Eduardo", "Angélica", "Sergio", "Brenda", "Juan Carlos", "Esther", "Raúl", "Silvia", "Antonio", "Victoria", "Alan", "Diana", "Salvador", "Rosa", "Juan Pablo", "Elena", "Mario", "Lorena", "Israel", "Alma", "Héctor", "Mariana", "Gabriel", "Vanessa", "Guillermo", "Susana", "Roberto", "Ana María", "Ernesto", "Ana Laura", "Emilio", "Cecilia", "Arturo", "Luz", "Omar", "Alejandra", "Octavio", "Estela", "Ignacio", "Laura Elena", "Hugo", "Carmen", "Jorge Luis", "Alma Rosa", "Ángel", "Adrián", "Teresa", "Francisco", "Lorena", "Raúl", "Alma Delia", "Víctor", "Rosario", "Rubén", "Andrea", "Francisco Javier", "Margarita", "Efraín", "Martha", "Julio", "Ana Karen", "René", "Isabel", "Armando", "Patricia", "Leopoldo", "Inés", "Salvador", "Claudia Patricia", "Mauricio", "Brenda", "Víctor Manuel", "Alicia", "Federico", "Daniela", "Agustín", "Verónica", "Eduardo", "Carmen"]
    apellidos = ["Martínez", "González", "Rodríguez", "López", "Hernández", "Pérez", "Sánchez", "Ramírez", "Torres", "Flores", "Gómez", "Díaz", "Reyes", "Morales", "Ortiz", "Castro", "Ruiz", "Chávez", "Vásquez", "Ramos", "Álvarez", "Jiménez", "Fernández", "Gutiérrez", "Mendoza", "Soto", "Aguilar", "Silva", "Romero", "Mendoza", "Chavez", "Juárez", "Guerrero", "Palacios", "Maldonado", "Pinto", "Rojas", "Molina", "Salazar", "Herrera", "Vega", "Vargas", "Cortés", "Navarro", "Peña", "Luna", "Cruz", "León", "Campos", "Cabrera", "Montes", "Zamora", "Acosta", "Orozco", "Quintero", "Ibarra", "Escobar", "Barajas", "Guerrero", "Santana", "Miranda", "Espinoza", "Valencia", "Barrera", "Figueroa", "Lara", "Cervantes", "Moreno", "Bautista", "Valenzuela", "Guerra", "Aguirre", "Delgado", "Pacheco", "Gallardo", "Espino", "Mata", "Castañeda", "Rangel", "Becerra", "Dominguez", "Amaya", "Esparza", "Olivera", "Osorio", "Bustamante", "Rosales", "Aldrete", "Olivares", "Escamilla", "Delatorre", "Báez", "Arellano", "Pineda", "Cisneros", "Beltrán", "Medina", "Castañeda", "Duarte", "Mercado", "Verdugo", "Escobedo", "Cázares", "Mares", "Elizondo", "Benitez", "Calderón"]

    nombres_aleatorios = random.choices(nombres, k=10)
    apellidos_aleatorios = random.choices(apellidos, k=10)
        
    nombres_apellidos = list(zip(nombres_aleatorios, apellidos_aleatorios))

    with open("nombres_apellidos.csv","w",newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["nombre", "apellido"])
        for nombre in nombres_apellidos:
            writer.writerow(nombre)

    print("Archivo CSV generado con exito")
    #--------------------------------------------------------


def asignar_enfermedades(ciudadanos = Ciudadano):
    file_enfermedades = pd.read_csv("enfermedades.csv")
    enfermedades = file_enfermedades["Nombre"].tolist()
    
    n = random.randint(0,2)
    enfermedades_aleatorias = random.sample(enfermedades, k=n)
    for enfermedad in enfermedades_aleatorias:
        ciudadanos.set_enfermedades(enfermedad)
    return ciudadanos

    

def asignar_comunidad():
    comunidad_1 = Comunidad("comunidad_1")
    return comunidad_1

def asignar_contactos(lista_ciudadanos):
    
    ciudadanos_con_contactos = []
    for ciudadano in lista_ciudadanos:
        n = np.random.normal(2.0,4.0 )
        print(n)
        n = int(n)
        print(n)
        contactos = random.choices(lista_ciudadanos, k=n)
        print(contactos)
        for contacto in contactos:
            ciudadano.set_contactos(contacto)
        ciudadanos_con_contactos.append(ciudadano)
        
    return ciudadanos_con_contactos

def reorganizar_contactos(lista_ciudadanos):
    for ciudadano in lista_ciudadanos:
        for contacto in ciudadano.get_contactos():
            print(contacto)
            # if contacto.get_nombre() == ciudadano.get_nombre():
            #     ciudadano.set_contactos(contacto) 

    return lista_ciudadanos


#------------------Fin Ciudadano------------------

def contagiar():
    pass

def main():
    
    ciudadanos = crear_ciudadano()
if __name__ == "__main__":
    main()
