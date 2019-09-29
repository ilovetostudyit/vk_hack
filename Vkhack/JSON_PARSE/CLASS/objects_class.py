import json
from json_parse.utils import *
import jellyfish
class Objects_class(object):
    def __init__(self, objects_dict):
        self.dict = objects_dict
    def get_object_name(self, object):
        return(self.dict[object]["name"]["ru"])
    def get_object_adress(self, object):
        return(self.dict[object]["adress"]["ru"])
    def get_object_brief(self, object):
        return(self.dict[object]["brief"]["ru"])
    def get_list_objects(self):
        test_str = ""
        for object in self.dict:
            test_str = test_str + self.dict[object]["name"]["ru"] + '\n'
        json_answer = {}
        json_answer["text"] = test_str
        return(json.dumps(json_answer, ensure_ascii=False))
    def object_info(self, object):
        text = self.dict[object]["name"]["ru"]
        if self.dict[object]["year"]:
            text = text + '\n Год создания:' + str(self.dict[object]["year"])
        text = text + '\n' + self.dict[object]["text"]["ru"]
        return(text)
        
    def object_search(self, object_name):
        json_answer = {}
        json_answer["text"] = ""
        max = 0
        tanim_object = 0
        for object in self.dict:
            tanim_coof = jellyfish.jaro_distance(self.get_object_name(object).lower(), object_name.lower())
            if (tanim_coof > max):
                max = tanim_coof
                tanim_object = object
        if (tanim_coof > 0.6):
            json_answer["text"] = "Я уверена это:"
        elif (tanim_coof > 0.4):
            json_answer["text"] = "Мне кажется это:"
        elif (tanim_coof > 0.2):
            json_answer["text"] = "Может быть это:"
        else:    
            json_answer["text"] = wrong_question()
            return(json.dumps(json_answer, ensure_ascii=False,))
        json_answer["text"] = json_answer["text"] + self.object_info(tanim_object)
        return(json.dumps(json_answer, ensure_ascii=False,))