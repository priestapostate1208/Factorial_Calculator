import math


def factorialCalculator(inputted_number):
    '''This returns the factorial of a given number'''
    fac_num=1
    for x in range(1,inputted_number+1): #don't forget the index counting
        fac_num = x * fac_num
    print(fac_num)
    return fac_num



inputted_number = int(input("What is the number you wish to work with?  "))
factorialCalculator(inputted_number)


