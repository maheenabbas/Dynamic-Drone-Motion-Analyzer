from vpython import *
#Web VPython 3.2

# create time variable, t, and time step, dt
t = 0
dt = 0.1
# creating the objects:
# 1- ground/floor as demanded in the Q
ground = box (pos = vector (0, 0, 0), size = vector(10,0.5,5), color = color.gray(0.5), opacity=0.8)
# 2- inorder to convert degree to radians- added pi.
drone = sphere(pos = vec(3*cos(0.6*pi*t), 2*sin(0.6*pi*t), 0.05*t**2), radius = 1, color = color.cyan, make_trail = True, trail_color = color.red)
# 3- Store drone position to be used later
# whatever pos the drone is at rest (t=0), 
# we use that and store it as a variable to be used in the while clause
drone_Position = drone.pos

#loop to animate the drone - since the Q asks for t equals to less than 10
while t <= 10:
    # set rate to control loop speed
    rate(5000)
    #storing a pos vec as a variable 
    droneposition = drone.pos
    #if t less than 0 then 
    if t > 0:
        #storing a velocity vec as a variable 
        dronevelocity = drone.vel
        # create velocity arrow that is attached to the drone
        velArr = attach_arrow(drone, "vel", color = color.blue, round = True)
        # update time to new time
        t = t + dt 
        # update poss to new value
        drone.pos = vec(3*cos(0.6*pi*t),2*sin(0.6*pi*t),0.05*t**2)
        
        #use the previous pos and subtract from the updated postion in order to get the new velocity and divide it by change in time    
        drone.vel = (drone.pos - droneposition) / dt
        #use the previous velocity and subtract from the updated velocity in order to get the accelration and divide it by change in time    
        drone.acc = (drone.vel - dronevelocity) / dt
        # create acceleration arrows that are atached to the drone
        accArr = attach_arrow(drone, "acc", shaftwidth=0.5, color = color.orange, round = True)
       
        # calculate acceleration components
        drone.acc_tan = (drone.acc).proj(drone.vel)
        drone.acc_rad = drone.acc - drone.acc_tan
        
        acc_tanArr = attach_arrow(drone, "acc_tan",  shaftwidth=0.5, color = color.cyan, round = True)
        acc_radArr = attach_arrow(drone, "acc_rad",  shaftwidth=0.5, color = color.purple, round = True)

   #if t equals to 0 or less than 0 then     
    else:
        # update time to new time
        t = t + dt 
        # update poss for new value of t 
        drone.pos = vec(3*cos(0.6*pi*t),2*sin(0.6*pi*t),0.05*t**2)
        #use the previous pos and subtract from the updated pos in order to get the velocity and divide it by change in time 
        drone.vel = (drone.pos - droneposition) / dt
        
        
# output the acc, tan acc, rad acc
print ("Pos = " + drone.pos + "m \n")
print ("Velocity = " + drone.vel + " m/s \n" )
print("Drone's Acceleration = " + drone.acc + " m/s^2 \n")
print("Drone's Tangential Accerelation = " + drone.acc_tan + " m/s^2 \n")
print("Drone's Radial Acceleration = " + drone.acc_rad + " m/s^2")
