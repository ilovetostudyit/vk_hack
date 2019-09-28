import json
class Buildings_class(object):
    def __init__(self, collects_dict):
        self.dict = collects_dict
    def get_building_name(self, object):
        return(self.dict[object]["name"]["ru"])
    def get_building_adress(self, object):
        return(self.dict[object]["adress"]["ru"])
    def get_list_objects(self):
        test_str = ""
        for object in self.dict:
            test_str = test_str + self.get_building_name(object) + ' (' + self.get_building_adress(object) + ') \n'
        json_answer = {}
        json_answer["text"] = test_str
        return(json.dumps(json_answer, ensure_ascii=False,))