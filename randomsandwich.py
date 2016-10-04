# Hi. The point of this program is to suggest a sandwich given a specific meat.
# Let's break it down.
from random import choice
meats = ['turkey', 'vito', 'ham', 'cheese', 'beef', 'tuna']

veggies = ['cucumbers', 'hot peppers', 'onions', 'sauce', 'oregano', 'tomatoes', 'lettuce']

condiment = ['dijon', 'mayo', 'jimmy mustard', 'avocado']

modifiers = ['add', 'no', 'extra']

sandwich = ['#1 Pepe', '#2 Big John', '#3 Totally Tuna', '#4 Turkey Tom', '#5 Vito', '#6 Veggie', '#7 Smoked Ham Club', '#8 Billy Club', '#9 Italian Night Club', '#10 Hunters club', '#11 Country Club', '#12 Beach Club', '#13 Veggie Club', '#14 Bootlegger Club', '#15 Club Tuna', '#16 Club Lulu', '#17 Ultimate Porker', 'Gargantuan', 'BLT']

checker = False
a1 = choice(sandwich)
a2 = choice(modifiers)
aa2 = choice(modifiers)
a3 = choice(condiment)
a4 = choice(veggies)
aa4 = choice(veggies)
aaa4 = choice(veggies)
a5 = choice(meats)

sel = raw_input("Choose a meat. \n> ")
if sel == 'ham':
	while checker is False:
		if a2 == modifiers[0] and a3 == condiment[2]:
			a2 = choice(modifiers)
		elif a2 == modifiers[0] and (a4 == 'tomatoes' or a4 == 'lettuce'):
			a2 = choice(modifiers)
			a4 = choice(veggies)
		elif a2 == 'ADD' and (a5 == 'ham' or a5 == 'cheese'):
			a2 = choice(modifiers)
		elif a2 == 'ADD' and a3 == 'mayo':
			a3 = choice(condiment)
		elif a1 != ('#1 Pepe' or '#7 Smoked Ham Club'):
			a1 = choice(sandwich)
		elif a2 == 'no' and (a4 != ('tomatoes' or 'lettuce')):
			a2 == choice(modifiers)
			a4 = choice(veggies)
		elif a2 == 'no' and a3 != 'mayo':
			a2 = choice(modifiers)
		else:
			checker = True


def sandwichprinter():
	re1 = "You should try a " + a1 + " " + a2 + " " + a4 + "."
	re2 = "You should try a " + a1 + " " + a2 + " " + a3 + " " + aa2 + " " + a4 + "."

	responselist = [re1, re2]
	result = choice(responselist)
	print result


sandwichprinter()
