'''Python as a calculator'''
# very short mess around time

2 + 2
2 - 2
2 * 2
5 / 2

# lets use assert to test
assert 2 + 2 == 4
assert 2 - 2 == 0
assert 5 / 2 == 2.5 # this will cause an error, we'll come back to this later

# operators
2 + 2
2 - 2
2 * 2
2 / 2
2 ** 2

# side note, ignore if python 3
# so remember when we tried assert 5/2 and it caused
# an error? according to the interpreter 5 / 2 == 2?
assert 5 / 2 == 2
# it is rounded down
# lets talk a little about types...
assert 5.0 / 2.0 == 2.5 # it works now!
assert float(5)/float(2) == 2.5
# ... yeah we'll talk about that later

'''Variables'''
# short mess around time
dude_age = 9001
lol = 'ITS OVER 9000!!!!!!!!!!'
welcome = 'Hello'
welcome = welcome + ' world!'

assert welcome == 'Hello world!'

# talk about +=
a = 10
a += 1
assert a == 11

'''Modules & Functions'''
import random

random.randint(0, 9)

# lets incorporate some variables...
small = 0
big = 10
random.randint(small, big) 
random.random()
###################################

import math

yum = math.pi
assert math.cos(yum) == -1
assert math.sin(yum) == 0
math.tan(yum) == 
assert math.sqrt(yum**2) == yum

'''Control Flow'''
# moderate-lots of time to mess around
# talk about ' vs "
meme = 'do u even'
meme = meme + ' lift bro??'

assert meme == 'do u even lift bro??'

if meme == 'do u even lift bro??':
	print('lolyes')
else:
	print('Y U NO APPLE PIE???')

# lets introduce logic, kids

do_u_even_lift_bro = 'yes'
no_ur_meme = 'maybe'

if no_ur_meme == 'yes' or do_u_even_lift_bro == 'yes':
	print('ur k')
elif no_ur_meme == 'maybe':
	print('KNOWURMEMEZKIDZ')
else:
	print('Y U NO NO UR MEMEZ?')

if no_ur_meme == 'yes' and do_u_even_lift_bro == 'yes':
	print('omg ur 2 amazing 4 skul')

if not no_ur_meme == 'no':
	print('ts gud 2 no ur memez gud j0b')
##########################################

# loops
for i in range(10):
	print(i)

for i in range(10):
	print('this is the ' + i + ' time this has been printed')

i = 0
while i < 10:
	print(i)
	i += 1
assert i == 10

while True:
	text = raw_input('DOUNOURMEME? ')
	if text == 'yes':
		print('ok i can stop now')
		break

'''Functions'''
# lots of time to mess around
def this_is_a_function(this_is_an_argument):
	print(this_is_an_argument)
this_is_a_function('hi')

def hello_world():
	return 'hello world'
assert hello_world() == 'hello world'

def loopalot(times):
	for i in range(times):
		print('time ' + i)
loopalot(6)