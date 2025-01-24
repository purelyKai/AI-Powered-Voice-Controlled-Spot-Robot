import os
import time
import math
from spot_controller import SpotController
from groq_ai import getText, get_commands

class SpotCommands:
    def __init__(self, spot: SpotController) -> None:
        self.spot = spot
        self.sample_name = "command.wav"
        
    def forward(self):
        """Move forward by 1 meter."""
        self.spot.move_to_goal(goal_x=1, goal_y=0)
        print("Spot moved forward.")
        return

    def back(self):
        """Move backward by 1 meter."""
        self.spot.move_to_goal(goal_x=-1, goal_y=0)
        print("Spot moved backward.")
        return

    def turnLeft(self):
        """Turn left by 90 degrees."""
        self.spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=math.pi/2, cmd_duration=1)
        print("Spot turned left.")
        return

    def turnRight(self):
        """Turn right by 90 degrees."""
        self.spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=-math.pi/2, cmd_duration=1)
        print("Spot turned right.")
        return

    def bow(self, angle=math.radians(30)):
        """Make the robot bow with the specified angle."""
        self.spot.bow(pitch=angle, body_height=0.1, sleep_after_point_reached=2)
        print(f"Spot bowed at {math.degrees(angle)} degrees.")
        return

    def circleDance(self, radius=1, duration=10):
        """Make the robot walk in a circle with a given radius."""
        angular_velocity = 2 * math.pi / duration
        linear_velocity = radius * angular_velocity
        self.spot.move_by_velocity_control(v_x=linear_velocity, v_y=0.0, v_rot=angular_velocity, cmd_duration=duration)
        print(f"Spot performed a circle dance with radius {radius} meters.")
        return

    def sidestep(self, direction="left", steps=1, step_distance=0.5):
        """Sidestep to the left or right."""
        y_offset = step_distance if direction.lower() == "left" else -step_distance
        for _ in range(steps):
            self.spot.move_by_velocity_control(v_x=0.0, v_y=y_offset, v_rot=0.0, cmd_duration=1)
        print(f"Spot sidestepped {direction} {steps} step(s).")
        return

    def patrol(self, waypoints):
        """Navigate through a series of waypoints."""
        for waypoint in waypoints:
            x, y = waypoint
            self.spot.move_to_goal(goal_x=x, goal_y=y)
            time.sleep(2)
            print(f"Spot moved to waypoint: ({x}, {y}).")
        print("Spot finished patrolling.")
        return

    def lieDown(self):
        """Power off and make the robot lie down."""
        self.spot.power_off_sit_down()
        print("Spot powered off and lay down.")
        return

    def getCommands(self):
        """Capture and process audio to return recognized commands."""
        print("Start recording audio...")
        cmd = f'arecord -vv --format=cd --device={os.environ["AUDIO_INPUT_DEVICE"]} -r 48000 --duration=10 -c 1 {self.sample_name}'
        os.system(cmd)
        print("Audio recorded. Processing...")
        
        text = getText()
        commands = get_commands(text)
        os.system("pkill arecord")
        final_commands = commands.split()
        print(f"Recognized commands: {final_commands}")
        return final_commands
