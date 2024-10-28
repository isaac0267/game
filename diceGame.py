import random # Import the random libary
print("The Dice Game ")
def rolls(): #Write a function 
  genrate=random.randint(1,6) #make a vairable genrate. use the random and randint to take to value
                           # a, b. my case 1 to 6
  return genrate             #return genrate 
 # print("The random number is:",rolls())    #This code wil help os to see the randome number.    

player_score=0
computer_score=0
target_score=20

# Now i will make the while loop 
while player_score <target_score and computer_score <target_score:
   player_score+=rolls()
   computer_score+=rolls()
   if player_score>=target_score:
    print("The player wine: "+ str(player_score))
    break
   elif computer_score>=target_score:    
    print("The computer win:"+str(computer_score)) 
    break