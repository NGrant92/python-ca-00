#!/usr/bin/python3
# Exercise for Dev Ops

import sys

# converts user input miles to feet
def miles_to_feet():
    print('MILES TO FEET:')
    miles = 13
    feet = 5280
    
    total = feet * int(miles)
    print(str(miles) + ' Miles = ' + str(total) + ' Feet')


# Converts hours and mins to seconds and
# gets the sum of the converted hours, minutes and inputted seconds
def total_seconds():
    print('CONVERT TO SECONDS:')
    hour = 7
    mins = 21
    sec = 37
    
    hour_sec = hour * 3600
    min_sec = mins * 60
    
    total_sec = hour_sec + min_sec + sec
    
    print('Total seconds: ' + str(total_sec))
    
def rectangle_area():
    w = 7
    h = 4
    print('Area of Rectangle: ' + str(w * h) + ' inches sq')
    
def name_and_age():
    name = 'Joe Blogs'
    age = '35'
    
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
            miles_to_feet()
        
        if args[0] == '--tosec':
            total_seconds()

        if args[0] == '--recarea':
            rectangle_area()

        if args[0] == '--nameage':
            name_and_age()


if __name__ == "__main__":
    main()