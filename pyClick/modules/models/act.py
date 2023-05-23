from dataclasses import dataclass
from modules.models.contractor import Contractor
from modules.models.status import Status
from modules.models.building import Building
from modules.models.executor import Executor
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Act():
    _contractor : Contractor = Contractor()
    _executor : Executor = Executor()
    _status : Status = Status()
    _building: Building = Building()

    def take_json(self):
        return self.to_json()

    def parse_json(self, json_info):
        return self.from_json(json_info)