import unittest
from modules.service.repository import repo
from modules.models.act import Act

class json_tests(unittest.TestCase):
    def test_take_json_acts(self):
        _repo = repo.create()
        act = _repo.take_acts_json()["acts"][0]
        no_act = Act().parse_json(act).take_json()
        assert act == no_act
        assert len(act) == len(no_act)

    