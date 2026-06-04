from car_class import Car

class CarDyanmics:
    def __init__(self):
        cool_car_data = ('Mclaren', '2017')
        car_results = Car(cool_car_data[1], cool_car_data[0])

        print(f'Car Created: {cool_car_data[1]} ({cool_car_data[0]})')
        print(f'Starting Speed: {car_results.speed()} km/h.')

        car_results.acceleration()
        car_results.brake()

if __name__ == '__main__':
    CarDyanmics()