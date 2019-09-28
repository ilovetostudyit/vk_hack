import sys
from json_parse.base_parse import *
from django.urls import path
#from . import views

def main(argv=None):
    museum = base_navigation()
    print(museum.buildings.get_list_objects())

    return 0

if __name__ == "__main__":
    main()