from math import ceil
import datetime as date

q1 = raw_input("What are you slicing? ")

q2 = raw_input("How many packs of %s do you have? " % q1)

def day_of_week():
  day = date.today().strftime("%A")
  if day == 'Friday' or day == 'Saturday':
    pass

def slice_calc(food, amt):
  if food == "ham":
    leftover = 21 - int(amt)
    result = ceil(leftover / 3)
    return "You need to slice %d hams." % result
  elif food == "turkey":
    fullrows = 18
    leftover = fullrows - int(amt)
    result = ceil(leftover / 1)
    return "You need to slice %d turkeys." % result


print slice_calc(q1, q2)
