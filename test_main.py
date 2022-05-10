import pytest
from main import *
class test:
    def testtoWrite(self):
        self.asserttoWrite('James', 10, "jseverson@unomaha.edu", 123567890, "Male") == "Name: James, Age: 10, Email: jseverson@unomaha.edu, phone #: 1234567890, gender: Male"
        self.asserttoWrite('James', 20, "jseverson2@unomaha.edu", 123567999, "Other") == "Name: James, Age: 20, Email: jseverson2@unomaha.edu, phone #: 1234567999, gender: Other"
    def testcheckemail(self):
        self.assertcheckemail("jseverson@unomaha.edu") == True
        self.assertcheckemail("something") == False
        self.assertcheckemail("jseverson.unomaha.edu") == False
    def testcheckphone(self):
        self.assertcheckphone("1234567890") == True
        self.assertcheckphone("(123)4567890") == True
        self.assertcheckphone("123-456-7890") == True
        self.assertcheckphone("22") == False