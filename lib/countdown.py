# your code goes here!
from time import sleep 

def countdown(integer):
    x = integer
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(integer):
    i = integer
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
        sleep(1)
    print("HAPPY NEW YEAR!")
