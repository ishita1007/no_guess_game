import random
print("Welcome to the number guessing game")
number_to_guess= random.randint(1,10)
no_of_tries =1
guess = int(input("please guess the number "))
while number_to_guess!= guess:
  print("Sorry it was not correct guess")
  if no_of_tries== 4:
     break
  elif  number_to_guess<guess:
    print('your guess was greater than the number')
  else:
    print("your guess was lower")
  guess= int(input("please guess again "))
  no_of_tries+=1   
 
if number_to_guess==guess:

    print("Well done you Win!")
    print("you took " + str(no_of_tries)+ " to complete the game")







