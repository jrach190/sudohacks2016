import time
import ps_drone

drone = ps_drone.Drone()
drone.startup()

drone.reset()
print "Batterie: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])

drone.takeoff()
time.sleep(7.5)

"""drone.mtrim()
time.sleep(5)


drone.moveForward()
time.sleep(2)
drone.stop()
time.sleep(2)

drone.moveBackward(0.25)
time.sleep(1.5)
drone.stop()
time.sleep(2)

drone.setSpeed(1.0)
print drone.setSpeed()

drone.turnLeft()
time.sleep(2)
drone.stop()
time.sleep(2)"""

drone.move(0,0,.5,0)
time.sleep(4)

#drone.anim(16,1)

"""drone.moveBackward()
time.sleep(2)
drone.moveForward()
time.sleep(0.25)
drone.hover()"""

drone.setSpeed(1)
drone.turnright(2)
time.sleep(2)

drone.hover()


print "Batterie: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])

drone.land()