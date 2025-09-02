import time
from abc import ABC, abstractmethod


# State interface
class TrafficLightState(ABC):
    @abstractmethod
    def change(self, traffic_light):
        pass


# Concrete State for Red Light
class RedLight(TrafficLightState):
    def change(self, traffic_light):
        print("Red Light - Stop")
        time.sleep(3)
        traffic_light.state = GreenLight()


# Concrete State for Green Light
class GreenLight(TrafficLightState):
    def change(self, traffic_light):
        print("Green Light - Go")
        time.sleep(3)
        traffic_light.state = YellowLight()


# Concrete State for Yellow Light
class YellowLight(TrafficLightState):
    def change(self, traffic_light):
        print("Yellow Light - Caution")
        time.sleep(3)
        traffic_light.state = RedLight()


# Context class
class TrafficLight:
    def __init__(self, state: TrafficLightState):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: TrafficLightState):
        print(f"Transitioning to {state.__class__.__name__}")
        self._state = state

    def change_light(self):
        self._state.change(self)


# Client code
if __name__ == "__main__":
    # Initialize traffic light with the red light state
    traffic_light = TrafficLight(RedLight())

    # Simulate the traffic light cycle
    for _ in range(6):  # Run the cycle a few times
        traffic_light.change_light()