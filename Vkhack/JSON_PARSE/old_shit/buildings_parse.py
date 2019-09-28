import json 
from base_struct import *


halls_struct = {
    "path": "",
    "number":"",
    "img":"",
    "img_header": pc_mob_str_struct,
    "virtual_tour": virtual_tour_preview,
    "exposition": simple_str_struct,
    "satellites": simple_str_struct,
    "name": text_description_struct,
    "short": text_description_struct,
    "text": text_description_struct,
    "searcha": text_description_struct,
    "seakeys": text_description_struct
    
}

halls_list_struct = {}
dict_init(halls_list_struct, 500, 'h', halls_struct)

floor_struct = {
    "path": "",
    "number": "",
    "name": text_description_struct,
    "plan": "", 
    "halls": halls_list_struct      
}

floors_list_struct = {}
dict_init(floors_list_struct, 500, 'f', floor_struct)

exposition_struct = {
    "path": "",
    "img": "",
    "img_header": pc_mob_str_struct,
    "circ_img": "",
    "virtual_tour": virtual_tour_preview,
    "satelites": simple_str_struct,
    "name": text_description_struct,
    "searcha": text_description_struct,
    "seakeys": text_description_struct,
    "halls_list_header": text_description_struct,
    "halls_list": []    
}
exposition_list_struct = {}
dict_init(exposition_list_struct, 500, 'exp', exposition_struct)  

building_struct = {"m_sort": "",
                   "path": "",
                   "closed": "",
                   "schedule": shedule_struct,
                   "ticket": "",
                   "picture": "",
                   "yamapcoords": "",
                   "appl_number": "",
                   "appl_number_tablet": "",
                   "img_header": img_header_struct,
                   "img": simple_str_struct,
                   "name": text_description_struct,
                   "menu":text_description_struct,
                   "brief": text_description_struct,
                   "text": text_description_struct,
                   "textmore":text_description_struct,
                   "adress": text_description_struct,
                   "timeline":text_description_struct,
                   "rate": text_description_struct,
                   "tel": text_description_struct,
                   "excursions":text_description_struct,
                   "invalid": text_description_struct,
                   "rules": text_description_struct,
                   "audiog": text_description_struct,
                   "searcha": text_description_struct,
                   "seakeys": text_description_struct,
                   "panorama":"",
                   "virtual_tour": virtual_tour_preview,
                   "floors": floors_list_struct,
                   "exposition": exposition_list_struct
}
buildings_dict = {}
dict_init(building_dict, 500, 'd', building_struct)    

with open('../JSON/buildings.json', 'r', encoding="utf8") as f:
    buildings_dict = json.load(f)
#
#try:
#    for building in (buildings_dict):
#        print(buildings_dict[building]["name"]["ru"])
#        for floor in buildings_dict[building]["floors"]:
#            print(" -" + buildings_dict[building]["floors"][floor]["name"]["ru"])
#except Exception as E:
##    print(E)