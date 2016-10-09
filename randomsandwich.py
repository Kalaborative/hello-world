# Hi. The point of this program is to suggest a sandwich given a specific meat.
# Let's break it down.
from random import choice
meats = ['turkey', 'vito', 'ham', 'cheese', 'beef', 'tuna']

veggies = ['cucumbers', 'hot peppers', 'onions', 'sauce', 'oregano', 'tomatoes', 'lettuce']

condiment = ['dijon', 'mayo', 'jimmy mustard', 'avocado']

modifiers = ['add', 'no', 'extra', 'easy']

sandwich = ['#1 Pepe', '#2 Big John', '#3 Totally Tuna', '#4 Turkey Tom', '#5 Vito', '#6 Veggie', '#7 Smoked Ham Club', '#8 Billy Club', '#9 Italian Night Club', '#10 Hunters Club', '#11 Country Club', '#12 Beach Club', '#13 Veggie Club', '#14 Bootlegger Club', '#15 Club Tuna', '#16 Club Lulu', '#17 Ultimate Porker', 'Gargantuan', 'BLT']


def sandwichprinter():
	re1 = "You should try a " + a1 + " " + a2 + " " + a4 + "."
	re2 = "You should try a " + a1 + " " + a2 + " " + a3 + " " + aa2 + " " + a4 + "."
	re3 = "You should try a " + a1 + " with " + a4 + " and " + a2 + " " + aa4 + "."

	responselist = [re1, re2, re3]
	result = choice(responselist)
	print result


sel = raw_input("Choose a meat. \n> ")

i = 1
while i != 10:
	checker = False
	a1 = choice(sandwich)
	a2 = choice(modifiers)
	aa2 = choice(modifiers)
	a3 = choice(condiment)
	a4 = choice(veggies)
	aa4 = choice(veggies)
	aaa4 = choice(veggies)
	a5 = choice(meats)

	if sel == 'ham':
		while checker is False:
			if a2 == 'add' and a3 == 'mayo':
				a3 = choice(condiment)
			elif a2 == "add" and (a4 == 'tomatoes' or a4 == 'lettuce'):
				a2 = choice(modifiers)
			elif a2 == 'add' and (a5 == 'ham' or a5 == 'cheese'):
				a2 = choice(modifiers)
			elif a2 == 'add' and a3 == 'mayo':
				a3 = choice(condiment)
			elif a1 in ['#2 Big John', '#3 Totally Tuna', '#4 Turkey Tom', '#5 Vito', "#6 Veggie", "#10 Hunters Club", "#12 Beach Club", "#13 Veggie Club", "#14 Bootlegger Club", "#15 Club Tuna", "#16 Club Lulu", "BLT"]:
				a1 = choice(sandwich)
			elif a1 == 'Italian Night Club' and ((a2 == 'add' or aa2 == 'add') and (a4 == 'onion' or (a4 == 'sauce' or aa4 == 'sauce') or a4 == 'oregano')):
				a2 = choice(modifiers)
			elif (a2 == 'add' and a4 == 'lettuce') or (a2 == 'add' and aa4 == 'lettuce'):
				a2 = choice(modifiers)
				a4 = choice(veggies)
			elif a2 == 'no' and a3 != 'mayo':
				a3 = choice(condiment)
			elif a1 in ['#1 Pepe', '#7 Smoked Ham Club', '#11 Country Club', '#8 Billy Club', '#17 Ultimate Porker'] and ((a2 == 'no' or aa2 == 'no') and a4 in ['hot peppers', 'onions', 'sauce', 'oregano']):
				a2 = choice(modifiers)
			elif a2 == 'no' and a4 == 'cucumbers':
				a2 = choice(modifiers)
				a4 = choice(veggies)
			elif a2 == 'add' and aa4 == 'lettuce':
				aa4 = choice(veggies)
			elif (a1 == '#9 Italian Night Club' or a1 == "Gargantuan") and (aa2 == 'add' and aa4 == 'onions'):
				aa2 = choice(modifiers)
			else:
				checker = True
	sandwichprinter()
	i += 1
