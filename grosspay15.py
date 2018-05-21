hours=int(input('Enter Hours:\n'))
rate=float(input('Enter Rate:\n'))
if hours > 40:
	print("Pay:", hours*(rate*1.5))