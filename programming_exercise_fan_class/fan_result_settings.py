from fan_class import Fan

class FanOutcome(Fan):
    
    def __init__(self, speed=Fan.slow, radius=5, color='Blue', on=False):
        super().__init__(speed, radius, color, on)