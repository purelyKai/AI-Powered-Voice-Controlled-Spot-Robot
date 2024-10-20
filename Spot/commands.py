import os
import time
from spot_controller import SpotController
import math
from groq_ai import *
from stt import *
# import cv2

ROBOT_IP = "192.168.80.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']

class SpotCommands:
    def __init__(self, spot: SpotController) -> None:
        self.spot = spot
        self.mic_process = None
        self.sample_name = "command.wav"
        
    def forward(self):
        self.spot.move_to_goal(goal_x=1, goal_y=0)
        return

    def back(self):
        self.spot.move_to_goal(goal_x=-1, goal_y=0)
        return

    def turnLeft(self):
        self.spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=math.pi/2, cmd_duration=1)
        return

    def turnRight(self):
        self.spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=-math.pi/2, cmd_duration=1)
        return

    def getCommands(self):
        
        print("Start recording audio")
        sample_name = "command.wav"
        cmd = f'arecord -vv --format=cd --device={os.environ["AUDIO_INPUT_DEVICE"]} -r 48000 --duration=5 -c 1 {sample_name}'
        print(cmd)
        os.system(cmd)
        time.sleep(5)

        #API CALL TO DEEPGRAM HERE
        text = getText()
        commands = get_commands(text)
        time.sleep(5)
        os.system("pkill arecord")
        final_commands = commands.split()
        return final_commands
