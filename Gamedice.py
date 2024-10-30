import random #Import random libary

print("Welcome to the Dice Game")

def rolls(): # function, that responsible for rolling the dice. 
 genrate=random.randint(1,6)
 return genrate #If we do not make return the value will be non. 
#("Test the number ",rolls()) #This code wil help os to see the randome number.  

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
  
  




































"""
import random # Import the random libary
print("The Dice Game ")
def rolls(): #Write a function 
  genrate=random.randint(1,6) #make a vairable genrate. use the random and randint to take to value
                           # a, b. my case 1 to 6
  return genrate             #return genrate 
 # print("The random number is:",rolls())    #This code wil help os to see the randome number.    

player_score=0 #Making the three variable 
computer_score=0
target_score=20

# Now i will make the while loop 
while player_score <target_score and computer_score <target_score:
   player_score+=rolls() #calling the function and opdate it. 
   computer_score+=rolls() #Calling the roll function for the computer variable.
   if player_score>=target_score: #Make the condition. If the player is greater than the target sorce or equal it mean the player is win
    print("The player wine: "+ str(player_score)) #Print the player is win. 
    break # if the player is win it will make break 
   elif computer_score>=target_score:     #otherwise the computer win 
    print("The computer win:"+str(computer_score)) #Print the computer is win. 
    
"""

"""
import random  # Import random libary
def rolls(): # function, that responsible for rolling the dice. 
  genrate=random.randint(1,6) # the genrate number will be store in genrate variable. 
                              # Return the genrate number  
  return genrate  #If we do not make return the value will be non. 
print("The genrate number: ", rolls()) #if we want to see the number that been genrate we use print function. 

#make the vairable 
player_score=0 # for the player 
computer_score=0 #The computer variable 
target_score=20   #Variable for score 

# while loop
while player_score < target_score and computer_score < target_score: # so long the player_score is less than target_score and computer_score is less than target score
  player_score+=rolls() # this code is calling the rolls function and opdating the player_score 
  computer_score+=rolls() #The code is doing the same thing. calling the function and adding the value to computer_score 
  if player_score>=target_score: #Condition, the code is if the player_score is greater or equal to target_score 
    print("The player is win", str(player_score)) #That mean the player is will win
    break #If the player win the loop will end 
  elif computer_score>=target_score: # otherwise the computer is greater or equal to target_score 
   print("The computer is win: ",str(computer_score)) #The computer will win. cl
  

"""