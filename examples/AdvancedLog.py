log_file = 'log.txt'

if __name__ == '__main__':
	with open(log_file, 'w') as log:
		stuff = input('log: ')
		while not stuff == 'exit':
			log.write(stuff + '\n')
			stuff = input('log: ')