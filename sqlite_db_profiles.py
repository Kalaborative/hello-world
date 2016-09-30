import sqlite3

with sqlite3.connect("jj_slicing.db") as connection:
  c = connection.cursor()
  c.execute("CREATE TABLE Profiles (Name TEXT, turk FLOAT, ham FLOAT, cheese FLOAT, vito FLOAT, beef FLOAT)")
  