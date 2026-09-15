import random

computer=random.choice([0,-1,1])

youstr=input("Enter the choice: ")
youDict={"s": 1,"w":-1, "g":0}
reverseDict = {1: "Snake", -1:"Water", 0: "Gun"}

you = youDict.get(youstr)
if you is None:
    print("Invlid choice! Please enter s,w or g")
    exit()
print(f"You chose: {reverseDict[you]} \nComputer chose: {reverseDict[computer]}")

if(computer==you):
    print("Draw!")
else:
    if(you==1 and computer==-1):
        print("You win!")
    elif(you==1 and computer==0):
        print ("You lose!")
    elif(you==-1 and computer==1):
        print("You lose!")
    elif(you==-1 and computer==0):
        print("You lose!")
    elif(you==0 and computer==1):
        print("You win!")
    elif(you==0 and computer==-1):
        print("You win!")
    else:
        print("Somehing went wrong!")
    

