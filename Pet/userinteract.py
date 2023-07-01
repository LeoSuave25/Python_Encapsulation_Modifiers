from HomePet import Pet

class UserInteraction:
    def prompt_user(self):
        # Prompt the user for their pet's information
        name = input("\033[1;32mEnter your pet's name: \033[0m")
        animal_type = input("\033[1;32mEnter your pet's type: \033[0m")
        while True:
            age = input("\033[1;32mEnter your pet's age: \033[0m")
            if age.isdigit():
                age = int(age)
                break
            else:
                print("\033[1;31mInvalid input. Age must be an integer.\033[0m")
        

        # Create a Pet object with the user's input
        pet = Pet(name, animal_type, age)

        return pet

    def display_pet_info(self, pet):
        # Use the Pet object's accessor methods to print the pet's information
        print(f"\033[1;34mYour pet's name is {pet.get_name()}.\033[0m")
        print(f"\033[1;34mYour pet is a {pet.get_animal_type()}.\033[0m")
        print(f"\033[1;34mYour pet is {pet.get_age()} years old.\033[0m")
    
    def ask_display(self):
        while True:
            display = input("\033[1;33mDo you want to display your pet's information? (yes/no): \033[0m")
            if display.lower() in ['yes', 'no']:
                return display.lower() == 'yes'
            else:
                print("\033[1;31mInvalid input. Please enter 'yes' or 'no'.\033[0m")

    def retry(self):
        while True:
            pet = self.prompt_user()
            if self.ask_display():
                self.display_pet_info(pet)
            retry = input("\033[1;33mDo you want to enter another pet's information? (yes/no): \033[0m")
            if retry.lower() == 'no':
                print("\033[92mThank you for using the pet information system.\033[0m")
                break