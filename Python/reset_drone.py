import time
import ps_drone

#make drone object
drone = ps_drone.Drone()

#Connect to the drone
drone.startup()

#Reset drone from bad state
drone.reset()
