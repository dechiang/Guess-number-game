# generate a random integer (1~100), do not print
# Let user guess the number
# if the user guess right, print "you are right"
# if the user is wrong, print "the answer is bigger / smaller than your guess"

import random

r = random.randint(0, 100)

print('The answer is an integer from 1 ~ 100')

while True:
	guess = input('Please enter your guess: ')
	guess = int(guess)
	
	if guess == r:
		print('your guess is correct!')
		break
	elif guess >= r:
		print('your guess is bigger than the answer')
	else:
		print('your guess is smaller than the answer')