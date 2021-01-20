'''
All of the classes have 3 methods to carry out their functions.
No additional comments have been added as the processes carried out are
fairly straightforward.

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

#Class that handles trigonomtry
class Trigonometry:
    def __init__(self, trigType):
        self.trigType = trigType

    def getSolution(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        trigType = self.trigType

        if trigType == "sin":
            self.solution = math.sin(math.radians(n1))
        elif trigType == "cos":
            self.solution = math.cos(math.radians(n1))
        elif trigType == "tan":
            self.solution = math.tan(math.radians(n1))
        elif trigType == "invsin":
            self.solution = math.degrees(math.asin(n1 / n2))
        elif trigType == "invcos":
            self.solution = math.degrees(math.acos(n1 / n2))
        elif trigType == "invtan":
            self.solution = math.degrees(math.atan(n1 / n2))
        elif trigType == "sideasin":
            n1 = math.radians(n1)
            self.solution = n2 * math.sin(n1)
        elif trigType == "sideatan":
            n1 = math.radians(n1)
            self.solution = n2 * math.tan(n1)
        elif trigType == "sideapyth":
            n1 = math.pow(n1, 2)
            n2 = math.pow(n2, 2)
            self.solution = math.sqrt(n1 - n2)
        elif trigType == "sidebcos":
            n1 = math.radians(n1)
            self.solution = n2 * math.cos(n1)
        elif trigType == "sidebtan":
            n1 = math.radians(n1)
            self.solution = n2 / math.tan(n1)
        elif trigType == "sidebpyth":
            n1 = math.pow(n1, 2)
            n2 = math.pow(n2, 2)
            self.solution = math.sqrt(n1 - n2)
        elif trigType == "sidecsin":
            n1 = math.radians(n1)
            self.solution = n2 / n1
        elif trigType == "sideccos":
            n1 = math.radians(n1)
            self.solution = n2 / n1
        elif trigType == "sidecpyth":
            n1 = math.pow(n1, 2)
            n2 = math.pow(n2, 2)
            self.solution = n1 + n2
        
        if self.solution == "�":
            return "Math Error."
        else:
            return self.solution
        
    def getEquation(self):
        trigType = self.trigType

        if trigType == "sin":
            return f"sin({self.n1}) = {self.solution}"
        elif trigType == "cos":
            return f"cos({self.n1}) = {self.solution}"
        elif trigType == "tan":
            return f"tan({self.n1}) = {self.solution}"
        elif trigType == "invsin":
            return f"Inverse sin({self.n1} / {self.n2}) = {self.solution}"
        elif trigType == "invcos":
            return f"Inverse cos({self.n1} / {self.n2}) = {self.solution}"
        elif trigType == "invtan":
            return f"Inverse tan({self.n1} / {self.n2}) = {self.solution}"
        elif trigType == "sideasin":
            return f"Side a: {self.n2}sin({self.n1}) = {self.solution}"
        elif trigType == "sideatan":
            return f"Side a: {self.n2}tan({self.n1}) = {self.solution}"
        elif trigType == "sideapyth":
            return f"Side a: a^2 + {self.n2}^2 = {self.n1}^2"
        elif trigType == "sidebcos":
            return f"Side b: {self.n2}cos({self.n1}) = {self.solution}"
        elif trigType == "sidebtan":
            return f"Side b: {self.n2}tan({self.n1}) = {self.solution}"
        elif trigType == "sidebpyth":
            return f"Side b: {self.n2}^2 + b^2 = {self.n1}^2"
        elif trigType == "sidecsin":
            return f"Side c: {self.n2}sin({self.n1}) = {self.solution}"
        elif trigType == "sideccos":
            return f"Side c: {self.n2}cos({self.n1}) = {self.solution}"
        elif trigType == "sidecpyth":
            return f"Side c: {self.n1}^2 + {self.n2}^2 = c^2"
            
