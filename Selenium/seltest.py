from selenium import webdriver
from time import sleep

# Create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_name("q")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
txts = driver.find_elements_by_xpath('//*[@class="g"]//h3/a')

print "The automation was a success!"
sleep(2)
print "It found " + str(len(txts)) + " searches."
sleep(2)
print ("\n" * 100)
print "Displaying results:"

# iterate through each element and print the text that is
# name of the search
i = 0
while (i < 10):
	for t in txts:
		print "Title: ", t.text
		print "Link: ", t.get_attribute('href')
		print
		i += 1
		sleep(3)

driver.quit()
