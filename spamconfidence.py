fname = input('Enter File Name:')
fhand = open(fname)

count = 0
total = 0

for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):
		count = count + 1
		colonpos = line.find(':')
		decimal = line[colonpos + 1: ]
		decimal = decimal.strip()
		decimal = float(decimal)
		total = total + decimal
print('Average Spam Confidence:', total/count)