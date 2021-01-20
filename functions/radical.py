'''
All of the classes have 3 methods to carry out their functions.
Additional comments have been added to explain complex processes.

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

#Class that handles single radicals with a single number as equals
class SingleRadical:
    def __init__(self, lc, n, eq):
        self.lc = lc
        self.n = n
        self.eq = eq

    def getSolution(self):
        lc = self.lc
        n = self.n
        eq = self.eq

        #Square both sides and then move everything to one side to get the solution
        eq = math.pow(eq, 2)
        eq -= n
        eq /= lc
        self.solution = eq
        return f"Solution: {self.solution}"

    def getEquation(self):
        if self.n < 0:
            return f"\nsqrt({self.lc}({self.solution}) {self.n}) = {self.eq}"
        else:
            return f"\nsqrt({self.lc}({self.solution}) + {self.n}) = {self.eq}"

#Class that handles single radicals with an x on the other side of =
class SingleRadicalWithX:
    def __init__(self, lc1, n1, lc2, n2):
        self.lc1 = lc1
        self.n1 = n1
        self.lc2 = lc2
        self.n2 = n2
    
    def getSolution(self):
        lc1 = self.lc1
        n1 = self.n1
        lc2 = self.lc2
        n2 = self.n2

        #Convert the equation to standard form and get it = 0
        lc3 = 2 * (lc2 * n2)
        lc2 = int(math.pow(lc2, 2))
        n2 = int(math.pow(n2, 2))
        lc3 -= lc1
        n2 -= n1

        #Check if a, b, and c have a factor in common and if so, divide them out
        for i in range(lc2, 0, -1):
            if (lc2 % i) == 0 and (lc3 % i) == 0 and (n2 % i) == 0:
                lc2 /= i
                lc3 /= i
                n2 /= i
                break

        #Factoring the product of a and c
        product = int(lc2) * int(n2)
        factors = []
        possible_solutions = []

        #If a * c < 0 then count down from -1
        if product < 0:
            for i in range(-1, product - 1, -1):
                if product % i == 0:
                    factors.append(i)
                    factors.append(-i)

        #Otherwise count up from 1
        else:
            for i in range(1, product + 1):
                if product % i == 0:
                    factors.append(i)
                    factors.append(-i)

        if len(factors) == 0:
            return "Error: Factoring Error."

        #If the factors of a and c add to equal b then add them to a list of possible solutions
        for i in range(0, len(factors)):
            for j in range(0, len(factors)):
                if factors[j] + factors[i] == lc3:
                    if not -factors[j] in possible_solutions and not -factors[i] in possible_solutions:
                        #Make it negative because when converting from factored form, the signs are flipped
                        possible_solutions.append(-factors[i])
                        possible_solutions.append(-factors[j])

        #No need to subtract and there is no equals value, so pass in null
        null = "null"
        return verifySolutions(possible_solutions, self.lc1, self.n1, self.lc2, self.n2, null, null)

    def getEquation(self):
        if self.n1 < 0:
            side1 = f"sqrt({self.lc1}x {self.n1})"
        else:
            side1 = f"sqrt({self.lc1}x + {self.n1})"

        if self.n2 < 0:
            side2 = f"{self.lc2}x {self.n2}"
        else:
            side2 = f"{self.lc2}x + {self.n2}"

        return f"\n{side1} = {side2}"

#Class that handles equations with 2 radicals, and adding/subtracting them.
class DoubleRadical:
    def __init__(self, lc1, n1, lc2, n2, eq, isSubtracting):
        self.lc1 = lc1
        self.n1 = n1
        self.lc2 = lc2
        self.n2 = n2
        self.eq = eq
        self.isSubtracting = isSubtracting

    def getSolution(self):
        lc1 = self.lc1
        n1 = self.n1
        lc2 = self.lc2
        n2 = self.n2
        eq = self.eq

        #Isolate one of the radicals and square
        lc1 -= lc2
        n1 -= int(math.pow(eq, 2) + n2)
        lc2 = int(math.pow((2 * eq), 2) * lc2)
        n2 = int(math.pow((2 * eq), 2) * n2)

        #Convert to standard form and get it = 0
        lc3 = 2 * (lc1 * n1)
        lc1 = int(math.pow(lc1, 2))
        n1 = int(math.pow(n1, 2))
        lc3 -= lc2
        n1 -= n2

        #Check if a, b, and c have a factor in common and if so, divide them out
        for i in range(lc1, 0, -1):
            if (lc1 % i) == 0 and (lc3 % i) == 0 and (n1 % i) == 0:
                lc1 /= i
                lc3 /= i
                n1 /= i
                break

        #Factoring the product of a and c
        product = int(lc1) * int(n1)
        factors = []
        possible_solutions = []

        #If a * c < 0 then count down from -1
        if product < 0:
            for i in range(-1, product - 1, -1):
                if product % i == 0:
                    factors.append(i)
                    factors.append(-i)
                    
        #Otherwise count up from 1
        else:
            for i in range(1, product + 1):
                if product % i == 0:
                    factors.append(i)
                    factors.append(-i)

        if len(factors) == 0:
            return "Error: Factoring Error."

        #If the factors of a and c add to equal b then add them to a list of possible solutions
        for i in range(0, len(factors)):
            for j in range(0, len(factors)):
                if factors[j] + factors[i] == lc3:
                    if not -factors[j] in possible_solutions and not -factors[i] in possible_solutions:
                        #Make it negative because when converting from factored form, the signs are flipped
                        #If j = i, don't duplicate the item in the list
                        if j == i:
                            possible_solutions.append(-factors[i])
                        else:
                            possible_solutions.append(-factors[i])
                            possible_solutions.append(-factors[j])

        return verifySolutions(possible_solutions, self.lc1, self.n1, self.lc2, self.n2, self.eq, self.isSubtracting)

    def getEquation(self):
        rad1 = ""
        rad2 = ""

        if self.n1 < 0:
            rad1 = f"sqrt({self.lc1}x {self.n1})"
        else:
            rad1 = f"sqrt({self.lc1}x + {self.n1})"
        if self.n2 < 0:
            rad2 = f"sqrt({self.lc2}x {self.n2})"
        else:
            rad2 = f"sqrt({self.lc2}x + {self.n2})"
        
        if self.isSubtracting == True:
            return f"\n{rad1} - {rad2} = {self.eq}"                 
        else:
            return f"\n{rad1} + {rad2} = {self.eq}"

#Verifies the possible solutions  
def verifySolutions(possible, lc1, n1, lc2, n2, eq, isSubtracting):
    verified = []
    extraneous = []

    #If it is a single radical with X
    if isSubtracting == "null":

        #For the number of possibilities
        for i in range(0, len(possible)):

            #Substitute the possible solution in for x
            #Try/except to catch if a negative number is in the square root
            try:
                term1 = int((lc2 * possible[i]) + n2)
                term2 = int(math.sqrt((lc1 * possible[i]) + n1))
            except:
                return "Error: cannot square root a negative number."
            
            #If the terms equal each other then it is a verified solution
            if term1 == term2:
                verified.append(possible[i])

            #Otherwise it is extraneous
            else:
                extraneous.append(possible[i])

    #Otherwise it is a double radical
    else:

        #For the number of possibilities
        for i in range(0, len(possible)):

            #Substitute the possible solution in for x
            #Try/except to catch if a negative number is in the square root
            try:
                term1 = int(math.sqrt((lc1 * possible[i]) + n1))
                term2 = int(math.sqrt((lc2 * possible[i]) + n2))
            except:
                return "Error: cannot square root a negative number."
            
            #If the radicals are being subtracted then subtract
            if isSubtracting == True:

                #If the terms equal each other then it is a verified solution
                if term1 - term2 == eq:
                    verified.append(possible[i])

                #Otherwise it is extraneous
                else:
                    extraneous.append(possible[i])

            #Otherwise add them
            else:

                #If the terms equal each other then it is a verified solution
                if term1 + term2 == eq:
                    verified.append(possible[i])

                #Otherwise it is extraneous
                else:
                    extraneous.append(possible[i])

    return f"Solutions:{verified} Extraneous Solutions:{extraneous}"
