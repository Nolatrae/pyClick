import unittest
from modules.service.repository import repo

class reposity_tests(unittest.TestCase):
    def test_get_acts(self):
        _repo = repo.create()
        
        result = _repo.get_acts()

        assert len(result) > 0
        print(result)