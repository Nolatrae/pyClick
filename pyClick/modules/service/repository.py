from modules.models.act import Act
from modules.models.executor import Executor
from modules.models.contractor import Contractor
from modules.service.proxy import db_proxy
from modules.models.building import Building

class repo():
    __acts = []
    __buildings = []
    __executors = []
    __contractors = []
    __proxy = None

    def __init__(self):
        self.__proxy = db_proxy()
        self.__proxy.create()

    # Методы данных    

    def get_acts(self):
        return self.__acts

    def take_acts_json(self):
        processed_acts = []
        for i in self.get_acts():
            processed_acts.append(i.to_json())
        return {"acts" : processed_acts}


    
    def get_buildings(self):
        return self.__buildings
    
    def get_executors(self):
        return self.__executors
    
    def get_contractors(self):
        return self.__contractors
        


    def load(self):
        self.__acts = []
        self.__buildings = []
        self.__executors = []
        self.__contractors = []

        contractor_parent = Contractor(_name="test1", _parent=None)
        contractor_act = Contractor(_name="test2", _parent=contractor_parent)
        executor_act = Executor(_name="test3", _contractor=contractor_act)
        building_act = Building(_name="test4")
        current_act = Act(_executor=executor_act, _building=building_act)

        self.__acts.append(current_act)


    def create():
        main = repo()
        main.load()

        return main

    

        
