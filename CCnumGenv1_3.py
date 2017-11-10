#!usr/bin/env python
# -*- coding: utf-8 -*-
"""

                        *******************************
                        *   Created by 4rch30pt3ryX   *
                        *******************************

Script to generate valid visa 16-digit cc numbers for testing purposes. Utilizes
the Luhn Algorithm to include checksum for the 16th digit.

Notes: Currently the script is set up to generate a set amount(~x) of random,
unique, and valid numbers. I have found an issue where I sometimes do not
receive the exact amount of numbers I requested numbers. Current testing
shows current observed results of less than or equal to x (where x = the
amount inputted form the user).
"""
from random import Random
import copy
import os
from colorama import init, Fore, Back, Style
from termcolor import colored

init()
validcclist = []

def creator():
    rows, columns = os.popen('stty size', 'r').read().split()

    intcol = int(columns)
    print('\n\n')
    print(colored('*    CCnumGen_v1.3    *', 'magenta').center(intcol))
    sign = colored('*    [---    Created By 4rch30pt3ryX    ---]    *', 'magenta')
    signs = sign.center(intcol) 
    longaster = colored('*************************************************', 'magenta').center(intcol)
    signage = longaster + '\n' + signs+ '\n' + longaster
    print('\n' + signage + '\n')
    
creator()

def checksum_cc(case):
    oddlist = list(case[::2]) #all odd ints in case
    evenlist = list(case[1::2]) #all even ints in case
    """ remember 1st spot = 0 """

    intevenlist = [int(i) for i in evenlist] #iterate over evenlist to convert to int
    intoddlist = [int(i) for i in oddlist] #iterate over oddlist to convert to int
    
    sum_of_evens = sum(intevenlist) # sum of all even ints in the list
    
    intlist = []

    for i in intoddlist: #iterates through caseevens and doubles each integer in the list
        doubleodds = i * 2
        strdbl = str(doubleodds) #convert doubleevens to a str to iterate on it in the next for loop
        #print(strdbl) #debugging      
       
        intdbl = [int(i) for i in strdbl] #list comprehension nest for loop to convert each character to int
        intdblr = sum(intdbl) #adds each set of iterated integers together
   
        intlist.append(intdblr) #append to new list intlist  

    intlistsum = sum(intlist) #add each int in the list together
    
    combined = (intlistsum + sum_of_evens) #sum of even ints and doubled odd ints
    
    checksum = combined % 10 #returns mod 10 of combined
    
    checksumdigit = 10 - checksum #implented to get the checksum digit
    
    full16 = (case + str(checksumdigit)) #add checksum to string to create 16 characters
    
    validcclist.append(full16)

visaPrefixList = [
        ['4', '5', '3', '9'],['4', '5', '5', '6'],
        ['4', '9', '1', '6'],['4', '5', '3', '2'],
        ['4', '9', '2', '9'],['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],['4', '7', '1', '6'],['4']
        ]

while True:
    try:
        usrrequest = (raw_input(colored("How many cards would you like to create?:  ",
                                   "blue"))) 
        # the amount, as an integer, of valid credit cards to be generated        
        if int(usrrequest) <= 0:
            print(colored("\nYou must provide a positive integer\n", 'red'))
            continue
        elif usrrequest == 'quit':
            print(colored("\nExiting...\n...\n", "red"))
            exit()
    except:
        print(colored("\nYou must provide a positive number", 'red'))
        continue
    else:
        break
        
amount = int(usrrequest)

def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, this can be any
    number of digits.
    'length' is the length of the CC number to generate. Typically 16,
    Gift Cards can be greater, for instance.
    """

    ccnumber = prefix
    # generate digits
    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum
    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:
        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):
            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit
    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))
    return ''.join(ccnumber)

def credit_card_number(rnd, prefixList, length, howMany):
    result = []    
            
    while len(result) < howMany:
        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))
            
    return result

def output(title, numbers):
    result = []
    result.append(title)
    result.append('-' * len(title))
    result.append('\n'.join(numbers))
    result.append('')

    return '\n'.join(result)

# ----------Main------------

generator = Random()
generator.seed()
# Seed from current time

def main():
    visa16 = credit_card_number(generator, visaPrefixList, 16, amount) 
    #assigns method credit_card_number and it's arguments
    visa15 = []
    for i in visa16:
        #shaves off '0.0' from completed_number in preparation to add the checksum digit
        strvisa15 = (str(i[0:15]))
        visa15.append(strvisa15)    

    for i in visa15: #loop iterates each i through method: checksum_cc
        ccchecksum = (checksum_cc(i)) 

    print("\n")  
    validvisa16list = []

    for item in validcclist: #this loop ensures no integers > or < 16 in length slip through
        if len(item) != 16:
            continue
    
        print(item)
        validvisa16list.append(item)
        
        #below is to write to a text file
        """path = 'C:/Users/<username>/test_CCs.txt'
    
        with open(path, 'a') as out:
            out.write('\n' + item)"""
main()
