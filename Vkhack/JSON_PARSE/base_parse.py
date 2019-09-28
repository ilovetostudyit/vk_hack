import json
from CLASS.buildings_class import *
from CLASS.objects_class import *
from CLASS.events_class import *
from CLASS.collects_class import *
from CLASS.museum_class import *

def base_navigation():
    museum = Museum_class()
    museum.buildings, museum.objects, museum.collects, museum.events = init_navigation()
    return(museum)

def dict_init(the_dict, n, str, fill_struct):
    i = 1
    while (i < n):
        the_dict[str + '%s' %(i)] = fill_struct
        i = i + 1
    return(the_dict)

def init_navigation():
    just_id_struct = {
        "id":""
    }

    time_shedule_struct = {
        "timebegin": "0",
        "timeend": "0"
    }

    regular_shedule_struct = {
        "sun": time_shedule_struct,
        "mon": time_shedule_struct,
        "tue": time_shedule_struct, 
        "wed": time_shedule_struct,
        "thu": time_shedule_struct,
        "fri": time_shedule_struct,
        "sat": time_shedule_struct,
    }
    exception_shedule_struct = {
        "date": time_shedule_struct
    }
    shedule_struct = {
        "regulars": regular_shedule_struct,
        "exceptions": exception_shedule_struct 
    }

    simple_str_struct = {
        "1": "",
        "2": "",
        "3": "",
        "caption":""
    }

    img_header_struct = {
        "pc": simple_str_struct,
        "mob": simple_str_struct
    }

    text_description_struct = {
        "ru": "",
        "en": ""
    }

    pc_mob_str_struct = {
        "pc": "",
        "mob":""
    }
    gallery_struct = {
        "id01":"",
        "id02":"",
        "id03":"",
        "caption": text_description_struct    
    }

    gallery_list_struct = {}
    dict_init(gallery_list_struct, 500, 'g', gallery_struct)

    virtual_tour_preview = {
        "preview": pc_mob_str_struct,
        "start": text_description_struct
    }    
    
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
    dict_init(within_list_struct, 500, 'w', within_struct) 

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
    collect_struct = {
        "path": "",
        "img_mob": "",
        "img_pc": "",
        "circ_img": 0,
        "name": text_description_struct,
        "headimg": text_description_struct,
        "text": text_description_struct,
        "addtext":text_description_struct,
        "textmore":text_description_struct,
        "lbmore":text_description_struct,
        "lbhide":text_description_struct,
        "searcha":text_description_struct,
        "seakeys":text_description_struct,
    }
    
    objects_dict = {}
    collects_dict = {}
    buildings_dict = {}
    events_dict = {}
    objects_dict = dict_init(objects_dict,500, 'o', object_struct)
    dict_init(collects_dict, 500, 'col', collect_struct)
    buildings_dict = dict_init(buildings_dict, 500, 'd', building_struct)
    dict_init(events_dict, 500, 'e', event_struct)
    with open('../JSON/buildings.json', 'r', encoding="utf8") as f:
        buildings_dict = json.load(f) 
    with open('../JSON/events.json', 'r', encoding="utf8") as f:
        events_dict = json.load(f)    
    with open('../JSON/objects.json', 'r', encoding="utf8") as f:
        objects_dict = json.load(f) 
    with open('../JSON/collects.json', 'r', encoding="utf8") as f:
        collects_dict = json.load(f)  
    museum_buildings = Buildings_class(buildings_dict)
    museum_objects = Objects_class(objects_dict)
    museum_collects = Collects_class(collects_dict)
    museum_events = Events_class(events_dict)
    return(museum_buildings, museum_objects, museum_collects, museum_events)