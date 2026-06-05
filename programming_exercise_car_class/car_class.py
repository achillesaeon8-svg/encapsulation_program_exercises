class Car:

    def __init__(self, year_model, car_brand):
        self.__year_model = year_model
        self.__make = car_brand
        self.__speed = 0

    def speed(self):
        return self.__speed
    
    def acceleration(self):
        print('Accelerating: \n')
        for count in range(5):
            self.__speed += 5
            print(f'Current Speed: {self.speed()} km/h.')

        print('=' * 60)

    def brake(self):
        print('Braking: \n')
        for count in range(5):
            if self.__speed >= 5:
                self.__speed -= 5
            else: 
                self.__speed = 0
            print(f'Current Speed: {self.speed()} km/h.')

        print('=' * 60)