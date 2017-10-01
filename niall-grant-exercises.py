#!/usr/bin/python3

import sys

def input_int(prompt, high):
    int_input = 0
    while True:
        int_input = input(prompt)
        if not int_input.isdigit():
            print('Invalid input: ' + str(int_input))
            continue
            
        int_input = int(int_input)
        
        if int_input >= high or int_input < 0:
            print('Invalid Value: ' + str(int_input))
            continue
        else:
            return int_input
        

def miles_to_feet():
    print('MILES TO FEET:\n')
    miles = input('No. of Miles:')
    feet = 5280
    if not miles:
        print('No valid input detected. Miles value defaults to 13')
        miles = 13
        
    total = feet * int(miles)
    return str(miles) + ' miles = ' + str(total) + ' feet'

def to_seconds():
    print('CONVERT TO SECONDS:')
    hour = input_int('Hour: ', 24)
    mins = input_int('Minutes: ', 60)
    sec = input_int('Seconds: ', 60)
    
    hour_sec = hour * 3600
    min_sec = mins * 60
    
    total_sec = hour_sec + min_sec + sec
    
    return 'Total seconds: ' + str(total_sec)

def main():
    args = sys.argv[1:]
    if not args:
        print('Invalid Entry.\n'
              'Usage Guide:\n'
              'Type: "python3 file.py [--arg]"\n\n'
              '[--arg value] options:\n'
              'miles_to_feet:\t\t--tofeet\n'
              'to_seconds:\t\t--tosec\n')
        
    if args[0] == '--tofeet':
        print(miles_to_feet())
    
    if args[0] == '--tosec':
        print(to_seconds())
    
if __name__ == "__main__":
    main()