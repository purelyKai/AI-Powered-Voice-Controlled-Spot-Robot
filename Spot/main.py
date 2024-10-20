import os
import time
from spot_controller import SpotController
# import cv2
from commands import *


ROBOT_IP = "192.168.80.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']


# def capture_image():
#     camera_capture = cv2.VideoCapture(0)
#     rv, image = camera_capture.read()
#     print(f"Image Dimensions: {image.shape}")
#     camera_capture.release()

    # // "image": "ghcr.io/otaberu/hackathon-spot-image:main",
def main():
    #example of using micro and speakers
    

    print("running3")
    # # Capture image

    time.sleep(2)
    # Use wrapper in context manager to lease control, turn on E-Stop, power on the robot and stand up at start
    # and to return lease + sit down at the end

    # with SpotController(username=SPOT_USERNAME, password=SPOT_PASSWORD, robot_ip=ROBOT_IP) as spot:
    #     spotCommander = SpotCommands(spot)
    #     spot.power_on_stand_up()

    #     time.sleep(1)
    #     spotCommander.openMic()
    #     time.sleep(10)
    #     spotCommander.closeMic()
    #     time.sleep(3)
        #move foward
        # spotCommander.foward()
        # time.sleep(1)
        #turn left
        # spotCommander.turnLeft()
        # time.sleep(1)
        # #turn right
        # spotCommander.turnRight()
        # time.sleep(1)


        





        # time.sleep(2)
        # capture_image()
        # # Move head to specified positions with intermediate time.sleep
        # spot.move_head_in_points(yaws=[0.2, 0],
        #                          pitches=[0.3, 0],
        #                          rolls=[0.4, 0],
        #                          sleep_after_point_reached=1)
        # capture_image()
        # time.sleep(3)
        # spot.move_head_in_points(yaws=[-0.2, 0],
        #                     pitches=[-0.3, 0],
        #                     rolls=[-0.4, 0],
        #                     sleep_after_point_reached=1)
        # time.sleep(2)
        # spot.move_head_in_points(yaws=[0, 0.2],
        #                     pitches=[0, 0.3],
        #                     rolls=[0, 0.4],
        #                     sleep_after_point_reached=1)
        
        # # Make Spot to move by goal_x meters forward and goal_y meters left
        # spot.move_to_goal(goal_x=1.0, goal_y=0)
        # time.sleep(3)
        # capture_image()

        # # Control Spot by velocity in m/s (or in rad/s for rotation)
        # # spot.move_by_velocity_control(v_x=-0.3, v_y=0, v_rot=0, cmd_duration=2)
        # spot.dust_off(yaws=[0.2, 0], pitches=[0.3, 0], rolls=[0.4, 0])
        # capture_image()
        # time.sleep(3)


if __name__ == '__main__':
    main()
