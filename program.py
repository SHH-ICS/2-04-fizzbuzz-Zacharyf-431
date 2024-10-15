# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

for myNumber in range(1, 33):
  if myNumber % 3 == 0 and myNumber % 5 == 0:
    print ("Fizzbuzz")
  elif myNumber % 3 == 0:
    print ("Fizz")
  elif myNumber % 5 == 0:
    print ("Buzz")
  else:
    print (myNumber)
