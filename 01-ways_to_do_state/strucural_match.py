import time
from dataclasses import dataclass


# Define states using dataclasses
@dataclass
class RedLight:
    pass


@dataclass
class GreenLight:
    pass


@dataclass
class YellowLight:
    pass


# Context class
class TrafficLight:
    def __init__(self):
        self.state = RedLight()  # Initial state

    def change_light(self):
        match self.state:
            case RedLight():
                print("Red Light - Stop")
                time.sleep(3)
                self.state = GreenLight()
            case GreenLight():
                print("Green Light - Go")
                time.sleep(3)
                self.state = YellowLight()
            case YellowLight():
                print("Yellow Light - Caution")
                time.sleep(3)
                self.state = RedLight()


# Client code
if __name__ == "__main__":
    traffic_light = TrafficLight()

    # Simulate the traffic light cycle
    for _ in range(6):  # Run the cycle a few times
        traffic_light.change_light()
