import pyfiglet as fig
class Styling:
    def __init__(self):
        print("\033[32m","="*100,"\033[m")
        title = "Python Car"
        print("\033[32m",fig.figlet_format(title),"\033[m")
        print(fig.figlet_format("Made by: Leoj M Suaverdez",font="bubble"))