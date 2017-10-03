#!/usr/bin/python3
# Exercise for Dev Ops

import sys
import functions

# Default function
def main():
    args = sys.argv[1:]
    
    # Checking if user specified function to use
    if not args:
        print('Invalid Entry.\n'
              'Usage Guide:\n'
              'TYPE: "python3 file.py --arg"\n\n'
              'OPTIONS:\n'
              'miles_to_feet:\t\t--tofeet\n'
              'to_seconds:\t\t--tosec\n'
              'rectangle_area:\t\t--recarea\n'
              'name_and_age:\t\t--nameage')
    else:
        # calls a certain function depending on user's specification
        if args[0] == '--tofeet':
            functions.miles_to_feet(13)
        
        if args[0] == '--tosec':
            functions.total_seconds(7, 21, 37)

        if args[0] == '--recarea':
            functions.rectangle_area(4, 7)

        if args[0] == '--nameage':
            functions.name_and_age('Joe Blogs', '35')


if __name__ == "__main__":
    main()