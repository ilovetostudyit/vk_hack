import json
class Buildings_class(object):
    def __init__(self, collects_dict):
        self.dict = collects_dict
    def get_list_objects(self):
        test_str = ""
        for object in self.dict:
            test_str = test_str + self.dict[object]["name"]["ru"] + '\n'
        json_answer = {}
        json_answer["text"] = test_str
        return(json.dumps(json_answer, ensure_ascii=False,))