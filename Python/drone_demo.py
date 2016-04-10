import time
import ps_drone



class DroneDemo:
    
    #Initialize drone
    drone = ps_drone.Drone()
    
    #Initialize DroneDemo, startup drone, tell it to take off and fly
    def __init__(self, location):
        this.location = location
        drone.startup()
        drone.reset()
        self.flyDrone()

    def flyDrone(self):
        end = False
        print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])
        drone.takeoff()
        time.sleep(7.5)






