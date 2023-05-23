from dataclasses import dataclass
from modules.models.contractor import Contractor
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Executor():
    _identify : str = ""
    _name: str = ""
    _desc : str = ""
    _contractor : Contractor = None

    def take_json(self):
        return self.to_json()
    
    def parse_json(self, json_info):
        return self.from_json(json_info)