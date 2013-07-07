import random

heads = 0
tails = 0

def toss():
	if random.random() < .5:
		return 'heads'
	else:
		return 'tails'

if __name__ == '__main__':
	for i in range(100):
		if toss() == 'heads':
			heads += 1
		else:
			tails += 1
	if heads > tails:
		print('heads')
	elif tails > heads:
		print('tails')
	else:
		print('tie') 