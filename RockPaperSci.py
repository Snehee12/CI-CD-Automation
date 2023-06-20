#!!!!!!!!!!!!!!!!!!!!! ROCK, PAPER,SCISSORS GAME !!!!!!!!!!!!!!!!!!!!!!!!

import random

#Choices
rock='''
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  '''
paper='''
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)'''
scissors='''
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  '''

#List containing all choices
game=[rock,paper,scissors]

#Random choice by computer
random_int=random.randint(0,2)
Computer_choice=game[random_int]

#making user choose their part
choice=int(input("What do you want to choose?\n1.ROCK\n2.PAPER\n3.SCISSORS\n"))
your_choice=game[choice-1]

#game conditons
if Computer_choice==rock and your_choice==rock:
    count=-1
elif Computer_choice==paper and your_choice==paper:
    count=-1
elif Computer_choice==scissors and your_choice==scissors:
    count=-1
elif Computer_choice==rock and your_choice==scissors:
    count=0
elif Computer_choice==scissors and your_choice==paper:
    count=0
elif Computer_choice==paper and your_choice==rock:
    count=0
elif Computer_choice==rock and your_choice==paper:
    count=1
elif Computer_choice==scissors and your_choice==rock:
    count=1
elif Computer_choice==paper and your_choice==scissors:
    count=1

#Printing their choice
print(f"\n\nComputer chose:\n{Computer_choice}")
print(f"\n\n\nYou chose:\n{your_choice}\n\n\n")

#Displaying results
if count==-1:
    print("Its a DRAW")
elif count==0:
    print("Sorry!!\n\n YOU LOST\n\n(ಥʖ̯ಥ)৴ SAD (ಥʖ̯ಥ)৴")
elif count==1:
    print("Congratulations!!! YOU WON\n\n☆彡(ノ^ ^)ノ Congratulations ヘ(^ ^ヘ)☆彡")
else:
    print("!!ERROR!!")
