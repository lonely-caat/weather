import unittest
import os
import configparser

class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    @staticmethod
    def readConfig():
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        config_file = __location__ + '/' + 'config.ini'
        cp  = configparser.ConfigParser()
        cp.read(config_file)

        return cp