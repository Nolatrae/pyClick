from dataclasses import dataclass
from modules.models.executor import Executor
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Building():
    _identify: str = ""
    _name: str = ""
    _desc: str = ""
    _executor: Executor = None
    
    def take_json(self):
        return self.to_json()
    
    def parse_json(self, json_info):
        return self.from_json(json_info)