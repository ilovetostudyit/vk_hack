import json 
from base_struct import *
        
period_struct = {
    "name": text_description_struct,
    "text": text_description_struct    
}

collector_struct = {
    "auth_year": "",
    "ru": "",
    "en": ""
}

collectors_list_struct = {}
dict_init(collectors_list_struct, 500, 'collector', collector_struct) 

object_struct = {
        "path": "",
        "m_parent_id": "", 
        "year": 0,
        "get_year": "",
        "inv_num": "",
        "type": text_description_struct,
        "country": text_description_struct,
        "period": period_struct,
        "paint_school": "",
        "graphics_type": "",
        "department": "",
        "masterpiece": "",
        "show_in_hall": "",
        "show_in_collection": 0,
        "name":text_description_struct,
        "namecom": text_description_struct,
        "size": text_description_struct,
        "text": text_description_struct,
        "annotation": text_description_struct,
        "litra": text_description_struct,
        "restor": text_description_struct,
        "audioguide":text_description_struct,
        "videoguide": text_description_struct,
        "link": text_description_struct,
        "linktext": text_description_struct,
        "producein": text_description_struct,
        "material": text_description_struct,
        "from": text_description_struct,
        "matvos": text_description_struct,
        "sizevos": text_description_struct,
        "prodcast": text_description_struct,
        "searcha": text_description_struct,
        "seakeys": text_description_struct,
        "hall": "",
        "building": "",
        "gallery": gallery_list_struct,
        "authors": "", 
        "collectors": collectors_list_struct,
        "cast": "0",
        "shop": "",
        "sortID": 0
}

objects_dict = {}
dict_init(objects_dict,500, 'o', object_struct)

#
class Object_class(object):
    def __init__(self, objects_dict):
        self.dict = objects_dict
    def get_list_objects(self):
        for object in (objects_dict):
            print(objects_dict[object]["name"]["ru"])
            
with open('../JSON/objects.json', 'r', encoding="utf8") as f:
   objects_dict = json.load(f)
try:
    museum_objects = Object_class(objects_dict)
    museum_objects.get_list_objects()
except Exception as E:
    print(E)

