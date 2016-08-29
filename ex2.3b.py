# ex2.3b.py - executemany() method


import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# insert multiple records using a tuple
	cars = [
			('Ford', 'Fiesta', 30),
			('Ford', 'Turbo', 20),
			('Ford', 'Traveler', 10),
			('Honda', 'Civic', 40),
			('Honda', 'Accord', 45)
	]


	# insert data into table
	c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)