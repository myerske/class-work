total = 0
count = 0
while True:
	try:
		x = int(input("Enter a number:\n"))
	except:
		print('Invalid Number')	
if x == 'Calculate':
	for itervar in [4, 5, 7]:
		total = total + itervar
	print('Total:', total)
	for itervar in [4, 5, 7]:
		count = count + 1
	print('Count:', count)
	print('Average:', total/count)