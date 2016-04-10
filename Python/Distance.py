import math
from geopy.geocoders import Nominatim
from geopy.distance import vincenty


def latitude(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    print(location.latitude)
    return location.latitude


def longtitude(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    print(location.longitude)
    return location.longitude


def difference(n1, n2):
    difference = n2 - n1
    return difference


def vector(xvector, yvector):
    distance = math.sqrt(math.pow(xvector, 2) + math.pow(yvector, 2))
    return distance


def conversion(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    origin = (0.0, 0.0)
    final = (location.latitude, location.longitude)
    return vincenty(origin, final).miles
