try:
	score=float(input('Enter your score:\n'))
	if score >= 0.9 and score <= 1.0:
		print('Grade: A')
	if score >= 0.8 and score < 0.9:
		print('Grade: B')
	if score >= 0.7 and score < 0.8:
		print('Grade: C')
	if score >= 0.6 and score < 0.7:
		print('Grade: D')
	if score >= 0.0 and score < 0.6:
		print('Grade: F')
	if score < 0.0:
		print('Invalid Score')
	if score > 1.0:
		print('Invalid Score')
except:
	print('Invalid Score')