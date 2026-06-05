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
    
    def set_mode(self, on):
        self.__on = on

    def set_size(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color