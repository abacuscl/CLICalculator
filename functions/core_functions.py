'''
All of the classes have 3 methods to carry out their functions.
These classes have straightforward processes, so no additional comments
were added.

__init__(args):
The basic class constructor. Takes the args provided and saves them as
class variables. These variables are used to perform calculations when the
getSolution() method is called.

getSolution():
Calculates the solution based on the class it is in. It returns the solution as
a String.

getEquation():
Formats the equation with the original values given in the constructor. Returns
the formatted equation as a String.
'''

#Imports
import math

#Class that handles addition
class Addition:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def getSolution(self):
        self.solution = (self.n1 + self.n2)
        return (self.solution)

    def getEquation(self):
        return f"{self.n1} + {self.n2} = {self.solution}\n"

#Class that handles subtraction
class Subtraction:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def getSolution(self):
        self.solution = (self.n1 - self.n2)
        return (self.solution)

    def getEquation(self):
        return f"{self.n1} - {self.n2} = {self.solution}\n"

#Class that handles multiplication
class Multiplication:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def getSolution(self):
        self.solution = (self.n1 * self.n2)
        return (self.solution)

    def getEquation(self):
        return f"{self.n1} * {self.n2} = {self.solution}\n"

#Class that handles division
class Division:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def getSolution(self):
        if self.n2 == 0:
            if self.n1 == 0:
                self.solution = "Indeterminate"
            else:
                self.solution = "Undefined"
        else:
            self.solution = (self.n1 / self.n2)
        return (self.solution)

    def getEquation(self):
        return f"{self.n1} / {self.n2} = {self.solution}\n"

#Class that handles powers (exponents)
class Power:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def getSolution(self):
        self.solution = math.pow(self.n1, self.n2)
        return (self.solution)

    def getEquation(self):
        return f"{self.n1}^{self.n2} = {self.solution}\n"

#Class that handles square roots
class SquareRoot:
    def __init__(self, n1):
        self.n1 = n1

    def getSolution(self):
        self.solution = math.sqrt(self.n1)
        return (self.solution)

    def getEquation(self):
        return f"sqrt({self.n1}) = {self.solution}\n"
