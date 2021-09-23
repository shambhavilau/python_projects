import random

doors = [0]*3
goat_door = [0]*2
swap = 0    # keep track of no. of swap wins
dont_swap = 0   # keep track of no. of don't swap wins

j = 0
while j < 10:
    x = random.randint(0, 2)  # generate a random door which will comprise of the Prize
    doors[x] = "BMW"  # prize
    for i in range(0, 3):
        if i == x:
            continue
        else:
            doors[i] = "Goat"
            goat_door.append(i)

    choice = int(input("Enter your choice"))
    door_open = random.choice(goat_door)  # open a door that doesnt have the prize
    while door_open == choice:
        door_open = random.choice(goat_door)   # if selected door is same as the goat door then again select a door
        # since they should not be same

    ch = input("DO you wish to swap y/n")
    if ch == 'y':
        if doors[choice] == "Goat":
            print("You won")
            swap += 1
        else:
            print("You lost")
    else:
        if doors[choice] == "Goat":
            print("You lost")
        else:
            print("You won")
            dont_swap += 1
    j += 1

print("Swap wins: ", swap)
print("Don't Swap wins: ", dont_swap)
