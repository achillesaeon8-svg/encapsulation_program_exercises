from fan_class import Fan

class FanSpecifications:
    
    first_fan = Fan()

    first_fan.set_speed(Fan.fast)
    first_fan.set_radius(10)
    first_fan.set_color('yellow')
    first_fan.set_on(on=True)

    second_fan = Fan()

    second_fan.set_speed(Fan.medium)
    second_fan.set_radius(5)
    second_fan.set_color(color='Blue')
    second_fan.set_on(on=False)

    print('FAN 1 SPECIFICATIONS')
    print(f'Speed: {first_fan.get_speed()}')
    print(f'Radius: {first_fan.get_radius()}')
    print(f'Color: {first_fan.get_color()}')
    print(f'Status Mode: {first_fan.get_on()}\n')

    print('FAN 2 SPECIFICATIONS')
    print(f'Speed: {second_fan.get_speed()}')
    print(f'Radius: {second_fan.get_radius()}')
    print(f'Color: {second_fan.get_color()}')
    print(f'Status Mode: {second_fan.get_on()}\n')

if __name__ == '__main__':
    FanSpecifications()