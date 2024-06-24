from comunidad import Comunidad
from enfermedad import Enfermedad
from ciudadano import Ciudadano

import numpy as np
import pandas as pd
import csv
import random






def crear_enfermedad():
    pass

#-----------------------Ciudadano-----------------

def crear_ciudadano():

    n = 100
    file_nombres = pd.read_csv("nombres_apellidos.csv")

    nombre_apellido = pd.DataFrame(file_nombres).to_numpy()
    rows = nombre_apellido.shape[0]

    archivo = []
    
    for nombre,apellido in nombre_apellido:
        ciudadano = Ciudadano( n, nombre +" "+ apellido, asignar_comunidad())
        archivo.append([ciudadano.get_id(), ciudadano.get_nombre_apellido(), ciudadano.get_enfermedad(), ciudadano.get_comunidad(), ciudadano.get_contactos(), ciudadano.get_estado()])
        n +=1 

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


def asignar_enfermedades():
    return []

def asignar_comunidad():
    comunidad_1 = Comunidad()
    return comunidad_1

def asignar_contactos():
    pass

#------------------Fin Ciudadano------------------

def contagiar():
    pass

def main():
    nombre = crea_nombres()
    ciudadanos = crear_ciudadano()

if __name__ == "__main__":
    main()
