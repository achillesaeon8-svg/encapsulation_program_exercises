class Fan:
    
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, radius=5, color='Blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = float(radius)
        self.__color = color

    def set_speed(self, speed):
        self.__speed = speed
    
    def set_on(self, on):
        self.__on = on

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def get_speed(self):
        return self.__speed
    
    def get_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color