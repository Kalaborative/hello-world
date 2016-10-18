from random import choice
from time import sleep


def mixBag():
	q = ["mangoHero1", "Kalaborative", "G6 Gatorix", "MIML_ACA_Andrew", "Andyman9491"]

	print "Assembling bag..."
	sleep(1)
	for qtem in q:
		print "Adding %s to the bag..." % qtem
		sleep(2)
		print "Done"
	print "Pulling an item from the bag..."
	sleep(1)
	gift = choice(q)
	print "The item of choice was %s!" % gift
	return gift
