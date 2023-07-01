class Pet:
    def __init__(self,name,animal,age):
        self.__name = name
        self.__animal = animal
        self.__age = age
    
    def set_name(self,new_name):
        self.__name = new_name

    def set_animal_type(self,new_animal_type):
        self.__animal = new_animal_type

    def set_age(self,new_age):
        self.__age = new_age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal
    
    def get_age(self):
        return self.__age