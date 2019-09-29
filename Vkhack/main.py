import sys
from json_parse.utils import *
from json_parse.base_parse import *
from django.urls import path
#from . import views

def main(argv=None):
    museum = base_navigation()
    print(museum.buildings.get_museum_status("ГАЛЕРЕЯ", "Понедельник"))
    print(museum.buildings.get_museum_status("ГитЛЕР", "Вторник"))
    print(museum.buildings.get_museum_status("рихтера", "Среда"))
    print(museum.buildings.get_museum_status("депазитарий", "Среда"))
    
    print(museum.buildings.building_navigation("галерея","расписание"))
    print(museum.buildings.building_navigation("галерея","контакты"))
    print(museum.buildings.building_navigation("галерея","яндекс.карты"))

    return 0

if __name__ == "__main__":
    main()