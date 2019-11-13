from selenium import webdriver


baseurl = "https://en.wiktionary.org/"
apple_expected_string = 'A common, round fruit produced by the tree Malus domestica, cultivated in temperate climates.'
pear_expected_string = 'An edible fruit produced by the pear tree, similar to an apple but elongated towards the stem'


xpaths = { 'search' : '//*[@name="search"]',
           'list_of_definitions' : "//ol",
           'submitButton' :   "//input[@name='login']"
         }
## Fire it up! 
mydriver = webdriver.Chrome()
mydriver.get(baseurl)

## First search input is ok
mydriver.find_element_by_xpath(xpaths['search']).send_keys("apple")
## hit that 'Enter' button
mydriver.find_element_by_xpath(xpaths['search']).send_keys(u'\ue007')
## we have a HTML ordered list let's convert it to python list of strings 
definitions = [x.text for x in mydriver.find_elements_by_xpath(xpaths['list_of_definitions'])]

## Check if the expected string is a part of the ol
assert apple_expected_string in definitions[0], "{0} not found on the page!".format(apple_expected_string)

## go back to main page and repeat all the steps for the pear 
mydriver.get(baseurl)
mydriver.find_element_by_xpath(xpaths['search']).send_keys("pear")
mydriver.find_element_by_xpath(xpaths['search']).send_keys(u'\ue007')
definitions = [x.text for x in mydriver.find_elements_by_xpath(xpaths['list_of_definitions'])]

assert pear_expected_string in definitions[0], "{0} not found on the page!".format(pear_expected_string)

print("Done!")
mydriver.quit()
