class UserInteraction:
    def __init__(self, fans):
        self.fans = fans

    def select_fan(self):
        fan_num = input("\033[34mWhich fan do you want to interact with (1 or 2)? \033[0m")
        if fan_num in ['1', '2']:
            return self.fans[int(fan_num) - 1]
        else:
            print("Invalid input. Please enter 1 or 2.")
            return self.select_fan()

    def fan_interaction(self):
        fan = self.select_fan()
        action = input("Do you want to get or set the fan's attributes? \033[31m(get/set): \033[0m")

        if action.lower() == "get":
            self.get_attributes(fan)
        elif action.lower() == "set":
            self.set_attributes(fan)
        else:
            print("\033[31mInvalid input. Please enter 'get' or 'set'.\033[0m")
            return self.fan_interaction()
        self.retry()
    def get_attributes(self, fan):
        print("\033[1m\033[92mSpeed:\033[0m", fan.get_speed())
        print("\033[1m\033[92mPower:\033[0m", fan.get_power())
        print("\033[1m\033[92mRadius:\033[0m", fan.get_radius())
        print("\033[1m\033[92mColor:\033[0m", fan.get_color())

    def set_attributes(self, fan):
        attribute = input("Which attribute do you want to set? \033[31m(speed/power/radius/color): \033[0m")
        value = input("Enter the new value for the attribute: ")

        if attribute.lower() == "speed":
            fan.set_speed(int(value))
        elif attribute.lower() == "power":
            fan.set_power(value.lower() == 'true')
        elif attribute.lower() == "radius":
            fan.set_radius(float(value))
        elif attribute.lower() == "color":
            fan.set_color(value)
        else:
            print("\033[31mInvalid attribute. Please enter 'speed', 'power', 'radius', or 'color'.\033[0m")
            return self.set_attributes(fan)
    def retry(self):
        retry = input("Do you have other actions? \033[31m(yes/no)\033[0m: ")
        if retry.lower() == 'yes':
            self.fan_interaction()
        elif retry.lower() == 'no':
            print("\033[92mThank you for using the fan system.\033[0m")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.retry()