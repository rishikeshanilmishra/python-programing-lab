import random
game_start = input("Would you like to roll the dice?")   # take input from the user
def dice_roll():  # define a function for rolling a dice
 print("Your number is: " + str(random.randint(1,6)))   #using random function function, it will pick any of the six numbers
 global play_again 
 play_again = input("Would you like to play again?")   # if user wants to play again
if game_start == "yes":
 dice_roll() 
 while play_again == "yes":
  dice_roll()
elif game_start == "no": # the game will continue to roll the dice until you input 'no' or some other input
 print("Game Over")
else: print("Input not recognized")
