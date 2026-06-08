from car_class import Car

class CarOutcome(Car):
    
    def __init__(self, year_model, car_brand):
        super().__init__(year_model, car_brand)

    def car_display_output(self):
        print('=' * 60)
        print(f'             Car Year & Model: {self.get_year_model()} {self.get_car_brand()}')
        print('=' * 60)

        print(f'Starting Speed: {self.speed()} km/h.\n')