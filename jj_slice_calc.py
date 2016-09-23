from datetime import date, datetime, timedelta
from random import randint
from sys import exit



fullturkey = 18
fullham = 21
fullvito = 11
fullbeef = 12
fullcheese = 18

terms = ['vito', 'cheese', 'beef', 'turkey', 'ham']


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

def slice_calc(food, amt):
  if food == "ham":
    day_of_week(food)
    leftover = fullham - float(amt)
    result = int(round(leftover / 3))
    is_positive(result)
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

def time_to_slice(num_packs, food):
  #num_packs = int(num_packs)
  if food == 'turkey':
    num_packs *= 6
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
  elif food == 'ham':
    num_packs *= 12
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
  elif food == 'vito':
    num_packs *= 15
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
  elif food == 'beef':
    num_packs *= 16
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)
  elif food == 'cheese':
    num_packs *= 24
    print "It would take about %d minutes to slice %s." % (num_packs, food)
    adj_packs = adjusted_time(num_packs)
    int_packs = int(adj_packs)
    overhour_filter(int_packs)
    is_a_lot(int_packs)

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
  elif ntime >=120 and ntime <= 150:
    ntime = ntime + randint(30, 50)

def factor_load():
  print "Factoring in possible orders..."
  factor = "3..."
  print factor
  i = 0
  while i < 4000000:
    i += 1
  factor = "2..."
  print factor
  while i < 80000000:
    i += 1
  factor = "1..."
  print factor
  while i < 140000000:
    i += 1
  factor = "Done"
  print factor

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

def overhour_filter(n):
  now = datetime.now()
  #n = int(n)
  if n < 59:
    new_now = now + timedelta(minutes = n)
    end_time = new_now.strftime("%I:%M %p")
    factor_load()
    print "You should be done by about %s." % end_time
  elif n >= 59:
    min_v = n % 60
    hour_v = n / 60
    new_now = now + timedelta(minutes = min_v, hours = hour_v)
    end_time = new_now.strftime("%I:%M %p")
    factor_load()
    print "You should be done by about %s." % end_time

def is_positive(n):
  if n < 0:
    print "You have enough! Don't slice anymore."
    exit()

while True:
  q3 = raw_input("Type in your name: ")
  q1 = raw_input("What are you slicing? ")
  q2 = raw_input("How many packs of %s do you have? " % q1)

  if q1 in terms:
    break
  else:
    print "Sorry that food item does not exist! Try again."

slice_calc(q1, q2)

