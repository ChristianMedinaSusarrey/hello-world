import unittest
import findWords


class ConverterTest(unittest.TestCase):
    def testFindOneWord(self):              
        expectedResult = " Word For exists: 1 times"
        # wordsToFind = "equivocarme,Fuerza,Chris,Test,Tarea,sentí"
        wordsToFind = "For"
        wordsToFind = wordsToFind.split(',')
        with open('Lullaby - The cure.txt', 'r') as file:
            data = file.read().replace('\n', ' ')
        wordsInText = data.split(' ')
        result = findWords.findWords(wordsToFind, wordsInText)          
        self.assertEqual(result.replace('\n', ''), expectedResult)
     
    def testFindTwoWords(self):              
        expectedResult =" Word For exists: 1 times Word for exists: 3 times"        
        wordsToFind = "For,for"
        wordsToFind = wordsToFind.split(',')
        with open('Lullaby - The cure.txt', 'r') as file:
            data = file.read().replace('\n', ' ')
        wordsInText = data.split(' ')
        result = findWords.findWords(wordsToFind, wordsInText)          
        self.assertEqual(result.replace('\n', ''), expectedResult)

    def testFindOneWordSpanish(self):              
        expectedResult =" Word equivocarme exists: 1 times"       
        wordsToFind = "equivocarme"
        wordsToFind = wordsToFind.split(',')
        with open('Fuerza Natural - Cerati.txt', 'r') as file:
          data = file.read().replace('\n', ' ')
        wordsInText = data.split(' ')
        result = findWords.findWords(wordsToFind, wordsInText)          
        self.assertEqual(result.replace('\n', ''), expectedResult)
     
    def testFindTwoWordsSpanish(self):              
        expectedResult =" Word equivocarme exists: 1 times Word natural exists: 2 times"        
        wordsToFind = "equivocarme,natural"
        wordsToFind = wordsToFind.split(',')
        with open('Fuerza Natural - Cerati.txt', 'r') as file:
            data = file.read().replace('\n', ' ')
        wordsInText = data.split(' ')
        result = findWords.findWords(wordsToFind, wordsInText)          
        self.assertEqual(result.replace('\n', ''), expectedResult)


if __name__ == "__main__":
    unittest.main()

    