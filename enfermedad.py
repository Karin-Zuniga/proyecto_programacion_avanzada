class Enfermedad():
    def __init__(self, nombre, inf_prob, pasos):
        self.__nombre = nombre
        self.__infeccion_probable = inf_prob
        self.__promedio_pasos = pasos
        self.__contador = 0

#--------------------get----------------
    def get_nombre(self):
        return self.__nombre

    def get_infeccion_probable(self):
        return self.__infeccion_probable
    
    def get_promedio_pasos(self):
        return self.__promedio_pasos
    
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
    
    
    def set_contador(self, contador):
        if isinstance(contador, int):
            self.__contador
