import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT model FROM inventory WHERE make='Ford'")

	rows = c.fetchall()

	for r in rows:
		print r[0]
