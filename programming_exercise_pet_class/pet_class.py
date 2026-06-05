class Pet:
    
    def __init__(self):
        self.__name = ' '
        self.__animal_type = ' '
        self.__age = 0

    def set_name(self, pet_name):
        self.__name = pet_name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, pet_age):
        self.__age = pet_age