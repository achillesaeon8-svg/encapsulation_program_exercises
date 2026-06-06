from fan_class import Fan

class FanOutcome(Fan):
    
    def __init__(self, speed=Fan.slow, radius=5, color='Blue', on=False):
        super().__init__(speed, radius, color, on)

    print('=' *50)
    print('=' *50)
    print('                 FAN 1 SPECIFICATIONS')
    print('=' *50)
    
    print(f'Speed: {first_fan.get_speed()}')
    print(f'Radius: {first_fan.get_radius()}')
    print(f'Color: {first_fan.get_color()}')
    print(f'Status Mode: {first_fan.get_on()}\n')

    print('=' *50)
    print('                 FAN 2 SPECIFICATIONS')
    print('=' *50)

    print(f'Speed: {second_fan.get_speed()}')
    print(f'Radius: {second_fan.get_radius()}')
    print(f'Color: {second_fan.get_color()}')
    print(f'Status Mode: {second_fan.get_on()}\n')
    print('=' *50)