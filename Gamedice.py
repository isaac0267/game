
import random #Import random libary

print("Welcome to the Dice Game")

def rolls(): # function, that responsible for rolling the dice. 
 genrate=random.randint(1,6)
 return genrate #If we do not make return the value will be non. 
("Test the number ",rolls()) #This code wil help os to see the randome number.  

player_score=0 # for the player 
computer_score=0 #The computer variable 
target_score=20  #Variable for score 

def playr(): # make a function showing the player win, when it reallay win
  print("The player win")

def ai():  # make the function the AI is win, when it really win
  print("AI win the")


while player_score<target_score and computer_score<target_score: # so long the player_score is less than target_score and computer_score is less than target score
  player_score+=rolls() # this code is calling the rolls function and opdating the player_score 
  computer_score+=rolls() #The code is doing the same thing. calling the function and adding the value to computer_score 

  if player_score >=target_score:  #Condition, the code is if the player_score is greater or equal to target_score
   playr() # calling the player function
   break # make a break if the player win 
  elif computer_score>=target_score: ## otherwise the computer is greater or equal to target_score 
    ai() #calling the ai function. 
    break  # the loop will stop if the ai winclear




































