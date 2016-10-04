# Well... let's begin. *cracks knuckles*
# import our necessary modules
from datetime import date, datetime, timedelta
from random import randint
from sys import exit
import sqlite3
import facebook

# NOTE: MAKE SURE TO RUN sqlite3_db_profiles.py BEFORE RUNNING THIS CODE
# OTHERWISE THE PROFILE FEATURE WILL NOT WORK ! ! !


# define our global variables
# In this case, we set these to what we believed would be
# completely full slicing levels, by pack.
fullturkey = 18
fullham = 21
fullvito = 11
fullbeef = 12
fullcheese = 18

# A list of terms the calculator will accept
# This also describes the specific order in which to insert the values.
terms = ['turkey', 'ham', 'cheese', 'vito', 'beef']

profiles = []
sliceload = []
slicetime = []

# Depending on the weekday, different slicing levels are observed.
# This is why this function is necessary.


def day_of_week(food):
  day = date.today().strftime("%A")
  if (day == 'Friday' or day == 'Saturday') and food == 'turkey':
    print "Today is %s which means you need to slice 2 rows." % day
    global fullturkey
    fullturkey -= 6
  elif food == 'turkey':
    print "Today is %s which means you need to slice 3 rows." % day
  elif (day == 'Friday' or day == 'Saturday') and food == 'ham':
    print "Today is %s which means you need to slice 2 rows." % day
    global fullham
    fullham -= 7
  elif food == 'ham':
    print "Today is %s which means you need to slice 3 rows." % day
  elif (day == 'Friday' or day == 'Saturday') and food == 'vito':
    print "Today is %s which means you need to slice 1.5 rows." % day
    global fullvito
    fullvito -= 4
  elif food == 'vito':
    print "Today is %s which means you need to slice 2 rows." % day
  elif (day == 'Friday' or day == 'Saturday') and food == 'beef':
    print "Today is %s which means you need to slice 1 row." % day
    global fullbeef
    fullbeef -= 6
  elif food == 'beef':
    print "Today is %s which means you need to slice 2 rows." % day
  elif (day == 'Friday' or day == 'Saturday') and food == 'cheese':
    print "Today is %s which means you need to slice 2 rows." % day
    global fullcheese
    fullcheese -= 6
  elif food == 'cheese':
    print "Today is %s which means you need to slice 3 rows." % day


# This be the big function.
def slice_calc(food, amt):
  if food == "ham":
    day_of_week(food)
    leftover = fullham - float(amt)  # Why float? Because we're rounding numbers.
    result = int(round(leftover / 3))  # Rounding an integer would be kinda pointless.
    is_positive(result)               # Wouldn't it?
    print "You need to slice %d hams." % result
    time_to_slice(result, food)
  elif food == "turkey":
    day_of_week(food)
    leftover = fullturkey - float(amt)
    result = int(round(leftover / 1))
    is_positive(result)
    print "You would need to slice about %d turkeys." % result
    time_to_slice(result, food)
  elif food == "vito":
    day_of_week(food)
    leftover = fullvito - float(amt)
    result = int(round(leftover / 3))
    is_positive(result)
    print "You need to slice %d salami and capicola." % result
    time_to_slice(result, food)
  elif food == "beef":
    day_of_week(food)
    leftover = fullbeef - float(amt)
    result = int(round(leftover / 3))
    is_positive(result)
    print "You need to slice %d hunks of roast beef." % result
    time_to_slice(result, food)
  elif food == "cheese":
    day_of_week(food)
    leftover = fullcheese - float(amt)
    result = int(round(leftover / 3))
    is_positive(result)
    print "You need to slice %d logs of cheese." % result
    time_to_slice(result, food)

# This function approximates the time it takes to slice a meat.
# Note that this means NO DISTRACTIONS WHATSOEVER!


def time_to_slice(num_packs, food):
  if food == 'turkey' and q3 in profiles:
    num_packs *= slicetime[0][0]
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)  # Shit happens. That's why we need an ADJUSTED time.
    int_packs = int(adj_packs)
    overhour_filter(int_packs)  # I'll explain this later.
    is_a_lot(int_packs)  # This too.
    keep_running()
  elif food == 'turkey':
    num_packs *= 6
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()
  elif food == 'ham' and q3 in profiles:
    num_packs *= slicetime[0][1]
    print "It would take about %r minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()
  elif food == 'ham':
    num_packs *= 12
    print "It would take about %r minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()
  elif food == 'cheese' and q3 in profiles:
    num_packs *= slicetime[0][2]
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()
  elif food == 'cheese':
    num_packs *= 24
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()
  elif food == 'vito' and q3 in profiles:
    num_packs *= slicetime[0][3]
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()
  elif food == 'vito':
    num_packs *= 15
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()
  elif food == 'beef' and q3 in profiles:
    num_packs *= slicetime[0][4]
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()
  elif food == 'beef':
    num_packs *= 16
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
    keep_running()


# So the concept of this is given any duration of time, in minutes,
# how likely would it be for an order to just pop in once or twice.
# This would be EXTREMELY difficult to do, so I simply guestimated
# by applying a small but random amount of minutes to our time.
def adjusted_time(ntime):
  if ntime < 10:
    ntime = ntime + randint(1, 4)
    return ntime
  elif ntime >= 10 and ntime < 30:
    ntime = ntime + randint(6, 14)
    return ntime
  elif ntime >= 30 and ntime < 60:
    ntime = ntime + randint(12, 19)
    return ntime
  elif ntime >= 60 and ntime < 91:
    ntime = ntime + randint(20, 38)
    return ntime
  elif ntime >= 91 and ntime < 120:
    ntime = ntime + randint(26, 44)
    return ntime
  else:
    ntime = ntime + randint(30, 50)
    return ntime


# A completely fake but showoff-y loading simulator.
def factor_load():
  print "Establishing a connection with the server..."
  i = 0
  while i < 9000000:
    i += 1
  factor = "Plotting previous sales data..."
  print factor
  i = 0
  while i < 9900000:
    i += 1
  factor = "Measuring average statistics..."
  print factor
  i = 0
  while i < 7500000:
    i += 1
  factor = "Running algorithms to predict projections..."
  print factor
  i = 0
  while i < 9300000:
    i += 1
  factor = "Done"
  print factor

# How much is "a lot"? Well wouldn't you like to know!


def is_a_lot(n):
  if n < 35:
    print "Lucky for you, %s, there's not a lot you have to do. Whoopee!" % q3
  elif n >= 35 and n < 50:
    print "Looks like you have quite a bit of slicing to do, %s. " % q3
  elif n >= 50 and n < 80:
    print "This might take a while but it shouldn't be overwhelming, %s." % q3
  elif n >= 80 and n < 110:
    print "You've got some serious work to do, %s. Chop chop!" % q3
  elif n >= 110:
    print "You have a LOT of slicing to do, %s! I'd get movin'!" % q3


# So unfortunately the way the timedelta object works, it maxes out at 59 minutes.
# So for every adjusted time over that, I have to dissect it into hours and minutes.
# Fortunately, that wasn't very hard to figure out.
def overhour_filter(n):
  now = datetime.now()
  if n < 59:
    new_now = now + timedelta(minutes=n)
    end_time = new_now.strftime("%I:%M %p")
    factor_load()
    print "You should be done by about %s." % end_time
  elif n >= 59:
    min_v = n % 60
    hour_v = n / 60
    if min_v == 0:
      min_v = min_v + 1
    new_now = now + timedelta(minutes=min_v, hours=hour_v)
    end_time = new_now.strftime("%I:%M %p")
    factor_load()
    print "You should be done by about %s." % end_time


# This basically prevents the program from saying something like..
# "you need to slice -4 turkeys."
# In other words, it's already full dipshit.
def is_positive(n):
  if n < 0:
    print "You have enough! Don't slice anymore."
    byebye = raw_input("Press enter to exit.")
    exit()


# I had to invent this so that file wouldn't just
# immediately close once it reached the end of the file.
def keep_running():
  run = raw_input("Would you like to continue? Enter y or n: ")
  if run == 'y' or run == 'Y':
    reset_stockvalue()
    slicing_helper()
  elif run == 'n' or run == 'N':
    print "Would you like to post a status of your hard work on the Jimmy John's Facebook page?"
    fbp = raw_input("> ")
    if fbp == "y":
      fb_post_update()
      byebye = raw_input("Thanks for using my program! \nHit Enter to exit.")
      exit()
    else:
      byebye = raw_input("Thanks for using my program! \nHit Enter to exit.")
      exit()
  else:
    print "Type y or n."
    keep_running()


def reset_stockvalue():
  global fullturkey
  fullturkey = 18
  global fullham
  fullham = 21
  global fullvito
  fullvito = 11
  global fullbeef
  fullbeef = 12
  global fullcheese
  fullcheese = 18

def fb_post_update():
  fdsliced = raw_input("What food did you slice today? ")
  cms = raw_input("Add a custom message to your status! ")
  justfin = "Our rock star, %s, just finished slicing " % q3
  status = justfin + fdsliced + "! " + cms
  
  my_token = "EAAN7unK1SmkBAKwXN1A9qfxU76AoVuqTURSDEWmfsnmcH3mX0JlRlOku4loy5IHpHZBtCHezaiDyQ5Pm6T2mAZB0jbuDMNdthZAFujg1gxPvMVq8LtgZAm4V7vAfKladj99gA9sS9Np37iIzWJUkhPFgJAt19HVoISqFZBaYRUwZDZD"
  my_id = "1664030033909655"
  graph = facebook.GraphAPI(access_token=my_token)
  graph.put_object(parent_object=my_id, connection_name='feed', message=status)
  
  print "Status posted! You can visit the page at https://www.facebook.com/jjsirving/"
  
def profile_loader(name):
  sliceload.append(name)
  print "On average, how many minutes does it take to slice 1 turkey?"
  print "If you don't know, guess."
  print "Decimals are accepted."
  tur = raw_input("> ")
  sliceload.append(tur)
  print "Ham?"
  ham = raw_input("> ")
  sliceload.append(ham)
  print "Cheese?"
  chz = raw_input("> ")
  sliceload.append(chz)
  print "And vito?"
  vit = raw_input("> ")
  sliceload.append(vit)
  print "Beef?"
  bf = raw_input("> ")
  sliceload.append(bf)

  with sqlite3.connect("jj_slicing.db") as connection:
    c = connection.cursor()

    c.execute("INSERT INTO Profiles VALUES(?, ?, ?, ?, ?, ?)", sliceload)
  print "Profile complete! Successfully updated database."


def slice_dump(person):
  prof = []
  prof.append(person)
  with sqlite3.connect("jj_slicing.db") as connection:
    c = connection.cursor()
    c.execute("SELECT turk,ham,cheese,vito,beef FROM Profiles WHERE Name=?", prof)
    slicedump = c.fetchall()
    for s in slicedump:
      slicetime.append(s)


# The main function that makes it run infinitely unless told otherwise.


def slicing_helper():
  while True:
    q1 = raw_input("What are you slicing? ")
    q2 = raw_input("How many packs of %s do you have? " % q1)

    if q1 in terms:
      slice_calc(q1, q2)
    else:
      print "Sorry that food item does not exist! Try again."

# We like to you by name, i guess.


q3 = raw_input("Type in your name: ")
with sqlite3.connect("jj_slicing.db") as connection:
  c = connection.cursor()

  c.execute("SELECT * FROM Profiles")
  rows = c.fetchall()

  for r in rows:
     profiles.append(r[0])

if q3 in profiles:
  slice_dump(q3)
  print "%s has a profile! Profile loaded." % q3
else:
  print "You don't have a profile. Would you like to make one now? Y/N"
  response = raw_input("> ")
  if response == "y" or response == "Y":
    profile_loader(q3)
    slice_dump(q3)
  else:
    slicing_helper()
# That's it. k bye.
slicing_helper()
