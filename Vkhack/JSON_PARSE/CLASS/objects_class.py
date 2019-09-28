import json
class Objects_class(object):
    def __init__(self, objects_dict):
        self.dict = objects_dict
    def get_list_objects(self):
        test_str = ""
        for object in self.dict:
            test_str = test_str + self.dict[object]["name"]["ru"] + '\n'
        json_answer = {}
        json_answer["text"] = test_str
        return(json.dumps(json_answer, ensure_ascii=False))