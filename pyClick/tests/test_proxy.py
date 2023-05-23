import unittest
from modules.service.proxy import db_proxy

class proxy_tests(unittest.TestCase):
    def test_connect_database(self):
        proxy = db_proxy()

        proxy.create()

        print(proxy.error_text)
        assert proxy.error_text == ""
        assert proxy.is_error == False

    
