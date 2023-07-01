import subprocess
import pyfiglet as fig

print("\033[32m","="*100,"\033[m")
title = "Main Interface"
print("\033[32m",fig.figlet_format(title),"\033[m")
print(fig.figlet_format("Made by: Leoj M Suaverdez",font="slant"))

while True:
    program = input("\033[1;32mWhich program do you want to access? (Car, Pet, Fan, quit): \033[0m")
    if program.lower() == 'car':
        subprocess.run(["python", "./Car/main.py"])
    elif program.lower() == 'pet':
        subprocess.run(["python", "./Pet/main.py"])
    elif program.lower() == 'fan':
        subprocess.run(["python", "./Fan/TestFan.py"])
    elif program.lower() == 'quit':
        print("\033[1;31mYou are now exiting the main interface\033[0m")
        break
    else:
        print("\033[1;31mInvalid input. Please enter 'Car', 'Pet', 'Fan' or 'quit'.\033[0m")
