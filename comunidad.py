from enfermedad import Enfermedad

class Comunidad():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__num_ciudadanos = 0
        self.__promedio_conexion_fisica = 0.0
        self.__enfermedad = ""
        self.__num_infectados = 0
        self.__probabilidad_conexion_fisica = 0.0


    #-------------------get--------------------
    def get_nombre(self):
        return self.__nombre
    
    def get_num_ciudadanos(self):
        return self.__num_ciudadanos


    def get_promedio_conexion_fisica(self):
        return self.__promedio_conexion_fisica



    def get_enfermedad(self):
        return self.__enfermedad


    def get_num_infectados(self):
        return self.__num_infectados


    def get_probabilidad_conexion_fisica(self):
        return self.__probabilidad_conexion_fisica

    #-------------------set--------------------

    def set_num_ciudadanos(self, num_ciudadanos):
        if isinstance(num_ciudadanos, int):
            self.__num_ciudadanos = num_ciudadanos


    def set_promedio_conexion_fisica(self, promedio_conexion_fisica):
        if isinstance(promedio_conexion_fisica, float):
            self.__promedio_conexion_fisica = promedio_conexion_fisica



    def set_enfermedad(self, enfermedad):
        if isinstance(enfermedad,Enfermedad):
            self.__enfermedad = enfermedad


    def set_num_infectados(self, num_infectados):
        if isinstance(num_infectados, int):
           self.__num_infectados = num_infectados


    def set_probabilidad_conexion_fisica(self, probabilidad_conexion_fisica):
        if isinstance(probabilidad_conexion_fisica, float):
            self.__probabilidad_conexion_fisica = probabilidad_conexion_fisica

