import os
import time
from spot_controller import SpotController
import math
import subprocess


# import cv2

ROBOT_IP = "192.168.80.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']

class SpotCommands:
    def __init__(self, spot: SpotController) -> None:
        self.spot = spot
        self.micProcess = None
    def foward(self):
        self.spot.move_to_goal(goal_x=.5, goal_y=0)
        return

    def back(self):
        self.spot.move_to_goal(goal_x=-.5, goal_y=0)
        return

    def turnLeft(self):
        self.spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=math.pi/2, cmd_duration=1)
        return

    def turnRight(self):
        self.spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=-math.pi/2, cmd_duration=1)
        return

    def openMic(self):
        sample_name = "command.wav"
        cmd = f'arecord -vv --format=cd --device={os.environ["AUDIO_INPUT_DEVICE"]} -r 48000 --duration=10 -c 1 {sample_name}'
        cmd = ['arecord', '-vv', '--format=cd', '--device=default', '-r', '48000', '--duration=10', '-c', '1', sample_name]
        # Start the microphone process
        self.micProcess = subprocess.Popen(cmd)
        print("Spot is listening...")

    def closeMic(self):
        if self.mic_process is not None:
            self.mic_process.terminate()  # Terminate the recording process
            self.mic_process  = None
            print("Spot stopped listening.")
        else:
            print("No active microphone recording.")
        


