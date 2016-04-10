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
        drone.takeoff() #tell drone to take off
        time.sleep(7.5) #wait for drone to take off before giving more instructions
        
        drone.move(0,0,.5,0) #move the drone up at half speed
        time.sleep(6) #let drone increase height for 6 seconds





