# ex2.6c.py - JOINing data from multiple tables


import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# retrieve data
	c.execute("""SELECT population.city, population.population, regions.region
			FROM population
			INNER JOIN regions
			ON population.city = regions.city""")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]