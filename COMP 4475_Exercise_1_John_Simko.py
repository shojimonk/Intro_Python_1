#John Simko
#COMP 4475 FA Exercise #1
#Sept 28th 2015

#Define Functions **********************

def mind_loop(func, *count):
	"""
	takes function ptr and variable values, loops
	until counter reaches 0, passing extra values
	to function, if they exist.
	"""
	guesses = count[0]
#	loops calling passed method until success or max cnt reached
	while guesses > 0:
		print 'You have {} guesses left!'.format(guesses)
		number = raw_input('Enter your number!: ')
		if len(count) > 1:		# if more than one var passed, send extra var to func
			result = func(number, count[1])
			guesses -= result
		else:					# else, just send user input
			result = func(number)
			guesses -= result	
	return number

def validity_check(num_in):
	"""
	Checks if num_in has exactly 5 digits
	and no repeat digits. return 1 if both true.
	"""
	if not num_in.isdigit():
		print "Only numbers are valid entries!"
		return 0
	if len(num_in) != 5:
		print "Invalid number given: not 5 digits."
		return 0
	nums = []
	for digit in num_in:
		if digit in nums:
			print "Invalid number given: digit repeated."
			return 0
		else:
			nums.append(digit)
			continue
	return 1

def digit_matching(num_in, proper_num)
	"""
	Checks if num_in and proper_num have the same digits
	in them, and how many digits are in the same place
	in each. returns 1 for no/partial match. 100 for full match.
	"""
#	calls admin method (ret 0 if rec 0) (bad coupling?)
	result = validity_check(num_in)
	if result == 0:
		return 0
		
#	counts digit matches
	match_cnt = 0
	for char in num_in:
		if char in proper_num:
			match_cnt += 1
	print 'Number of digits in both guess and answer: {}'.format(match_cnt)
#	counts placement matches
	loop = 4
	match_cnt = 0
	while loop >= 0:
		if num_in[loop] == proper_num[loop]:
			match_cnt += 1
		loop -= 1
	print 'Number of digits in correct location: {}'.format(match_cnt)
	if match_cnt == 5:
		print 'Congratulations! You got the number!'
		return 100
	else:
		return 1

		
def flavor_print():
	"""
	Prints basic rules of game.
	"""
	print "Welcome to the MasterMind Number Guessing Game!"
	print "This game consists of players trying to correctly guess a 5-digit"
	print "number which has been set by the Game Master. For each guess, players"
	print "will be told how many digits are in both their guess and the answer, "
	print "as well as how many digits of their guess are in the correct place."
	print "Note: Guesses which are not valid answers will be ignored!"
	return

	#End Functions *************************

#Main Method:
flavor_print()
print "First, we will need a valid MasterMind 5-digit Number."
master_num = mind_loop(validity_check, 1)

print "\n\n\n\n\n\n\n\n\n"*8
flavor_print()
print "We will now begin taking guesses!"
mind_loop(digit_matching, 8, master_num)
print "\nThank you for playing the MasterMind game!"