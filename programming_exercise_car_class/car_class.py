class Car:
# →
    def __init__(self):
        self.__year_model = year_model
        self.__make = car_brand
        self.__speed = 0

    cool_car = ('Mclaren', '2017')

    def speed(self):
        return self.__speed
    
    def acceleration(self):
        print('Accelerating: ')
        for count in range(5):
            self.__speed += 5
            print(f'Current Speed: {self.get_speed()} km/h.')

    def brake(self):
        print('Braking: ')
        for count in range(5):
            if self.__speed >= 5:
                self.__speed -= 5
            else: 
                self.__speed = 0
            print(f'Current Speed: {self.get_speed()} km/h.')