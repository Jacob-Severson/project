import pytest
from main import *
class test:
    def testnameAndAge(self):
        self.assertnameAndAge('James', 10) == 'Hello James! You are 20 years old.'
        self.assertnameAndAge('james', 10) == 'Hello James! You are 20 years old.'

        with self.assertRaises(TypeError):
            nameAndAge(10, 10)
            nameAndAge('James', '10')