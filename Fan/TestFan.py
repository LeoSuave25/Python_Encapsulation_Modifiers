'''For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. 
Assign medium speed, radius 5, color blue, and turn it off for the second object. 
Display each object’s speed, radius, color, and on properties.'''
from functions import Fan
from style import Styling
from user_interactions import UserInteraction
headers = Styling()

first_fan = Fan(Fan.FAST,True,10,"Yellow")
second_fan = Fan(Fan.MEDIUM,False,5,"Blue")

fans = [first_fan, second_fan]

interaction = UserInteraction(fans)
interaction.fan_interaction()