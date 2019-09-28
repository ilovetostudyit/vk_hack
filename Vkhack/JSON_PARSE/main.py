import sys
from base_parse import *

def main(argv=None):
    museum = base_navigation()
    museum.buildings.get_list_objects()
    museum.events.get_list_objects()
    return 0

if __name__ == "__main__":
    main()