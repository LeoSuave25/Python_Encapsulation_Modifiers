class Car:
    def __init__(self,year_model,make,speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    def accelerate(self):
        if self.__speed < 300:
            self.__speed += 5
            return True
        else:
            print("\033[1;31mThe car is overheating!\033[0m")
            self.__speed = 0
            return False
    def brake(self):
        if self.__speed > 0:
            self.__speed -= 5
            return True
        else:
            print("\033[1;32mThe car has already stopped.\033[1;31m")
            return False
    def get_speed(self):
        return self.__speed
    def get_year_model(self):
        return self.__year_model
    def get_make(self):
        return self.__make