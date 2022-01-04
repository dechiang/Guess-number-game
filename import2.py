# generate a random integer (1~100), do not print
# Let user guess the number
# if the user guess right, print "you are right"
# if the user is wrong, print "the answer is bigger / smaller than your guess"

import random

start = input('please enter a start integer: ')
end = input('please enter an end integer: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

print('The answer is an integer from', start, 'to', end)

while True:
	count += 1 # count = count + 1
	guess = input('Please enter your guess: ')
	guess = int(guess)
	if guess == r:
		print('your guess is correct!')
		print('you have guessed', count, 'times')
		break
	elif guess >= r:
		print('your guess is bigger than the answer')
	else:
		print('your guess is smaller than the answer')
	print('you have guessed', count, 'times')