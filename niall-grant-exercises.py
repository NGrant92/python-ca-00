#!/usr/bin/python3

import sys

def miles_to_feet(miles):
    feet = 5280
    if not miles:
        miles = 13
        
    total = feet * int(miles)
    return str(miles) + ' miles = ' + str(total) + ' feet'

def calc_seconds():
    hour = 7
    min = 21
    sec = 37
    return

def switch(key, param):
    switch_dict = {
        'miles_to_feet': miles_to_feet(param)
    }
    
    print(switch_dict.get(key, 'Invalid Input: ' + key))

def main():
    args = sys.argv[1:]
    
    if not args:
        miles_to_feet('')
    else:
        switch(args[0], args[1])
        

if __name__ == "__main__":
    main()