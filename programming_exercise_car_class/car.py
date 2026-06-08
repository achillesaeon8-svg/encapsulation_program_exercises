from car_class import Car
from car_display_mechanics import CarOutcome

class CarDyanmics:
    def __init__(self):
        cool_car_data = ('Mclaren 720s', '2017')
        car_results = CarOutcome(cool_car_data[1], cool_car_data[0])

        car_results.car_display_output()

        car_results.acceleration()
        car_results.brake()

if __name__ == '__main__':
    CarDyanmics()