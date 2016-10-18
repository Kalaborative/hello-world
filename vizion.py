from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import sys
from time import sleep
print "Status: Initializing Chrome window..."
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://michael-davis-3pcn.squarespace.com/")
print "Status: OK"

print "Status: Clicking blog..."
try:
	myblog = driver.find_element_by_link_text('MY BLOG')
	myblog.click()
	print "Status: OK"
except:
	print "Status: Failed to click blog"
	sys.exit()

try:
	print "Selecting desired blog..."
	blogpost = driver.find_element_by_link_text("The 5 biggest announcements from Google's Pixel event")
	bloglink = blogpost.get_attribute('href')
	blogpost.click()
except Exception as e:
	print "Status: Failed to select desired blog"
	sleep(2)
	print "See message below"
	sleep(2)
	print e
	sys.exit()
print "Status: OK"
data = requests.get(bloglink).text
soup = BeautifulSoup(data, "html.parser")

print "Status: Collecting all text..."
try:
	blocktxt = soup.find_all(attrs={"class": "sqs-block html-block sqs-block-html"})
	print "Status: Text collection success!"
except Exception as e:
	print "Status: Failed to find text"
	sleep(2)
	print "See message below"
	sleep(2)
	print e
	sys.exit()
print "Status: OK"
sleep(2)
print "Status: Closing Chrome..."
driver.quit()
print "Status: done"

print "Status: Writing generated text to a file"
sleep(3)
try:
	with open("blogpost.txt", "wb") as code:
		for b in blocktxt:
			code.write(b.get_text().encode('utf-8'))
except Exception as e:
	print "Error writing the code to a file"
	sleep(2)
	print "See message below"
	sleep(2)
	print e
	sys.exit()

print "Would you like to see the file's contents? (y/n)"
sf = raw_input("> ")
if sf == "y":
	print ("\n" * 100)
	with open("blogpost.txt", "rb") as code:
		post = code.read()
		sentences = post.split('. ')
		for sentence in sentences:
			print sentence
			sleep(8)
			print ("\n" * 100)
