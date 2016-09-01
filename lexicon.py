# First we establish lists that include our words,
direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verb = ['go', 'stop', 'kill', 'eat', 'jump']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
noun = ['door', 'bear', 'princess', 'window']

# Empty list here
my_list = []

def scan(string):
		wordify = str(string)
		phrase = wordify.split()
		del my_list[:]
		for word in phrase:
			if word in direction:
				 my_list.append(('direction', word))
			elif word in verb:
				 my_list.append(('verb', word))
			elif word in stop:
				 my_list.append(('stop', word))
			elif word in noun:
				my_list.append(('noun', word))
			else:
				is_a_number(word)
		return my_list


def is_a_number(s):
		try:
			number = int(s)
			my_list.append(('number', number))
		except ValueError:
			my_list.append(('error', s))		