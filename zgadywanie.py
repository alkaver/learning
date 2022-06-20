#Komputer znajduje liczbę podaną przez użytkownika



import random
liczba=int(input("Wprowadź liczbę: "))
y=int(input("Wprowadź zakres: "))
robot=random.randint(1,y)
print(robot)
z=1
while liczba !=robot:
    if robot<liczba:
        x=robot
        robot = random.randint(x+1, liczba)
        print(robot)
        z=z+1
    if robot>liczba:
        x=robot
        robot = random.randint(liczba, x-1)
        print(robot)
        z=z+1
print(f"ilość zgadnięć:{z}")