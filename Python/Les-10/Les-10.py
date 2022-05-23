def comparison(var1,var2):
    var1Type = type(var1)
    var2Type = type(var2)
    if var1Type == var2Type:
        if var1 == var2:
            return ('The two variables are identical in type, and identical in value')
        else:
            return ('the two variables are identical in type, but not identical in value')

    else:
        if var1 == var2:
            #This part of the function needs a system to convert both variables to the same type in a way that works on any variable type. Not essential for assignment, so Im leaving that out for now.
            return ('The two variables are not identical in type, but they are in value')
        else:
            return ('the two variables are not identical')




import unittest
class TestCompare(unittest.TestCase):
    '''Tests voor de functie ''comparison''.'''
    def test_function_comparison_with_strings(self):
        '''Werkt de functie met verschillende strings'''
        print("When comparing the two variables, it turns out that",comparison('test','test1'))
        print("When comparing the two variables again, it turns out that",comparison('test','test'))
    def test_function_with_different_types(self):
        '''Werkt de functie als een of meer variabelen leeg zijn?'''
        print("When comparing a string and an integer, the result is:",comparison('1',1))
        print("when comparing an integer and a float, the result is:",comparison(1,1.0))


if __name__ == '__main__':
    unittest.main()