import time
from spot_controller import SpotController
from commands import *
# import cv2

ROBOT_IP = "192.168.80.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']

def main():
    print("running3")
    time.sleep(2)

    with SpotController(username=SPOT_USERNAME, password=SPOT_PASSWORD, robot_ip=ROBOT_IP) as spot:
        spotCommander = SpotCommands(spot)
        spot.power_on_stand_up()

        time.sleep(1)
        spotCommander.back()
        time.sleep(2)

        commands = spotCommander.getCommands()

        time.sleep(1)
        spotCommander.forward()
        time.sleep(2)
        #sample_name = "taunt.wav"
        for command in commands:
            if "forward" in command:
                print("Playing sound")
                #os.system(f"ffplay -nodisp -autoexit -loglevel quiet volume=2.0 {sample_name}")
                time.sleep(2)
                spotCommander.forward()
            elif "back" in command:
                print("Playing sound")
                #os.system(f"ffplay -nodisp -autoexit -loglevel quiet volume=2.0 {sample_name}")
                time.sleep(2)
                spotCommander.back()
            elif "turnLeft" in command:
                print("Playing sound")
                #os.system(f"ffplay -nodisp -autoexit -loglevel quiet volume=2.0 {sample_name}")
                time.sleep(2)
                spotCommander.turnLeft()
            elif "turnRight" in command:
                print("Playing sound")
                #os.system(f"ffplay -nodisp -autoexit -loglevel quiet volume=2.0 {sample_name}")
                time.sleep(2)
                spotCommander.turnRight()
            else:
                continue
            time.sleep(2)

if __name__ == '__main__':
    main()
