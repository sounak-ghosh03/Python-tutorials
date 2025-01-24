# DESIGNING A SNAKE WATER GUN GAME IN PYTHON
# The gun beats the snake, the water beats the gun, and the snake beats the water.

import random


def check(comp, user):              #checking the condition of the game
    if (comp == user):
        return 0

    if (comp == 0 and user == 1):
        return -1

    if (comp == 1 and user == 2):
        return -1

    if (comp == 2 and user == 0):
        return -1

    return 1

myscore=0
compscore=0
print("\nWELCOME TO SNAKE, WATER AND GUN GAME!!!\n")
n = int(input("Enter number of rounds you want to play\n"))
for i in range(n):
    print("\nROUND NUMBER",i+1)
    comp = random.randint(0, 2)         #generates a random number between 0 to 2
    user = int(input("Enter 0 for Snake, 1 for water and 2 for Gun\n"))
    
    if (user < 0 or user > 2):
            
        print("Invalid choice!!\n") 
        continue
            

    score = check(comp, user)

    print("You chose Snake") if (user==0) else print("You chose Water")if(user==1) else print("You chose Gun")
    print("Computer chose Snake") if (comp==0) else print("Computer chose Water")if(comp==1) else print("Computer chose Gun")


    if (score == 0):
        print("Its a draw")
    elif (score == -1):
        print("You Lose")
        compscore+=1
    else:
        print("You Won")
        myscore+=1

print("\nYour total score:",myscore)
print("Computer total score:",compscore)

if (myscore > compscore):
    print("YOU WIN THE GAME!!!")
elif (myscore == compscore):
    print("ITS A DRAW!!!!")
else:
    print("YOU LOSE THE GAME!!!")