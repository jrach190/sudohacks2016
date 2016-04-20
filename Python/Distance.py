"""
This file was Written by Jeremiah Lantzer
for sudoHacks 2016
functions to help drone go to any
final location. Functions called in Drone Demo.
"""


import math
from geopy.geocoders import Nominatim
from geopy.distance import vincenty


def latitude(address):  # converts a person's address into latitude
    geolocator = Nominatim()
    location = geolocator.geocode(address)  # function from the geopy library for conversion to distance
    print(location.latitude)
    return location.latitude


def longtitude(address):  # converts a person's address into longitude
    geolocator = Nominatim()
    location = geolocator.geocode(address)  # function from the geopy library for conversion to distance
    print(location.longitude)
    return location.longitude


def conversion(latitudepub, longitudepub, latPharm, longPharm):  # finds the final distance between the home and pharm
    origin = (latPharm, longPharm)
    final = (latitudepub, longitudepub)
    return vincenty(origin, final).miles  # converts 2 longitudes and latitudes to miles between them


def findtime(distance, speedofdrone):  # receives the distance between two points, the speed of the drone.
    time = distance / speedofdrone     # returns time the drone must fly for
    return time


def findangle(xvector, yvector):  # drone is initialized at a set angle
    angle = math.atan2(xvector, yvector)
    angle *= 2 * math.pi
    return angle
