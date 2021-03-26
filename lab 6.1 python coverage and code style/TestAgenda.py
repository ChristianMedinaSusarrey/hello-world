import unittest
import Agenda


class ConverterTest(unittest.TestCase):
    
    
    
    def testAddPerson(self):
        open('D:\\myAgenda.txt', 'w').close()
        p1 = Agenda.Person("Jorge","jorge@email.test","32", "Jamaica")              
        p1.addPerson()
        expectedResult = "Jorge,jorge@email.test,32,Jamaica"       
        with open('D:\\myAgenda.txt', 'r') as file:
            data = file.read().replace('\n', '')
        self.assertEqual(data, expectedResult)
    
    def testGetAllRecords(self):
        open('D:\\myAgenda.txt', 'w').close()
        p1 = Agenda.Person("Jorge","jorge@email.test","32", "Jamaica")              
        p1.addPerson()
        p1 = Agenda.Person("Miguel","miguel@email.test","17", "Honduras")              
        p1.addPerson()                              
        data = p1.getAllRecords()
        expectedResult = "Jorge,jorge@email.test,32,JamaicaMiguel,miguel@email.test,17,Honduras"               
        self.assertEqual(data.replace('\n', ''), expectedResult)

    def testSearchRecords(self):        
        p1 = Agenda.Person("Jorge","jorge@email.test","32", "Jamaica")                      
        expectedResult = "Jorge,jorge@email.test,32,Jamaica"
        line = p1.searchRecord("Jorge")               
        self.assertEqual(line.replace('\n', ''), expectedResult)
        
    def testDeleteRecord(self): 
        open('D:\\myAgenda.txt', 'w').close()
        p1 = Agenda.Person("Jorge","jorge@email.test","32", "Jamaica")              
        p1.addPerson()       
        p1 = Agenda.Person("Jorge","jorge@email.test","32", "Jamaica")                      
        expectedResult = "Jorge,jorge@email.test,32,Jamaica"
        deleted = p1.toDelete("Jorge") 
        line = p1.searchRecord("Jorge")               
        self.assertIsNone(line)
   

if __name__ == "__main__":
    unittest.main()
