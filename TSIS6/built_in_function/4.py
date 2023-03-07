import math
import time

number = int(input("Enter a number: "))
time_in_milliseconds = int(input("Enter a time in milliseconds: "))


time.sleep(time_in_milliseconds / 1000)
print(math.sqrt(number))
