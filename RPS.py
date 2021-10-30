import random

def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "s":
            return False
        elif you =="p":
            return True
    elif comp == "s":
        if you == "p":
            return False
        elif you =="r":
            return True
    elif comp == "p":
        if you == "r":
            return False
        elif you =="s":
            return True
        


print("Computer turn rock(r) paper(p) scissors(s)")
randInp = random.randint(1,3)
if randInp == 1:
        comp = "r"
elif randInp == 2:
        comp = "p"
elif randInp == 3:
        comp = "s"
   
you = input("Your turn choose 1 rock(r) paper(p) scissors(s)")
a = gameWin(comp,you)

print(f"Comp choice is {comp}")
print(f"You choice is {you}")

if a == None:
    print("It's a tie")
elif a == True:
    print("You Win!")
elif a == False:
    print("You Lose!")

