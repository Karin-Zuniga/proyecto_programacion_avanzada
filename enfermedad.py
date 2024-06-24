class Enfermedad():
    def __init__(self):
        self.__nombre = ""
        self.__infeccion_probable = 0.0
        self.__promedio_pasos = 100000
        self.__enfermo = False
        self.__contador = 0

#--------------------get----------------
    def get_nombre(self):
        return self.__nombre

    def get_infeccion_probable(self):
        return self.__infeccion_probable
    
    def get_promedio_pasos(self):
        return self.__promedio_pasos
    
    def get_enfermo(self):
        return self.__enfermo
    
    def get_contador(self):
        return self.__contador
#--------------------set----------------

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
    
    def set_infeccion_probable(self, infeccion_probable):
        if isinstance(infeccion_probable, float):
            self.__infeccion_probable = infeccion_probable
    
    def set_promedio_pasos(self, promedio_pasos):
        if isinstance(promedio_pasos, int):
            self.__promedio_pasos = promedio_pasos
    
    def set_enfermo(self, enfermo):
        if isinstance(enfermo,bool):
            self.__enfermo = enfermo
    
    def set_contador(self, contador):
        if isinstance(contador, int):
            self.__contador
