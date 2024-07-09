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

def crear_ciudadano(comunidad_1):

    n = 100
    file_nombres = pd.read_csv("nombres_apellidos.csv")
    nombres = pd.DataFrame.sample(file_nombres, comunidad_1.get_num_ciudadanos())
    nombre_apellido = pd.DataFrame(nombres).to_numpy()

    archivo = []
    
    lista_ciudadanos = []
    for nombre,apellido in nombre_apellido:
        ciudadano = Ciudadano( n, nombre +" "+ apellido, comunidad_1)

        #ciudadano = asignar_enfermedades(ciudadano)
        lista_ciudadanos.append(ciudadano)
        n +=1 
    lista_ciudadanos = asignar_contactos(lista_ciudadanos,comunidad_1)

        
    #lista_ciudadanos = reorganizar_contactos(lista_ciudadanos)
    for ciudadano in lista_ciudadanos:
        lista_contactos = []
        for contacto in ciudadano.get_contactos():
           lista_contactos.append(contacto.get_nombre_apellido())
        archivo.append([ciudadano.get_id(), ciudadano.get_nombre_apellido(), ciudadano.get_enfermedad(), ciudadano.get_comunidad(), lista_contactos, ciudadano.get_estado()])
    headers = ["ID","Nombre", "enfermedades", "Comunidad", "Contactos", "Estado"]

    df = pd.DataFrame(archivo, columns=headers)
    df.to_csv("ciudadano.csv")
    print("Archivo CSV generado con exito")
    return lista_ciudadanos
    

        
        #----creando lista con nombres y apellidos----
def crea_nombres():
    nombres = ["Ana", "Juan", "María", "Carlos", "Laura", "José", "Andrea", "David", "Sofía", "Alejandro", "Claudia", "Pedro", "Gabriela", "Fernando", "Natalia", "Luis", "Valeria", "Miguel", "Paola", "Jorge", "Daniela", "Ricardo", "Andrea", "Javier", "Adriana", "Diego", "Patricia", "Manuel", "Vanessa", "Marco", "Verónica", "Martín", "Carolina", "Óscar", "Pamela", "Eduardo", "Angélica", "Sergio", "Brenda", "Juan Carlos", "Esther", "Raúl", "Silvia", "Antonio", "Victoria", "Alan", "Diana", "Salvador", "Rosa", "Juan Pablo", "Elena", "Mario", "Lorena", "Israel", "Alma", "Héctor", "Mariana", "Gabriel", "Vanessa", "Guillermo", "Susana", "Roberto", "Ana María", "Ernesto", "Ana Laura", "Emilio", "Cecilia", "Arturo", "Luz", "Omar", "Alejandra", "Octavio", "Estela", "Ignacio", "Laura Elena", "Hugo", "Carmen", "Jorge Luis", "Alma Rosa", "Ángel", "Adrián", "Teresa", "Francisco", "Lorena", "Raúl", "Alma Delia", "Víctor", "Rosario", "Rubén", "Andrea", "Francisco Javier", "Margarita", "Efraín", "Martha", "Julio", "Ana Karen", "René", "Isabel", "Armando", "Patricia", "Leopoldo", "Inés", "Salvador", "Claudia Patricia", "Mauricio", "Brenda", "Víctor Manuel", "Alicia", "Federico", "Daniela", "Agustín", "Verónica", "Eduardo", "Carmen"]
    apellidos = ["Martínez", "González", "Rodríguez", "López", "Hernández", "Pérez", "Sánchez", "Ramírez", "Torres", "Flores", "Gómez", "Díaz", "Reyes", "Morales", "Ortiz", "Castro", "Ruiz", "Chávez", "Vásquez", "Ramos", "Álvarez", "Jiménez", "Fernández", "Gutiérrez", "Mendoza", "Soto", "Aguilar", "Silva", "Romero", "Mendoza", "Chavez", "Juárez", "Guerrero", "Palacios", "Maldonado", "Pinto", "Rojas", "Molina", "Salazar", "Herrera", "Vega", "Vargas", "Cortés", "Navarro", "Peña", "Luna", "Cruz", "León", "Campos", "Cabrera", "Montes", "Zamora", "Acosta", "Orozco", "Quintero", "Ibarra", "Escobar", "Barajas", "Guerrero", "Santana", "Miranda", "Espinoza", "Valencia", "Barrera", "Figueroa", "Lara", "Cervantes", "Moreno", "Bautista", "Valenzuela", "Guerra", "Aguirre", "Delgado", "Pacheco", "Gallardo", "Espino", "Mata", "Castañeda", "Rangel", "Becerra", "Dominguez", "Amaya", "Esparza", "Olivera", "Osorio", "Bustamante", "Rosales", "Aldrete", "Olivares", "Escamilla", "Delatorre", "Báez", "Arellano", "Pineda", "Cisneros", "Beltrán", "Medina", "Castañeda", "Duarte", "Mercado", "Verdugo", "Escobedo", "Cázares", "Mares", "Elizondo", "Benitez", "Calderón"]

    nombres_aleatorios = random.choices(nombres, k=1000000)
    apellidos_aleatorios = random.choices(apellidos, k=100000)
        
    nombres_apellidos = list(zip(nombres_aleatorios, apellidos_aleatorios))

    with open("nombres_apellidos.csv","w",newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["nombre", "apellido"])
        for nombre in nombres_apellidos:
            writer.writerow(nombre)

    print("Archivo CSV generado con exito")
    #--------------------------------------------------------


# def asignar_enfermedades(ciudadanos):
#     file_enfermedades = pd.read_csv("enfermedades.csv")
#     enfermedades = file_enfermedades["Nombre"].tolist()
    
#     n = random.randint(0,2)
#     enfermedades_aleatorias = random.sample(enfermedades, k=n)
#     for enfermedad in enfermedades_aleatorias:
#         ciudadanos.set_enfermedades(enfermedad)
#     return ciudadanos

    

def crear_comunidad():
    comunidad_1 = Comunidad("comunidad_1")
    comunidad_1.set_num_ciudadanos(1000)
    comunidad_1.set_num_infectados(0)
    comunidad_1.set_probabilidad_conexion_fisica(0.7)
    comunidad_1.set_promedio_conexion_fisica(5.0)

    return comunidad_1

def asignar_contactos(lista_ciudadanos, comunidad_1):
    
    ciudadanos_con_contactos = []
    for ciudadano in lista_ciudadanos:
        lista = []
        for persona in lista_ciudadanos:
            if persona !=ciudadano:
                lista.append(persona)

        n = np.random.normal(comunidad_1.get_promedio_conexion_fisica(),1.0)
        n = int(n)
        if n<0:
            n = n*(-1)
        while n >= comunidad_1.get_num_ciudadanos():
            n = n-1


        contactos = random.sample(lista, k=n)
        
        for contacto in contactos:
            ciudadano.set_contactos(contacto)
        ciudadanos_con_contactos.append(ciudadano)
        
    return ciudadanos_con_contactos

# def reorganizar_contactos(lista_ciudadanos):
#     for ciudadano in lista_ciudadanos:
#         print(ciudadano.get_nombre_apellido())
        
#         for contacto in ciudadano.get_contactos():
#             for persona in contacto.get_contactos():
#             #    print(persona.get_nombre_apellido())
#                 if persona.get_nombre_apellido() == ciudadano.get_nombre_apellido():  
#                     print(persona.get_nombre_apellido())  
#                     contacto.set_contactos(ciudadano)
#                     print(persona.get_contactos()[-1].get_nombre_apellido())
                   
#                 else:
#                     print("no se repite")
#             # if contacto.get_nombre() == ciudadano.get_nombre():
#             #           #     ciudadano.set_contactos(contacto) 
        
#     return lista_ciudadanos


#------------------Fin Ciudadano------------------

def paciente_0(lista_ciudadanos):
    virus = Enfermedad("virus",0.3,2)
    lista_ciudadanos[-1].set_enfermedades(virus)
    lista_ciudadanos[-1].set_estado(2)
    lista_ciudadanos[-1].set_etapa_enfermedad(virus.get_promedio_pasos())
    return lista_ciudadanos,virus



def contagiar(lista_ciudadanos,virus,comunidad):
    for ciudadano in lista_ciudadanos:        
        if ciudadano.get_estado() == 2:

            contacto_estrecho = []
            for contacto in ciudadano.get_contactos():
                seleccion = np.random.choice([True, False], p=[comunidad.get_probabilidad_conexion_fisica(), 1-comunidad.get_probabilidad_conexion_fisica()])
                if seleccion == True:
                    contacto_estrecho.append(contacto)
                for persona in contacto_estrecho:
                    if persona.get_estado() == 1:
                        a = virus.get_infeccion_probable()
                        b = (1 - virus.get_infeccion_probable())
                        valor = [1,2]
                        infeccion = np.random.choice(valor, 1, p=(b,a))

                        contacto.set_estado(infeccion[0])
                        
                        if contacto.get_estado() == 2:
                            contacto.set_enfermedades(virus)
                            num_infectados = comunidad.get_num_infectados() + 1
                            comunidad.set_num_infectados(num_infectados)
                            contacto.set_etapa_enfermedad(virus.get_promedio_pasos())
                            
                        
                            

    return lista_ciudadanos           

def recuperarse(lista_ciudadanos):
    for ciudadano in lista_ciudadanos:
        if ciudadano.get_estado() == 2:
            etapa = ciudadano.get_etapa_enfermedad() - 1
            ciudadano.set_etapa_enfermedad(etapa)
            if ciudadano.get_etapa_enfermedad() == 0:
                ciudadano.set_estado(3)
                
    return lista_ciudadanos

def mostrar_info(lista_ciudadano, comunidad):
    sanos = 0
    enfermos = 0
    inmunes = 0
    
    for ciudadano in lista_ciudadano:
        if ciudadano.get_estado() == 1:
            sanos = sanos + 1
        elif ciudadano.get_estado() == 2:
            enfermos = enfermos + 1
        else:
            inmunes = inmunes + 1
    comunidad.set_num_infectados(enfermos)
    print(f"De {comunidad.get_num_ciudadanos()} ciudadanos en la comunidad {comunidad.get_nombre()} hay {enfermos} enfermos")
    

def main():
    crea_nombres()
    comunidad_1 = crear_comunidad()
    ciudadanos = crear_ciudadano(comunidad_1)
    contador = 0
    ciudadanos,virus = paciente_0(ciudadanos)
    
    while contador < 1000:
        mostrar_info(ciudadanos,comunidad_1)
        ciudadanos = recuperarse(ciudadanos)
        ciudadanos = contagiar(ciudadanos, virus, comunidad_1)
        contador +=1


if __name__ == "__main__":
    main()

