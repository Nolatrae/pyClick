from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Status():
    _identify: str = ""
    _code: int = 0
    _name: str =""
    _desc: str= ""

    @property
    def id(self)->str:
        return self._identify
    
    @id.setter
    def id(self, identify_new:str):
        self._identify = identify_new
    
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, new_code: int):
        self._code = new_code
    
    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self, name_new:str):
        self._name = name_new
    
    @property
    def desc(self)->str:
        return self._desc
    
    @desc.setter
    def desc(self, new_desc):
        self._desc = new_desc

    def take_json(self):
        return self.to_json()
    
    def parse_json(self, json_info):
        return self.from_json(json_info)