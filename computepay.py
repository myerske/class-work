def computepay(hours,rate):
	pay=hours*rate
	if hours <= 40:
		print("Pay:", hours*rate)
	if hours > 40:
		print("Pay:", hours*(rate*1.5))
		
computepay(45, 10)