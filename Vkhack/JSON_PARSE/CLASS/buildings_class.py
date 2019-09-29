import json
import pandas as pd
from json_parse.utils import *
class Buildings_class(object):
    def __init__(self, collects_dict):
        self.dict = collects_dict
    def get_building_name(self, object):
        return(self.dict[object]["name"]["ru"])
    def get_building_adress(self, object):
        return(self.dict[object]["adress"]["ru"])
    def get_building_brief(self, object):
        return(self.dict[object]["brief"]["ru"])
    def get_list_objects(self):
        test_str = ""
        for object in self.dict:
            test_str = test_str + '-' + self.get_building_name(object) + ' (' + self.get_building_adress(object) + ') \n'
        json_answer = {}
        json_answer["text"] = test_str
        return(json.dumps(json_answer, ensure_ascii=False,))
        
    def get_museum_shedule(self, object, date):
        json_answer = {}
        json_answer["text"] = self.get_building_name(object) + ' '
        date_base = {
            "понедельник": "mon",
            "вторник": "tue",
            "среда": "wed",
            "четверг": "thu",
            "пятница": "fri",
            "суббота": "sat",
            "воскресенье": "sun"
        }
        max = 0
        tanim_object = 0
        for each in date_base:
            tanim_coof = tanimoto(each.lower(), date.lower())
            if (tanim_coof >= max):
                max = tanim_coof
                tanim_object = each
        if (tanim_coof > 0.45):
            day_id = date_base[tanim_object]
            if self.dict[object]["schedule"] and self.dict[object]["schedule"]["regulars"]:
                if self.dict[object]["schedule"]["regulars"][day_id]["timebegin"] and self.dict[object]["schedule"]["regulars"][day_id]["timeend"]:
                    json_answer["text"] = json_answer["text"] + 'Время работы: с ' + self.dict[object]["schedule"]["regulars"][day_id]["timebegin"]
                    json_answer["text"] = json_answer["text"] + ' до ' + self.dict[object]["schedule"]["regulars"][day_id]["timeend"]
                else:
                    json_answer["text"] = json_answer["text"] + "не работает в этот день"
            else:
                json_answer["text"] =  json_answer["text"] + "еще не имеет расписания"
        else:
            return(wrong_question())
        return(json_answer["text"])
    
    def building_recognition(self, building_name, date):
        max = 0
        tanim_object = 0
        for object in self.dict:
            tanim_coof = tanimoto(self.get_building_name(object).lower(), building_name.lower())
            if (tanim_coof >= max):
                max = tanim_coof
                tanim_object = object
        if (tanim_coof > 0.50):
            return(self.get_museum_shedule(tanim_object, date))
        else:
            return(wrong_question())
            
    def get_museum_status(self, building_name, date):
        json_answer = {}
        json_answer["text"] = self.building_recognition(building_name, date)
        return(json.dumps(json_answer, ensure_ascii=False,))
    def get_building_contacts(self, object):
        text = ""
        if self.dict[object]["tel"]["ru"]:
            text = text + self.dict[object]["tel"]["ru"]
        else:
            text = text + "К сожалению, нет номера телефона." + '\n'
        if self.dict[object]["invalid"]["ru"]:
            text = text + "Поддержка людей с ограниченными возможностями: " + self.dict[object]["invalid"]["ru"] + '\n'
        else:
            text = text + "К сожалению, нет информации, оборудовано ли здание для инвалидов." + '\n'
        if self.dict[object]["rate"]["ru"]:
            text = text + "Билеты: " + self.dict[object]["rate"]["ru"] + '\n'
        else:
            text = text + "К сожалению, нет информации о билетах." + '\n'
        return(text)
    
    def get_yandex_link(self, object):
        text = "https://yandex.com/maps/?ll="
        list_basic = self.dict[object]["yamapcoords"].split(',')
        text = text + list_basic[2] + '%2C' + list_basic[1]+ '&z='+list_basic[0]
        return(text)
    
    def building_navigation(self, building_name, button_pressed):
        json_answer = {}
        max = 0
        tanim_object = 0
        for object in self.dict:
            tanim_coof = tanimoto(self.get_building_name(object).lower(), building_name.lower())
            if (tanim_coof >= max):
                max = tanim_coof
                tanim_object = object
        if (tanim_coof > 0.50):
            json_answer["text"] = self.get_building_name(tanim_object) + '. ' + self.get_building_brief(tanim_object) + '\n'
            if button_pressed == "расписание":
                json_answer["text"] = json_answer["text"] + " Какой день недели вас интересует?"
                return(json.dumps(json_answer, ensure_ascii=False,))
            elif button_pressed == "контакты":
                json_answer["text"] = json_answer["text"] + self.get_building_contacts(tanim_object)
                return(json.dumps(json_answer, ensure_ascii=False,))
            elif button_pressed == "яндекс.карты":
                json_answer["text"] = json_answer["text"] + "ссылка на Яндекс.Карты:"+ self.get_yandex_link(object)
                return(json.dumps(json_answer, ensure_ascii=False,))
        else:
            json_answer["text"] = wrong_question()
        return(json.dumps(json_answer, ensure_ascii=False,))
    