import random
num = random.randint(1,101)
print("This is a Number Guessing game")
guess = 0
while num != guess:
	guess = int(input("Enter Guess: "))
	

	if num > guess:
		print("Guess higher")
	elif num < guess:
		print("Guess lower")
	else:
		print("You Guessed Right")
