class Car:
    def __init__(self,year_model,make,speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        print(self.__speed)