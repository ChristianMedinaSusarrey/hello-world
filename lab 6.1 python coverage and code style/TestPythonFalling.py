# You need to create two functions to substitute str() and int(). 
# A function called int_to_str() that converts integers into strings 
# and a function called str_to_int() that converts strings into integers

#The ord() function returns an integer representing the Unicode character.
import unittest
import PythonFalling

class PythonFailingTest(unittest.TestCase):
     
     def testStringToInt(self):              
        # expectedResult ="<class 'int'>"   
        result = type(PythonFalling.str_to_int("255"))
        self.assertEqual(result, type(5))
     
     def testIntToString(self):              
        # expectedResult ="<class 'String'>"   
        result = type(PythonFalling.int_to_str(123))
        self.assertEqual(result, type("string"))
    
     def testIsNegative(self):                       
        result = PythonFalling.isNegative(5)
        self.assertFalse(result)
     
     def testIsNegative2(self):                       
        result = PythonFalling.isNegative(-5)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()





