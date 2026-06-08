from fan_class import Fan

class FanOutcome(Fan):
    
    def __init__(self, speed=Fan.slow, radius=5, color='Blue', on=False):
        super().__init__(speed, radius, color, on)

    def fan_display_output(self, fan_number):

        colors = { 
            
            'Yellow': '\033[93m',
            'Blue': '\033[94m',
            'Normal': '\033[0m'
        }
        
        color_code = colors.get(self.get_color(), '\033[97m')
        reset_color = colors['Normal']

        print('=' *50)       
        print(f'                FAN {fan_number} SPECIFICATIONS')
        print('=' *50)
        
        print(f'Speed: {self.get_speed()}')
        print(f'Radius: {self.get_radius()}')
        print(f'Color: {color_code}{self.get_color()}{reset_color}')
        print(f'Status Mode: {self.get_on()}')

        print('=' *50)
