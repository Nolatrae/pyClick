from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Contractor():
    _identify: str = ""
    _parent : str = ""
    _name: str = ""
    _desc: str = ""

    def take_json(self):
        return self.to_json()
    
    def parse_json(self, json_info):
        return self.from_json(json_info)
