#ROCK,PAPER AND SCISSOR GAME.
#-1=ROCK,0=PAPER,1=SCISSOR

import random
your_score=0
computer_score=0
print("GAME RULES:Rock beats Scissor,Scissor beats Paper,Paper beats Rock")
try:
    rounds=int(input("Enter the number of rounds:"))
    if rounds<=0:
        print("Rounds must be valid.")
        exit() 
except ValueError:
    print("Invalid response.")
    exit()
yourdict={
    "r":-1,
    "p":0,
    "s":1
}
reversedict={
    -1:"ROCK",
    0:"PAPER",
    1:"SCISSOR"
}
for i in range(rounds):
    computer=random.choice([-1,0,1])       
    yourstr=input("Enter 'R' or 'P' or 'S':").lower()
    if yourstr not in yourdict:
        print("Invalid response.")
        continue
    you=yourdict[yourstr]
    if(you==computer):
        print("It is a draw.")
    elif(computer==-1 and you==0):
        print("You won.")
        your_score+=1
    elif(computer==0 and you==1):
        print("You won.")
        your_score+=1
    elif(computer==1 and you==-1):
        print("You won.")
        your_score+=1
    else:
        print("You lose.")
        computer_score+=1
    print(f"'Your' score is '{your_score}' and 'Computer' score is '{computer_score}'")

if(your_score>computer_score):
    print("You won")
elif(your_score<computer_score):
    print("You lose")
else:
    print("Its a draw")