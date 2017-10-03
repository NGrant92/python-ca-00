#!/usr/bin/python3
# Exercise for Dev Ops

import sys
import function_exercises
    
def rectangle_area(w, h):
    print('Area of Rectangle: ' + str(w * h) + ' inches sq')
    
def name_and_age(name, age):
    print(name + ' is ' + age + ' years old')

# Default function
def main():
    args = sys.argv[1:]
    
    # Checking if user specified function to use
    if not args:
        print('Invalid Entry.\n'
              'Usage Guide:\n'
              'Type: "python3 file.py --arg"\n\n'
              'Options:\n'
              'miles_to_feet:\t\t--tofeet\n'
              'to_seconds:\t\t--tosec\n'
              'rectangle_area:\t\t--recarea\n'
              'name_and_age:\t\t--nameage')
    else:
        # calls a certain function depending on user's specification
        if args[0] == '--tofeet':
            function_exercises.miles_to_feet(13)
        
        if args[0] == '--tosec':
            function_exercises.total_seconds(7, 21, 37)

        if args[0] == '--recarea':
            rectangle_area(4, 7)

        if args[0] == '--nameage':
            name_and_age('Joe Blogs', '35')


if __name__ == "__main__":
    main()