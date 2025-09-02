import time


# TrafficLight class to represent the actual traffic light
class TrafficLight:
    def __init__(self):
        self.color = "Red"

    def set_color(self, color):
        self.color = color
        print(f"Traffic Light is now {self.color}")


# Define command functions
def red_light_command(traffic_light):
    traffic_light.set_color("Red")


def green_light_command(traffic_light):
    traffic_light.set_color("Green")


def yellow_light_command(traffic_light):
    traffic_light.set_color("Yellow")


def emergency_command(traffic_light):
    traffic_light.set_color("Red")  # Keep all lights red during emergency


# Define state functions
def red_light(controller):
    controller.red_command(controller.traffic_light)
    time.sleep(3)
    controller.state = green_light


def green_light(controller):
    controller.green_command(controller.traffic_light)
    time.sleep(3)
    controller.state = yellow_light


def yellow_light(controller):
    controller.yellow_command(controller.traffic_light)
    time.sleep(3)
    controller.state = red_light


def emergency_state(controller):
    controller.emergency_command(controller.traffic_light)
    time.sleep(3)
    # Stay in emergency state until deactivated


# Controller class
class TrafficLightController:
    def __init__(self):
        self.traffic_light = TrafficLight()  # The actual traffic light

        # Initialize with command functions
        self.red_command = red_light_command
        self.green_command = green_light_command
        self.yellow_command = yellow_light_command
        self.emergency_command = emergency_command

        self.state = red_light  # Initial state

    def change_light(self):
        self.state(self)

    def activate_emergency(self):
        print("Activating Emergency Mode")
        self.state = emergency_state

    def deactivate_emergency(self):
        print("Deactivating Emergency Mode")
        self.state = red_light


# Client code
if __name__ == "__main__":
    controller = TrafficLightController()

    # Simulate normal operation
    for _ in range(3):
        controller.change_light()

    # Activate emergency mode
    controller.activate_emergency()
    for _ in range(2):
        controller.change_light()

    # Deactivate emergency mode and resume normal operation
    controller.deactivate_emergency()
    for _ in range(3):
        controller.change_light()
