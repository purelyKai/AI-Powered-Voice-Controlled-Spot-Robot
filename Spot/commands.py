import os
import time
from spot_controller import SpotController
import math
# import cv2

ROBOT_IP = "192.168.80.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']


def foward(spot: SpotController):
    spot.move_to_goal(goal_x=.5, goal_y=0)
    return

def turnLeft(spot: SpotController):
    spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=math.pi/2, cmd_duration=2)
    return

def turnRight(spot: SpotController):
    spot.move_by_velocity_control(v_x=0.0, v_y=0.0, v_rot=-math.pi/2, cmd_duration=2)
    return

