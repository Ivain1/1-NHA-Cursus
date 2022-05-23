#!/usr/bin/env python3
from random import randint #importing a random number generator in order to have varying input every time the program is run.

number = int(randint(0,100))
text = str('A piece of placeholder text')
#theList.append(randint(5,10))
#additions = range(randint(0,15))
randomList = []


def measure(num1,string1,list1):

    '''Measure(<int>,<string>,<list>)
    A function that measures the length of an integer and a string, and appends the list
    The list is appended by C entries of D, where C is a random number between 0 and B, and d is a random number between 0 and A.
    A is the value of the number input, while B is the length of the string.
    '''

    for i in range(0,randint(1,len(string1))):
        randomList.append(randint(0,number))
    print(id(num1))
    print('the number is',num1)
    print('the length of the number is',len(str(num1)))
    print(id(string1))
    print('the string is',string1)
    print('The length of the string is',len(string1))
    print(id(list1))
    print('the list is',list1)
    print('The length of the randomized list is:', len(list1))
    return(list1)


print(measure(number,text,randomList))












