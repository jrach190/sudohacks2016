"""
Portions of code implement the ps_drone API, used as per license. Software written by Jeremiah Lantzer
and Jonathan Rach for Sudo HackStetson 2016 Hackathon
"""

import time
import ps_drone
from pubnub import Pubnub
import Distance

global msg
global speedofdrone


# Initialize drone
drone = ps_drone.Drone()

drone.startup()         # connect to drone
speedofdrone = 11  # assuming the constant top speed of drone: 11 mph
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])  # outputs current battery level
print "Drone initialized"


# initialize pubnub
pubnub = Pubnub(publish_key='demo', subscribe_key='sub-c-312e2a08-fee2-11e5-9086-02ee2ddab7fe')


def _callback(message, channel):  # pubnub code for receiving information from the front end to the drone
    
    msg = message  # allow message variable to be used outside callback if needed
    # print(message)
    if msg == "ret":
        pubnub.unsubscribe(channel='demo')  # unsubs for a moment to call function without an error
        flyHome()

    elif msg != "" :
        pubnub.unsubscribe(channel='demo')   # unsubs for a moment to call function without an error
        flyAway()
        pubnub.subscribe(channels="demo", callback=_callback, error=_error)  # subscribes again
    else:
        print (message)


def flyAway():
    print 'Drone leaving base'

    address = "1600 Pennsylvania Ave NW, Washington, DC 20500" '''
                                                                Normally set to receiving address.
                                                                For demo purposes
                                                                phone shall send a preset value.
                                                               '''
    addressPharm = "901 N Woodland Blvd, DeLand, FL 32720"

    drone.takeoff()         # launch drone
    time.sleep(7.5)         # wait 7.5s for drone to take off before executing commands
        
    drone.moveUp(1)         # increase altitude
    time.sleep(2)           # wait for increase

    moveDist(address, addressPharm)  # sends the drone to its destination
        
    print 'Drone arrived'
    drone.hover()
    '''
    hover drone over drop site
    doesn't fly home until command is received from phone
    '''


def flyHome():
    print 'Drone returning home'
        
    """
    Code for testing purposes

    drone.turnLeft()       #turn drone left to reverse direction
    time.sleep(4.5)         #turn for 4.5 seconds to reverse direction
            
    drone.moveBackward()     #move drone forward
    time.sleep(6)           #move forward for 2 seconds
    """

    address = "1600 Pennsylvania Ave NW, Washington, DC 20500" '''
                                                                Normally set to receiving address.
                                                                For demo purposes
                                                                phone shall send a preset value.
                                                               '''
    addressPharm = "901 N Woodland Blvd, DeLand, FL 32720"

    drone.turnLeft(.5)  # drone turns 180 degrees
    time.sleep(1)       # drone moves 180 degrees/sec at half power

    moveDist(address, addressPharm)  # sends the drone home the same way it came

    drone.moveDown()   # reverse height increase
    time.sleep(2)           # lower height for 4 seconds
        
    drone.land()
    print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])   # tells the battery level after the
                                                                                    # flight took place
    exit()


def _error(message):
    print(message)

pubnub.subscribe(channels="demo", callback=_callback, error=_error)


def moveDist(address, addressPharm):     # function to send the drone the distance it needs to fly
                    # also used for return trips

    deliveryLat = Distance.latitude(address)  # converts an address to its latitude equivalent
    deliveryLong = Distance.longtitude(address)   # converts an address to its longitude equivalent
    pharmcacyLat = Distance.latitude(addressPharm)
    pharmacyLong = Distance.longitude(addressPharm)
    flyDist = Distance.conversion(deliveryLat, deliveryLong, pharmcacyLat, pharmacyLong)
    # conversion finds the distance in miles between two longitudes and latitudes

    drone.moveForward()
    time.sleep(Distance.findtime(flyDist, speedofdrone))  # receives the time the drone must move for
