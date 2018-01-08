from random import randint

random_numbers = []

# you can change the number of numbers a participant needs to give below
for i in range(0,3):
  randnum = randint(1,9)
  random_numbers.append(randnum)
  
# this line is for debugging and should be removed once everything is up and running
print(random_numbers)

print('choose 3 numbers between zero  and ten, you have 2 chances' )

print()

chances = 2

while chances > 0:
  response = []
  for i in range(3):
    guess = int(input("what's your  number now? ") )
    if guess not in range(1, 10):
      print("choice not within the given limits")
      print()
      print("kindly pick a number between one and ten")
    
    else:
      response.append(guess)
  
  print (response)
  if response == random_numbers:
    print ("You have hit the Jackpot! ")
    break
    
  chances -= 1
    
else:
    print ("Try again later please!")
