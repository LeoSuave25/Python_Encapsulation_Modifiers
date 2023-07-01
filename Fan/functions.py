'''A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed
'''
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self,speed=1,power=False,radius=5,color="blue"):
        self.__speed = speed
        self.__power = power
        self.__radius = float(radius)
        self.__color = color
