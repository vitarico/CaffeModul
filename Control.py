import time
import ps_drone
import cv2
def dronestart():
    drone = ps_drone.Drone()  # Start using drone
    drone.startup()  # Connects to drone and starts subprocesses
    drone.printBlue("Connected to Drone")
    drone.reset()  # Always good, at start


    while drone.getBattery()[0] == -1:    time.sleep(0.1)  # Waits until the drone has done its reset
    time.sleep(0.5)  # Give it some time to fully awake

    drone.printBlue("Battery: " + str(drone.getBattery()[0]) + "%  " + str(drone.getBattery()[1]))  # Gives a battery-status
    return drone
def keycontroller(drone,key):
    if key == " ":
        if drone.NavData["demo"][0][2] and not drone.NavData["demo"][0][3]:
            #drone.takeoff()
            print "takeoff"
        else:
            #drone.land()
            print "land"
    elif key == "0":
        drone.hover()
    elif key == "w":
        drone.moveForward()
    elif key == "s":
        drone.moveBackward()
    elif key == "a":
        drone.moveLeft()
    elif key == "d":
        drone.moveRight()
    elif key == "q":
        drone.turnLeft()
    elif key == "e":
        drone.turnRight()
    elif key == "7":
        drone.turnAngle(-10, 1)
    elif key == "9":
        drone.turnAngle(10, 1)
    elif key == "4":
        drone.turnAngle(-45, 1)
    elif key == "6":
        drone.turnAngle(45, 1)
    elif key == "1":
        drone.turnAngle(-90, 1)
    elif key == "3":
        drone.turnAngle(90, 1)
    elif key == "8":
        drone.moveUp()
    elif key == "2":
        drone.moveDown()
    elif key == "*":
        drone.doggyHop()
    elif key == "+":
        drone.doggyNod()
    elif key == "-":
        drone.doggyWag()

#Step 1: Initalisiere Drone
drone=dronestart()
#Set Drone Default Speed Settings
drone.setSpeed(0.2)

#Starts the Video Stream
#drone.startVideo()
#drone.showVideo()
#time.sleep(5)

Running = True
while Running:
    print "In Control Loop"


    #Get Pictures to put in the Model
    cap=drone.VideoImage
    cap = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)
    cv2.imshow("Frame", cap)
    cv2.imwrite("frontd.png", cap)

    #Call The Classification Funktion here !
    DirectionClass=1


    #Controll via Classified Data
    #Sleep defines the inertia time
    Sleep = 0.5

    if DirectionClass == 0:
        drone.moveForward()
        print "Forward"
        time.sleep(Sleep)
        drone.stop()
    elif DirectionClass == 1:
        drone.turnRight()
        print "Turing Right"
        time.sleep(Sleep)
        drone.stop()
    elif DirectionClass == 2:
        drone.turnLeft()
        print "Turning Left"
        time.sleep(Sleep)
        drone.stop()
    elif DirectionClass == 3:
        drone.turnLeft()
        print "No Goal in Sight"
        time.sleep(Sleep)
        drone.stop()
    else:
        drone.hover()

    #Default Controller via Keys in the Terminal !
    key = drone.getKey()
    keycontroller(drone,key)