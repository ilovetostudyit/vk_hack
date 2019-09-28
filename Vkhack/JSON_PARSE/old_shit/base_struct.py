import json 

def dict_init(the_dict, n, str, fill_struct):
    i = 1
    while (i < n):
        the_dict[str + '%s' %(i)] = fill_struct
        i = i + 1

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

