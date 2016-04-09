# #######################
# Code for the Sudo
# Hacks Drone Drop System
# #######################

import time                     # imports the time library
import ps_drone                 # Imports the PS-Drone-API


drone = ps_drone.Drone()
drone.startup()
authKey = 812601927

authenticate = False


drone.takeoff()                 # the drone begins its flight
time.sleep(7.5)                 # command continues for 7.5 seconds

while(authenticate == False):


drone.land()                    # The drone lands
