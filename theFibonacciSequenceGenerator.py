
"""
Author: Akhil Malik
Date created: 16 June 2024
"""

import sys

def exitAsk():
    
    exitInput = input("\n\t// Do you want to continue finding out more fibonacci numbers?? (y/n): ")
    
    if exitInput. lower() == "n":
    
        print("\n\t// Thank you for using the Fibonacci Sequence Generator! See you next time!!")
        print("\t// Exiting program ... \n")

        sys. exit(0)

    elif exitInput.lower() == "y":
    
        print("\n\t\t// Let's have a go at it again!")
        fibonacci_sequence_generator()

    else:

        print("\n\n\t\t!! (y/n)")
        print("\n\t\t!! For Yes - lower case \"y\"")
        print("\n\t\t!! For No - lower case \"n\"")

        exitAsk()

print("\n\tHi there! This is the Fibonacci Sequence Generator.")
print("\n\n\tFibonacci numbers each number is the sum of the two preceding ones, starting from 0 and 1.")
print("\n\tThey are seen in nature, such as in the arrangement of leaves on a stem, the branching of trees, and the pattern of sunflower seeds.")
print("\n\n\tTo generate such numbers, ")

def fibonacci_sequence_generator():

    userInput = input("\n\t// Enter how many Fibonnaci numbers do you wish to find out?: ")

    if userInput.isdigit():

        number = int(userInput)
    
        a = 0
        b = 1

        fibonacciList = [a , b]


        if number > 2:

            for x in range(number):
                
                c = fibonacciList[-1] + fibonacciList[-2]        
                
                fibonacciList.append(c)
                
            else:
            
                print("\n\t", fibonacciList[:-2])

        elif number == 1:

            print("\n\t", fibonacciList[0])

        elif number == 2:

            print("\n\t", fibonacciList[1])

        

        exitAsk()

    else:

        print("\n\t// Dear Sir/Ma'am, ")
        print("\n\t\t// It is unfortunate to inform you that our program has rejected your request.")
        print("\t\t// This could have occured due to an error in the type of input provided.")
        print("\n\n\t\t## Please type a POSITIVE NATURAL NUMBER. ##")

        exitAsk()


fibonacci_sequence_generator()
