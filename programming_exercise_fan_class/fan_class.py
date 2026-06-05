class Fan:
    
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, radius=5, color='Blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = float(radius)
        self.__color = color