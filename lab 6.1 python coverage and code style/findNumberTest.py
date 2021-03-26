import unittest
import findWords


class ConverterTest(unittest.TestCase):    
    def testBinaryRep(self):              
        expectedResult = "111"
        result = findWords.getBinaryRepresentations(7)          
        self.assertEqual(result, expectedResult)

    def testHexRep(self):              
        expectedResult = "19"
        result = findWords.getHexRepresentations(25)              
        self.assertEqual(result, expectedResult)  
            
    def testBinaryRepZero(self):
        expectedResult = "0"
        result = findWords.getBinaryRepresentations(0)          
        self.assertEqual(result, expectedResult)

    def testHexRepZero(self):
        expectedResult = "0"
        result = findWords.getHexRepresentations(0)              
        self.assertEqual(result, expectedResult)  


if __name__ == "__main__":
    unittest.main()