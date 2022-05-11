import unittest

import main
from main import *
class Testmain(unittest.TestCase):
    def testtoWrite(self):
        self.assertEqual(toWrite("james",10,"jseverson@unomaha.edu",1234567890,"male"), "Name: james, Age: 10, Email: jseverson@unomaha.edu, Phone #: 1234567890, Gender: male")
        self.assertEqual(toWrite("James",20,"jseverson2@unomaha.edu",1111111111,"other"), "Name: James, Age: 20, Email: jseverson2@unomaha.edu, Phone #: 1111111111, Gender: other")

    def testcheckemail(self):
        self.assertEqual(checkemail("jseverson@unomaha.edu"), True)
        self.assertEqual(checkemail("something"), False)
        self.assertEqual(checkemail("aowora@unomaha.edu"), True)
    def testcheckphone(self):
        self.assertEqual(checkphone("1234567890"),True)
        self.assertEqual(checkphone("(123)4567890"),True)
        self.assertEqual(checkphone("123-456-7890"),True)
        self.assertEqual(checkphone("22"),False)
