log_file = 'log.txt'

if __name__ == '__main__':
	log = open(log_file, 'w')
	stuff = input('log: ')
	while not stuff == 'exit':
		log.write(stuff + '\n')
		stuff = input('log: ')
	log.close()