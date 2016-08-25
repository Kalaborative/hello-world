# Make a list of tuples stored in 'records'
records = [
	('foo', 1, 2),
	('bar', 'hello'),
	('foo', 3, 4)
]

# Defining a function and their variables
def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print('bar', s)


# This for-loop iterates through records using two parameters
for tag, *args in records: # Notice how *args is set to a whatever is after
	if tag == 'foo':       # the first string in the tuples.
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)