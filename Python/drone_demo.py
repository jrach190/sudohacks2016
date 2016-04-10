"""Portions of code implement the ps_drone API, used as per license. Software written by Jeremiah Lantzer
    and Jonathan Rach for Sudo HackStetson 2016 Hackathon"""

import time
import ps_drone
from pubnub import Pubnub

global msg



#Initialize drone
drone = ps_drone.Drone()

drone.startup()         #connect to drone
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])
print "Drone initialized"


#initialize pubnub
pubnub = Pubnub(publish_key='demo', subscribe_key='sub-c-312e2a08-fee2-11e5-9086-02ee2ddab7fe')


def _callback(message, channel):
    
    msg = message #allow message variable to be used outside callback if needed
    #print(message)
    if msg == "ret":
        pubnub.unsubscribe(channel='demo')
        flyHome()

    elif msg != "" :
        pubnub.unsubscribe(channel='demo')
        flyAway()
        pubnub.subscribe(channels="demo", callback=_callback, error=_error)
    else:
        print (message)

def flyAway():
    print 'Drone leaving base'
    drone.takeoff()         #launch drone
    time.sleep(7.5)         #wait 7.5s for drone to take off before executing commands
        
    drone.moveUp(1)
    time.sleep(2)
        
    """drone.turnRight(1)      #turn drone to the right at full speed
        time.sleep(2.25)        #stop the turn after 90 degrees"""
            
    drone.moveForward()
    time.sleep(6)
        
    print 'Drone arrived'
    drone.hover()           #hover drone over drop site

def flyHome():
    print 'Drone returning home'
        
    """drone.turnLeft()       #turn drone left to reverse direction
    time.sleep(4.5)         #turn for 4.5 seconds to reverse direction
            
    drone.moveBackward()     #move drone forward
    time.sleep(6)           #move forward for 2 seconds"""
        
    drone.moveDown()   #reverse height increase
    time.sleep(2)           #lower height for 4 seconds
        
    drone.land()
    print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])
    exit()

def _error(message):
    print(message)

pubnub.subscribe(channels="demo", callback=_callback, error=_error)