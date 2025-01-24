import time
from spot_controller import SpotController
from commands import SpotCommands

ROBOT_IP = "192.168.80.3"  # Replace with actual robot IP
SPOT_USERNAME = "admin"    # Replace with Spot username
SPOT_PASSWORD = "2zqa8dgw7lor"  # Replace with Spot password

def main():
    print("Initializing Spot...")
    time.sleep(2)

    with SpotController(username=SPOT_USERNAME, password=SPOT_PASSWORD, robot_ip=ROBOT_IP) as spot:
        spotCommander = SpotCommands(spot)
        spot.power_on_stand_up()
        print("Spot powered on and standing.")

        try:
            while True:
                print("Awaiting commands...")
                commands = spotCommander.getCommands()

                for command in commands:
                    if "forward" in command:
                        spotCommander.forward()
                    elif "back" in command:
                        spotCommander.back()
                    elif "turnLeft" in command:
                        spotCommander.turnLeft()
                    elif "turnRight" in command:
                        spotCommander.turnRight()
                    elif "bow" in command:
                        spotCommander.bow()
                    elif "circleDance" in command:
                        spotCommander.circleDance(radius=1, duration=5)
                    elif "lieDown" in command:
                        spotCommander.lieDown()
                        break
                    elif "sidestep" in command:
                        direction = "left" if "left" in command else "right"
                        spotCommander.sidestep(direction=direction, steps=2)
                    elif "patrol" in command:
                        waypoints = [(1, 0), (2, 2), (0, 2)]  # Example waypoints
                        spotCommander.patrol(waypoints=waypoints)
                    else:
                        print(f"Unknown command: {command}")
                time.sleep(2)

        except KeyboardInterrupt:
            print("Shutting down...")
            spot.power_off_sit_down()
            print("Spot is powered off.")

if __name__ == "__main__":
    main()
