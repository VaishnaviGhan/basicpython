import random

def GameWin(comp,you):
    if comp==you:
      return None
    elif comp =='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
           return False
        elif you=='s':
           return True


    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
                return True

print("Comp turn: Snake(s) Water(w) Gun(g)..")
randNo = random.randint(1,3)
if randNo==1:
    comp ='s'

elif randNo=='2':
    comp ='w'
elif randNo=='3':
    comp='g'

you = input("Your Turn: Snake(s) Water(w)  Gun(g)")
a = GameWin(comp ,you)

print(f"Computer choise {comp}")
print(f"your choise {you}")

if a =='None':
    print("Tie")
elif a:
        print("win")
else:
        print("loss")