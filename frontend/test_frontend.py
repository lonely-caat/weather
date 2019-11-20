from weather.frontend.page_object import PageObject

class FrontendTest(PageObject):


    def test_apple(self):
        """
        Steps:
        1. Go to the main page of the application
        2. In the top 'Search' input field enter 'Apple' and hit 'Enter'

        Expected Result:
        Verify 'A common, round fruit produced by the tree Malus domestica, cultivated in temperate climates.'
        string is present in in the word definitions section

        """
        apple_expected_string = 'A common, round fruit produced by the tree Malus domestica, cultivated in temperate climates.'

        self.input_data(self.xpaths['search'], 'apple')

        ## Search for the list of word definitions
        definitions = [x.text for x in self.wd.find_elements_by_xpath(self.xpaths['list_of_definitions'])]
    
        ## Check if the expected string is a part of the ol
        self.assertIn(apple_expected_string, definitions[0], "{0} not found on the page!".format(apple_expected_string))


    def test_pear(self):
        """
        Steps:
        1. Go to the main page of the application
        2. In the top 'Search' input field enter 'Apple' and hit 'Enter'

        Expected Result:
        Verify 'An edible fruit produced by the pear tree, similar to an apple but elongated towards the stem'
        string is present in in the word definitions section

        """

        pear_expected_string = 'An edible fruit produced by the pear tree, similar to an apple but elongated towards the stem'
        self.input_data(self.xpaths['search'], 'pear')

        ## Search for the list of word definitions
        definitions = [x.text for x in self.wd.find_elements_by_xpath(self.xpaths['list_of_definitions'])]

        ## Check if the expected string is a part of the ol
        self.assertIn(pear_expected_string, definitions[0], "{0} not found on the page!".format(pear_expected_string))