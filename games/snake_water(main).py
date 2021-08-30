import random

def game(comp,you):
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
        else:
            return None
    if comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
        else:
            return None
    if comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
        else:
            return None                    

randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'    

print("WELCOME to Snake Water Gun Game")       
print("Computers Turn choose: Snake(s), Water(w) or Gun(g): ")
you=input("Your Turn choose: Snake(1), Water(2) or Gun(3): ")

print(f"Computer chose {comp}")
print(f"You chose {you}")

a=game(comp,you)
if a==None:
    print("The game is a tie")
elif a==True:
    print("Congratlations! You Won")
else:
    print("You loose! Better luck next time")    

