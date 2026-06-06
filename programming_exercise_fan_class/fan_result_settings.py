from fan_class import Fan

class FanOutcome(Fan):
    
    def __init__(self, speed=Fan.slow, radius=5, color='Blue', on=False):
        super().__init__(speed, radius, color, on)

    def fan_display_output(self, fan_number):
        
        print('=' *50)       
        print(f'                 {fan_number} SPECIFICATIONS')
        print('=' *50)
        
        print(f'Speed: {self.get_speed()}')
        print(f'Radius: {self.get_radius()}')
        print(f'Color: {self.get_color()}')
        print(f'Status Mode: {self.get_on()}')

        print('=' *50)
