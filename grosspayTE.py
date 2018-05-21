inp=input('Enter Hours:\n')
try:
	hours=int(inp)
	rate=int(input('Enter Rate:\n'))
	print('Pay:',hours*rate)
except:
	print('Please enter a number')
