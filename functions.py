#!/usr/bin/python3
# Exercise for Dev Ops

import sys
import math

# prompt: Message for user
# high: the max number input can't go over
def input_int(prompt, high):
    while True:
        # asks user for input
        int_input = input(prompt)
        # checks to make sure user input is only a number
        # if not then it restarts loop
        if not int_input.isdigit():
            print('Invalid input: ' + str(int_input) + '\n')
            continue
        
        # converts input from a string to an int
        int_input = int(int_input)
        
        # checks if user input needs to be tested
        if isinstance(high, int):
            # checks to make sure input is within a range
            # repeats loop if it's outside of range
            # if true it'll break loop and return the value
            if high > int_input >= 0:
                return int_input
            else:
                print('Invalid Value: ' + str(int_input))
                continue
        # if param is not an int then it'll simply return the int
        else:
            return int_input


# converts user input miles to feet
def miles_to_feet(miles):
    feet = 5280
    if not miles:
        print('No valid input detected. Miles value defaults to 13')
        miles = 13
    
    total = feet * int(miles)
    print(str(miles) + ' Miles = ' + str(total) + ' Feet')


# Converts hours and mins to seconds and
# gets the sum of the converted hours, minutes and inputted seconds
def total_seconds(hour, mins, sec):
    hour_sec = hour * 3600
    min_sec = mins * 60
    
    total_sec = hour_sec + min_sec + sec
    
    print('Total seconds: ' + str(total_sec))

# To calculate the area of a rectangle
def rectangle_area(w, h):
    print('Area of Rectangle: ' + str(w * h) + ' inches sq')

# To concat a name and age into a sentance
def name_and_age(name, age):
    print(name + ' is ' + age + ' years old')

# Takes parameters x0, y0, x1, y1 and returns the distance between the points (x0,y0) and (x1, y1)
def point_distance(x0, y0, x1, y1):
    
    point_calc = (x1 - x0)**2 + (y1 - y0)**2
    dist = int(math.sqrt(point_calc))
    
    # prints result to screen
    print('Distance Between points (' + str(x0) + ',' + str(y0) + ') and (' + str(x1) + ',' + str(y1) + ')')
    print('Total Dist: ' + str(dist))

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
              'point_distance:\t\t--pntdist\n')
    else:
        # calls a certain function depending on user's specification
        # asks user for input if required by the method
        if args[0] == '--tofeet':
            print('MILES TO FEET:')
            miles = input_int('No. of Miles: ', '')
            miles_to_feet(miles)
        
        if args[0] == '--tosec':
            print('CONVERT TO SECONDS:')
            hour = input_int('Hour: ', 24)
            mins = input_int('Minutes: ', 60)
            sec = input_int('Seconds: ', 60)
            total_seconds(hour, mins, sec)
        
        if args[0] == '--pntdist':
            x0 = input_int('x0: ', '')
            y0 = input_int('y0: ', '')
            x1 = input_int('x1: ', '')
            y1 = input_int('y1: ', '')
            point_distance(x0, y0, x1, y1)

if __name__ == "__main__":
    main()
