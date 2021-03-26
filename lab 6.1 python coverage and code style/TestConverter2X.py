import unittest
import converter2X


class ConverterTest(unittest.TestCase):
    def testBinaryRep(self):              
        expectedResult = "111"
        result = converter2X.getBinaryRepresentations(7)          
        self.assertEqual(result, expectedResult)

    def testHexRepWithoutLetter(self):              
        expectedResult = "19"
        result = converter2X.getHexRepresentations(25)              
        self.assertEqual(result, expectedResult)

    def testHexRepWithLetter(self):              
        expectedResult = "A"
        result = converter2X.getHexRepresentations(10)              
        self.assertEqual(result, expectedResult)   
     
    def testBinaryRepZero(self):              
        expectedResult = "0"
        result = converter2X.getBinaryRepresentations(0)          
        self.assertEqual(result, expectedResult)

    def testHexRepZero(self):              
        expectedResult = "0"
        result = converter2X.getHexRepresentations(0)              
        self.assertEqual(result, expectedResult)  


if __name__ == "__main__":
    unittest.main()
