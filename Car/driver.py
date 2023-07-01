from carclass import Car
class Driver:
    def __init__(self, car):
        self.car = car
        print(f"\033[1;34mYou are driving a {self.car.get_year_model()} {self.car.get_make()}. Current speed: {self.car.get_speed()} km/h\033[0m")
    def drive(self):
        while True:
            action = input("\033[1;33mDo you want to accelerate, brake, or get current speed? Enter 'quit' to stop: \033[0m")
            if action.lower() == "accelerate":
                times = int(input("\033[1;32mHow many times do you want to accelerate? \033[1;32m"))
                for i in range(times):
                    if not self.car.accelerate():
                        break
                print(f"\033[1;32mCurrent speed: {self.car.get_speed()} km/h\033[0m")
            elif action.lower() == "brake":
                times = int(input("\033[1;31mHow many times do you want to brake? \033[0m"))
                for i in range(times):
                    if not self.car.brake():
                        break
                print(f"\033[1;32mCurrent speed: {self.car.get_speed()} km/h\033[0m")
            elif action.lower() == "get current speed":
                print(f"\033[1;32mCurrent speed: {self.car.get_speed()} km/h\033[0m")
            elif action.lower() == "quit":
                print("\033[1;92mYou are now exiting your vehicle.\033[0m")
                break
            else:
                print("\033[1;31mInvalid input. Please enter 'accelerate', 'brake', 'get current speed' or 'quit'.\033[0m")