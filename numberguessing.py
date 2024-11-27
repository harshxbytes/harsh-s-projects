import random
print("Today we are going to play a very exciting game:-")
print("The game will be like:-")
print("you will enter a number and the same my computer and if the number matches then you will win in one attempt")
print("the less the score of person he/she wins")
print("enjoy your game")

num = int(input("Guess the number - it's your turn now "))
computernum = random.randint(0,100)


for i in range (0,150):
  
    num = int(input("Guess the number - it's your turn now "))
    if (computernum - num) < 10 :
          print("you are very much near")
          
    elif (computernum - num) <20:
          print("you are just few steps away ")
          
    elif (computernum - num ) < 30:
          print("you are having a way differce between input and targets")
                 
    else :
          print("you are very far from the target")
    if num == computernum :
        print ("you won -- you are the perfect human in this world as very few people in the past have only guessed the number in just one attempt ")
        print ("you should have +9999 aura")
        print("hope you enjoyed")
        exit()
