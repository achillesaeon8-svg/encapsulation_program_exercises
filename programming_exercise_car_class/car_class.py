class Car:

    def __init__(self):
        self.__year_model = year_model
        self.__make = car_brand
        self.__speed = 0

    cool_car = ('Mclaren', '2017')

    def speed(self):
        return self.__speed
    
    def acceleration(self):
        print('Accelerating: ')
        for acceleration in range(5):
            self.cool_car.accelerate()
            current_speed = self.cool_car.get_speed()
            print(current_speed)

    def brake(self):
        print('Braking: ')
        for deceleration in range (5):
            self.cool_car.decelerate()
            current_speed = self.cool_car.slowing_down()
            print(current_speed)