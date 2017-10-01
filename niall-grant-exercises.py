#!/usr/bin/python3
# Exercise for Dev Ops

import sys


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
def miles_to_feet():
    print('MILES TO FEET:')
    miles = input_int('No. of Miles: ', '')
    feet = 5280
    if not miles:
        print('No valid input detected. Miles value defaults to 13')
        miles = 13
    
    total = feet * int(miles)
    return str(miles) + ' Miles = ' + str(total) + ' Feet'


# Converts hours and mins to seconds and
# gets the sum of the converted hours, minutes and inputted seconds
def to_seconds():
    print('CONVERT TO SECONDS:')
    hour = input_int('Hour: ', 24)
    mins = input_int('Minutes: ', 60)
    sec = input_int('Seconds: ', 60)
    
    hour_sec = hour * 3600
    min_sec = mins * 60
    
    total_sec = hour_sec + min_sec + sec
    
    return 'Total seconds: ' + str(total_sec)


# Default function
def main():
    args = sys.argv[1:]
    
    # Checking if user specified function to use
    if not args:
        print('Invalid Entry.\n'
              'Usage Guide:\n'
              'Type: "python3 file.py [--arg]"\n\n'
              '[--arg value] options:\n'
              'miles_to_feet:\t\t--tofeet\n'
              'to_seconds:\t\t--tosec\n')
    
    # calls a certain function depending on user's specification
    if args[0] == '--tofeet':
        print(miles_to_feet())
    
    if args[0] == '--tosec':
        print(to_seconds())


if __name__ == "__main__":
    main()
