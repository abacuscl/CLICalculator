'''
This class is structutred differently than others so more
detail will be given in comments to provide clarification
'''

#Imports
import math

#Class that handles synthetic division
class SyntheticDivision:
    def __init__(self, lcs, n):
        self.lcs = lcs
        self.n = n

    #Gets a solution with a specified C number
    def getSolutionWithC(self, c):
        self.c = c
        c = -c
        lcs = self.lcs

        #Performs synthetic division on the equation's LCs 
        new_nums = []
        temp = 0
        remainder = 0
        for i in range(0, len(lcs) + 1):

            #If it's the first LC, then keep it as-is
            if i == 0:
                new_nums.append(lcs[i])
                temp = lcs[i]

            #If it's the last number, then calculate the remainder
            elif i == len(lcs):
                remainder = (c * temp) + self.n

            #Otherwise, calculate the next number to +/- with the next LC
            else:
                temp = (c * temp) + lcs[i]
                new_nums.append(temp)

        #Formats the equation
        equation = "\n"
        exp = 0
        for i in range(0, len(new_nums)):
            exp = len(new_nums) - i - 1
            if new_nums[i] < 0:
                if i == len(new_nums) - 1:
                    equation += f"{new_nums[i]} "
                else:
                    if exp == 1:
                        equation += f"{new_nums[i]}x "
                    else:
                        equation += f"{new_nums[i]}x^{exp} "
            else:
                if i == 0:
                    equation += f"{new_nums[i]}x^{len(new_nums) - 1} "
                elif i == len(new_nums) - 1:
                    equation += f"+ {new_nums[i]} "
                else:
                    if exp == 1:
                        equation += f"+ {new_nums[i]}x "
                    else:
                        equation += f"+ {new_nums[i]}x^{exp} "

        if self.c < 0:
            if remainder < 0:
                equation += f"{remainder}/x{self.c}"
            else:
                equation += f"+ {remainder}/x{self.c}"
        else:
            if remainder < 0:
                equation += f"{remainder}/x+{self.c}"
            else:
                equation += f"+ {remainder}/x+{self.c}"

        return equation

    #Performs synthetic substitution, essentially synthetic division but returning the remainder
    def doSyntheticSubstitution(self, c):
        self.c = c
        lcs = self.lcs

        #Performs synthetic division like above
        new_nums = []
        temp = 0
        remainder = 0
        for i in range(0, len(lcs) + 1):
            if i == 0:
                new_nums.append(lcs[i])
                temp = lcs[i]
            elif i == len(lcs):
                remainder = (c * temp) + self.n
            else:
                temp = (c * temp) + lcs[i]
                new_nums.append(temp)
        
        return f"\nf({c}) = {remainder}"

    #Gets the possible real zeros
    def getZeros(self, q, p):
        factors_q = []
        factors_p = []
        lis = []

        #Finding the factors of Q
        if q < 0:
            for i in range(-1, int(q - 1), -1):
                if q % i == 0:
                    factors_q.append(int(q / i))
        else:
            for i in range(1, int(q + 1)):
                if q % i == 0:
                    factors_q.append(int(q / i))

        #Finding the factors of P
        if p < 0:
            for i in range(-1, int(p - 1), -1):
                if p % i == 0:
                    factors_p.append(int(p / i))
        else:
            for i in range(1, int(p + 1)):
                if p % i == 0:
                    factors_p.append(int(p / i))

        #Dividing the factors by each other once to form the list
        for i in range(0, len(factors_p)):
            for j in range(0, len(factors_q)):
                temp = factors_p[i]/factors_q[j]

                #If it is an integer, then leave it as an integer
                if temp.is_integer():
                    if not temp in lis:
                        lis.append(temp)

                #Otherwise, format the fraction as a string
                else:
                    temp = f"{factors_p[i]}/{factors_q[j]}"
                    if not temp in lis:
                        lis.append(temp)
        
        return f"\n+/-{lis}"

    #Fully factors the function        
    def fullyFactor(self, q, p):
        factors_q = []
        factors_p = []
        qp_list = []
        lcs = self.lcs

        #Gets the factors of Q
        if q < 0:
            for i in range(-1, int(q - 1), -1):
                if q % i == 0:
                    factors_q.append(int(q / i))
        else:
            for i in range(1, int(q + 1)):
                if q % i == 0:
                    factors_q.append(int(q / i))

        #Gets the factors of P
        if p < 0:
            for i in range(-1, int(p - 1), -1):
                if p % i == 0:
                    factors_p.append(int(p / i))
        else:
            for i in range(1, int(p + 1)):
                if p % i == 0:
                    factors_p.append(int(p / i))

        #Dividing to create the full list
        for i in range(0, len(factors_p)):
            for j in range(0, len(factors_q)):

                #This time, the numbers are left as floats and not converted to strings
                temp = factors_p[i]/factors_q[j]
                temp2 = -(factors_p[i]/factors_q[j])
                if not temp in qp_list:
                    qp_list.append(temp)
                if not temp2 in qp_list:
                    qp_list.append(temp2)

        #Perform synthetic division
        #The loop will run until the degree on the equation is 2
        new_nums = []
        factors = []
        temp = 0
        remainder = 0
        cur_degree = len(lcs)

        #Runs through the list of Q and P
        for i in range(0, len(qp_list)):
            c = qp_list[i]
            for j in range(0, len(lcs) + 1):
                if j == 0:
                    new_nums.append(lcs[j])
                    temp = lcs[j]
                elif j == len(lcs):
                    remainder = (c * temp) + self.n
                else:
                    temp = (c * temp) + lcs[j]
                    new_nums.append(temp)

            #If the remainder is 0, then save the values
            if remainder == 0:
                cur_degree -= 1
                
                #Save the N variable and take out N from the list of LCs
                self.n = new_nums[len(new_nums) - 1]
                new_nums.remove(new_nums[len(new_nums) - 1])

                #Save the current LCs as the new LCs and reset the list
                lcs = new_nums
                new_nums = []

                #Append the factors of the function
                factors.append(-qp_list[i])

                #If there are 2 degrees left, then stop
                if cur_degree == 2:
                    break
                
            new_nums = []

        #Format the equation
        equation = "\n"
        for i in range(0, len(factors)):
            if factors[i] < 0:
                equation += f"(x {factors[i]})"
            else:
                equation += f"(x + {factors[i]})"
        equation += f"({lcs[0]}x^2 "
        if lcs[1] < 0:
            equation += f"{lcs[1]}x "
        elif lcs[1] == 0:
            pass
        else:
            equation += f"+ {lcs[1]}x "

        if self.n < 0:
            equation += f"{self.n})"
        elif self.n == 0:
            pass
        else:
            equation += f"+ {self.n})"

        return equation
