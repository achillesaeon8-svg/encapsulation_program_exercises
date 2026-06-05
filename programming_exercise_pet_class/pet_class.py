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

    def get_name(self, input_name):
        return self.__name

    def get_animal_type(self, input_animal_type):
        return self.__animal_type

    def get_age(self, input_age):
        return self.__age