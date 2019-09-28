import json 
from base_struct import *

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
 
collects_dict = {}
dict_init(collects_dict, 500, 'col', collect_struct)        


with open('../JSON/collects.json', 'r', encoding="utf8") as f:
    collects_dict = json.load(f)
try:
    for collect in (collects_dict):
        print(collects_dict[collect]["name"]["ru"])
except Exception as E:
    print(E)