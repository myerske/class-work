smallest = None
largest = None
while True:
	x = input("Enter a number:\n")
	if x == 'Calculate':
		print('Before:', smallest)
		for itervar in (4, 5, 7):
			if smallest is None or itervar < smallest:
				smallest = itervar
			print('Loop:', itervar, smallest)
		print('Smallest:', smallest)

		print('Before:', largest)
		for itervar in (4, 5, 7):
			if largest is None or itervar > largest:
				largest = itervar
			print('Loop:', itervar, largest)
		print('Largest:', largest)