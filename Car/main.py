from carclass import Car
from driver import Driver
from style import Styling

headers = Styling()

my_car = Car(1990, "Mitsubishi Lancer", 30)
driver = Driver(my_car)

driver.drive()