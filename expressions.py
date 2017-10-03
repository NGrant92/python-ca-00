#!/usr/bin/python3
# Exercise for Dev Ops

import sys
import functions

# Default function
def main():
    args = sys.argv[1:]
    
    # Checking if user specified function to use
    if not args:
        menu = open('menu.txt', 'rU')
        print(menu.read())
        
    else:
        # calls a certain function depending on user's specification
        if args[0] == '--tofeet':
            functions.miles_to_feet(13)
        
        elif args[0] == '--tosec':
            functions.total_seconds(7, 21, 37)

        elif args[0] == '--recarea':
            functions.rectangle_area(4, 7)

        elif args[0] == '--nameage':
            functions.name_and_age('Joe Blogs', '35')
        else:
            menu = open('menu.txt', 'rU')
            print('INVALID INPUT: ' + args[0] + menu.read())
            


if __name__ == "__main__":
    main()