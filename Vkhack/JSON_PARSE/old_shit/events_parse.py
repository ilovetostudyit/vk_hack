import json 
from base_struct import *

sponsor_struct = {
    "id":"",
    "spcategory": text_description_struct    
}

sponsors_list_struct = {}
dict_init(sponsors_list_struct, 500, 's', sponsor_struct)

within_struct = {
     "id": 11869,
    "name": text_description_struct,
    "mainfoto": simple_str_struct,
    "path": "",
    "dateBegin": "",
    "dateEnd": "",
    "type": text_description_struct 
}
within_list_struct = {}
within_list_struct(within_list_struct, 500, 'w', within_struct) 

event_struct = {
        "path": "",
        "m_parent_id": "",
        "img_mob": "",
        "img_pc": "",
        "img_header": pc_mob_str_struct,
        "dateBegin":"",
        "dateEnd":"",
        "type":text_description_struct,
        "age":"",
        "ticket":"",
        "name": text_description_struct,
        "headimg": text_description_struct,
        "text": text_description_struct,
        "addtext":text_description_struct,
        "date":text_description_struct,
        "halls":text_description_struct,
        "price":text_description_struct,
        "audioguide":text_description_struct,
        "mediaguide":text_description_struct,
        "searcha":text_description_struct,
        "seakeys":text_description_struct,
        "building": just_id_struct,
        "gallery": gallery_list_struct,
        "circ_img": simple_str_struct,
        "files": "",
        "sponsors": sponsors_list_struct,
        "shop": just_id_struct,
        "connect": "",
        "ab_event": "",
        "within": within_list_struct,
        "mapurl": ""        
}

events_dict = {}
dict_init(events_dict, 500, 'e', event_struct)       

with open('../JSON/events.json', 'r', encoding="utf8") as f:
    events_dict = json.load(f)
#try:
#   for event in (events_dict):
#        print(events_dict[event]["name"]["ru"])
#except Exception as E:
#    print(E)