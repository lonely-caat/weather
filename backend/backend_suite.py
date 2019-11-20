from weather.common.test_suite import TestSuite
from weather.backend.backend_client import BackendClient



class BackendSuite(TestSuite):
    @classmethod
    def setUpClass(cls):
        conf = cls.readConfig()
        cls.client = BackendClient(conf['backend']['host'], conf['backend']['key'])

