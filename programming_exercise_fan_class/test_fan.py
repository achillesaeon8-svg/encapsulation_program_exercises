from fan_class import Fan
from fan_display_mechanics import FanOutcome

class FanSpecifications:
    
    first_fan = FanOutcome(speed=Fan.fast, radius=10, color='Yellow', on=True)
    second_fan = FanOutcome(speed=Fan.medium, radius=5, color='Blue', on=False)

    first_fan.fan_display_output(fan_number=1)
    second_fan.fan_display_output(fan_number=2)

if __name__ == '__main__':
    FanSpecifications()