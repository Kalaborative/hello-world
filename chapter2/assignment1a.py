"""
So today we're going to be doing our first assignment. This entails making a databse
with 100 integers and then prompting the user to perform a type of aggregation
on them. Let's think of some ways we can accomplish this.

First we need to know how to make a database and populate it with values.

We need to know how to use random integers

We need to know how to ask the user for input

We need to know how to exit the program upon command

We need to know how to use the aggregation methods

I think that's it. Let's expound on these, shall we?
"""

import random
import sqlite3
from sys import exit

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	c.execute("DROP TABLE IF EXISTS nums")
	c.execute("CREATE TABLE nums (num INT)")

	my_randoms = random.sample(xrange(1, 1000), 100)

	i = 0
	while i<100:
		c.execute("INSERT INTO nums values(?)", (my_randoms[i],))
		i += 1


	# we've created the table and populated it.
	# now we need some input.

	while True:

		print "What would you like to do?"
		choice = raw_input("> ")

		if choice == "exit":
			exit()
		elif choice == "average":
			c.execute("SELECT avg(num) FROM nums")

			result = c.fetchone()
			print result[0]
		elif choice == "maximum":
			c.execute("SELECT max(num) FROM nums")

			result = c.fetchone()
			print result[0]
		elif choice == "minimum":
			c.execute("SELECT min(num) FROM nums")
			result = c.fetchone()
			print result[0]
		elif choice == "sum":
			c.execute("SELECT sum(num) FROM nums")
			result = c.fetchone()
			print result[0]
		elif choice == "count":
			c.execute("SELECT count(num) FROM nums")
			result = c.fetchone()
			print result[0]
		else:
			print "I couldn't understand that."
