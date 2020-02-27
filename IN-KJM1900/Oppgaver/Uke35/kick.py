
# coding: utf-8

# In[2]:


import numpy as np

###Starting with the constants###

#gravitational constant in m/s^2
GRAVITATIONAL_CONSTANT=9.8

#drag coefficient 
DRAG_COEFFICIENT = 0.4

#density of air. the unit is kg m^3
AIR_DENSITY = 1.2 

SECONDS_IN_HOUR = 3600.0
METERS_IN_KM = 1000.0

###Given in the problem###

#the units for the velocities below are in km/h, have to convert this to m/s
hardKickVelocityKmH = 120.
softKickVelocityKmH = 30.

# football radius in CM 
footballRadiusCm = 11.

# mass of football in KG 
footballWeight = 0.43

###Defining some useful functions###

def centimeterToMeter(cm): 
    return cm /100.0

#converts the velocity from Km/h to m/s
#param: kmh - the velocity in km/h
#return: corresponding velocity in m/s
def KmHToMs(kmh): 
    return kmh*METERS_IN_KM/SECONDS_IN_HOUR

""" Computes the area of a circle. 
param: radius - radius in METER! if the radius is in centimeter, use centimeterToMeter to convert it first. """
def computeCircleArea(radius): 
    return np.pi*(radius**2)
    
#computes the drag force 
#params: area - should be in m**2
#velocity - should be in m/s
#returns - drag force in 
def computeDragForce(area, velocity): 
    return (DRAG_COEFFICIENT * AIR_DENSITY* area * (velocity**2))/2
    
#compute the gravitational force
#param: mass - should be in meters 
#returns the gravitational force
def computeGravitationalForce(mass):
    return mass**GRAVITATIONAL_CONSTANT

###NB: No one specified the number of decimal places in the problem. 

#the mass will be the same regardless of speed, so we can just print this once
print (f"Gravitational force: {computeGravitationalForce(footballWeight)} N")

"""To get the drag force,
we need to get the area of the ball first, 
we need to ensure that the unit is converted to meters before doing it.
after than we can just call computeDragForce """
footballArea = computeCircleArea(centimeterToMeter(footballRadiusCm));

hardKickDragForce = computeDragForce(footballArea, KmHToMs(hardKickVelocityKmH))
softKickDragForce = computeDragForce(footballArea, KmHToMs(softKickVelocityKmH))

print(f"Drag force when kicking hard: {hardKickDragForce} N")
print(f"Drag force when kicking softly: {softKickDragForce} N")
r"""
PS C:\Users\Min PC\Downloads> python .\kick.py
Gravitational force: 0.00025585320679968063 N
Drag force when kicking hard: 10.136872295583068 N 
Drag force when kicking softly: 0.6335545184739417 N"""