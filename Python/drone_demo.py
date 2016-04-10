import time
import ps_drone
from pubnub import Pubnub

global msg



#Initialize drone
drone = ps_drone.Drone()

drone.startup()         #connect to drone
drone.reset()           #reset drone to good state after poor condition event
time.sleep(2)           #wait for reset to complete before allowing other commands
print "Drone initialized"


#initialize pubnub
pubnub = Pubnub(publish_key='demo', subscribe_key='sub-c-312e2a08-fee2-11e5-9086-02ee2ddab7fe')


def _callback(message, channel):
    msg = message #allow message variable to be used outside callback if needed
    #print(message)
    if msg == "ret":
        print 'Drone returning home'

        drone.turnLeft()       #turn drone left to reverse direction
        time.sleep(4.5)         #turn for 4.5 seconds to reverse direction

        drone.moveForward()     #move drone forward
        time.sleep(2)           #move forward for 2 seconds"""

        drone.move(0,0,-1,0)   #reverse height increase
        time.sleep(6)           #lower height for 4 seconds

        drone.land()
        exit()

    elif msg != "" :
        print 'Drone leaving base'
        drone.takeoff()         #launch drone
        time.sleep(7.5)         #wait 7.5s for drone to take off before executing commands

        drone.move(0,0,1,0)    #move drone up at half speed
        time.sleep(6)           #move drone up for 4 seconds

        """drone.turnRight(1)      #turn drone to the right at full speed
        time.sleep(2.25)        #stop the turn after 90 degrees
        """
        drone.moveForward()
        time.sleep(2)

        drone.hover()           #hover drone over drop site"""

    else:
        print (message)

def _error(message):
    print(message)

pubnub.subscribe(channels="demo", callback=_callback, error=_error)