import sqlite3

with sqlite3.connect("jj_slicing.db") as connection:
  c = connection.cursor()
  c.execute("CREATE TABLE Profiles (Name TEXT, turk FLOAT, ham FLOAT, cheese FLOAT, vito FLOAT, beef FLOAT)")

  # Uncomment the next line and comment out the line above
  # if you need to clear the table.
  # c.execute("DELETE FROM Profiles")
