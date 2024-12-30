"""
Author: Akhil Malik
Date Created: 19 June 2024
"""

import random
import sys

def exitAsk():
    
    exitInput = input("\n\t// Do you want to create another password?? (y/n): ")
    
    if exitInput. lower() == "n":
    
        print("\n\t// Thank you for using the Password Generator! See you next time!!")
        print("\t// Exiting program ... \n")

        sys. exit(0)

    elif exitInput.lower() == "y":
    
        print("\n\t\t// Let's have a go at it again!")
        createPassword()

    else:

        print("\n\n\t\t!! (y/n)")
        print("\n\t\t!! For Yes - lower case \"y\"")
        print("\n\t\t!! For No - lower case \"n\"")

        exitAsk()



def upperSwitch(char_list):
    return [char.upper() for char in char_list]


def createPassword():

    user_input = input("\n\t\t// Enter the length of your new password (eg. 10, 23, 798): ")
    
    lowercase_Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase_Alphabets = upperSwitch(lowercase_Alphabets)
    numerals = ['1','2','3','4','5','6','7','8','9','0']
    special_Char = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','|','.','/','<','>','?']

    main_list = lowercase_Alphabets + uppercase_Alphabets + numerals + special_Char
    random.shuffle(main_list)

    if user_input.isdigit():
    
        length = int(user_input)

        if length > 0:
            x = 1
            y = []

            while x <= length:
                a = random.choice(main_list)
                b = y.append(a)
                x += 1
            
            z = ''.join(map(str,y))
            print("\n", z, "\n")
            exitAsk()

        elif length == 0:
            print("\n\t\t// Error: The length cannot be zero.")
            exitAsk()
        
    else:
        print("\n\t\t// Error: Please enter an POSITIVE INTEGER (1, 2, 3, 4...).")
        exitAsk()

print("\n\tHey there! This program generates passwords of your given length of randomized alphanumeric and speacial characters.")
createPassword()
