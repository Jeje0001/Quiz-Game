print("Welcome to the quiz game")

playing=input("Do you want to play the quiz game enter yes or no?").lower()
def Start():
        print("The game will start now")


if playing == "yes":
        Start()
else:
        quit()

score=0


answer=input(" What does the cpu stand for ?  ").lower()

if answer == "central processing unit":
        print("You are right")
        score+=1
else:
        print("You are wrong")


answer=input(" What does the gpu stand for ?  ").lower()

if answer == "graphics processing unit":
        print("You are right")
        score+=1
else:
        print("You are wrong")
    

answer=input(" What does the ram stand for ?  ").lower()

if answer == "random access memory":
        print("You are right")
        score+=1
else:
        print("You are wrong")

answer=input(" What does the rom stand for ?  ").lower()

if answer == "read only memory":
        print("You are right")
        score+=1
else:
        print("You are wrong")


print("You got " + str(score) + " right")

percent= int(((score / 4)*100))
print("You got " + str(percent) + " percent")