import random

high=int(input("Wprowadź zakres: "))
low = 1
z=1
feedback=""
while feedback !="c":
    robot = random.randint(low, high)
    feedback=input(f"is {robot} too high(h), too low(l) or correct(c)? ")
    if feedback =="l":
        low=robot+1
        z=z+1
    elif feedback == "h":
        high=robot-1
        z=z+1
print(f"The computer guessed the correct number. It took {z} tries")
