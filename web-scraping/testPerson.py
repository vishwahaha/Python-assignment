import Person
import unittest
import io
import sys

class TestPersonClass(unittest.TestCase):
    def test_newUsername(self):  
        def testFunc():
            Person.scrap("vishwa.prakash.771")                  
        self.assertRaises(AssertionError, testFunc)

    def test_existingUsername(self):
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        Person.scrap("anshul.d.sharma.7")                                     
        sys.stdout = sys.__stdout__                     
        self.assertEqual(capturedOutput.getvalue(), "My name is Anshul Dutt Sharma and my current city is Roorkee\n")

if __name__ == '__main__':
    unittest.main()