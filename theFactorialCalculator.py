"""
Author: Akhil Malik
Date created: 16 June 2024
"""
import sys

def exitAsk() :
    
    exitInput = input("\n\t// Do you want to continue finding out more factorials?? (y/n): ")
    
    if exitInput. lower() == "n":
    
        print("\n\t// Thank you for using the Factorial Calculator! See you next time!!")
        print("\t// Exiting program ... \n")

        sys. exit(0)

    elif exitInput.lower() == "y":
    
        print("\n\t\t// Let's have a go at it again!")
        factorial_calculator()

    else:

        print("\n\n\t\t!! (y/n)")
        print("\n\t\t!! For Yes - lower case \"y\"")
        print("\n\t\t!! For No - lower case \"n\"")

        exitAsk()

print("\n\tHi there! This is a program to calculate the factorial of a number (non-negative integer).")
print("\n\tFactorial of a number in mathematics is the product of all the positive numbers less than or equal to a number.")
print("\n\t\tn! = (n)x(n-1)x(n-2)x(n-3)x...x(4)x(3)x(2)x(1)")

def factorial_calculator ():
    
    userInput = input( "\n\t// Enter a number: ")
    
    if userInput.isdigit():

        number = int(userInput)
        x = f"{number}!"
        factorial = 1
        i = number
    
        while i >= 1:
    
            factorial = factorial * i
            i -= 1

        print("\n\t", x , "is", factorial) 
   
        print("\n\tNow here's the explaination :-")
        
        a = number
        b = f"{a}x"
        c = [b]
        d = 1
        
        while a >= 1:
    
            d = d * a
            a -= 1

            if a > 1:
    
                b = f"{a}x"
                c.append(b)

            elif a == 1:
    
                b = f"{a}"
                c.append(b)
                e = ''.join(map(str,c))
    
                print("\n\t\t\tThus," , x , " = " , e , " = ", d , "\n")

            elif number == 1:

                print("\n\t\tBut there are no positive values less than one so the data set cannot be arranged which counts as the possible combination of how data can be arranged (it cannot).")
                print("\n\t\t\tThus, 1! = 1.")

            elif number == 0:

                print("\n\t\tBut there are no positive values less than zero so the data set cannot be arranged which counts as the possible combination of how data can be arranged (it cannot).")
                print("\n\t\t\tThus, 0! = 1.")

        exitAsk()
    
    else:

        print("\n\t// Dear Sir/Ma'am, ")
        print("\n\t\t// It is unfortunate to inform you that our program has rejected your request.")
        print("\t\t// This could have occured due to an error in the input provided.")
        print("\n\n\t\t## Factorials of only NON-NEGATIVE INTEGERS are possible. ##")
        print("\n\t\t\t// ie. >=0")
        print("\n\t\t\t// eg. 25476, 7353, 404.")

        exitAsk()
    
factorial_calculator()
