#Imports
import math
import sys

#App module imports
try:
    from command_handler import isValidCommand, executeCommand
except Exception as e:
    print(f"Error loading critical files\n{e}")
    input("Press Enter to quit...")
    sys.exit()

'''
General Purpose Methods
'''
#Prints the number prompt based on the type of equation
def printPrompt(prompt):
    if prompt == "coreN":
        print("\nEnter a number")
    elif prompt == "coreN2":
        print("\nEnter a second number")
    elif prompt == "generic":
        print("\nEnter a number")
    elif prompt == "radLC":
        print("\nEnter a leading coefficient")
    elif prompt == "radN":
        print("\nEnter the following number")
    elif prompt == "radLC2":
        print("\nEnter a second leading coefficient")
    elif prompt == "radN2":
        print("\nEnter the second following number")
    elif prompt == "radequals":
        print("\nEnter what the equation equals")
    elif prompt == "A":
        print("\nEnter angle A in degrees")
    elif prompt == "a":
        print("\nEnter side a")
    elif prompt == "b":
        print("\nEnter side b")
    elif prompt == "c":
        print("\nEnter side c")
    elif prompt == "lcquantity":
        print("\nEnter the highest exponent in the function")
    elif prompt == "polyn":
        print("\nEnter the value of the final number in the function")
    elif prompt == "polyq":
        print("\nEnter the value of Q (The same as the first leading coefficient)")
    elif prompt == "polyp":
        print("\nEnter the value of P (The same as the last number, not a coefficient)")
    elif prompt == "polyc":
        print("\nEnter the value of c")

#Checks if the operator is valid
def isValidOperator(usrin):
    if usrin == ("+"):
        return True
    elif usrin == ("-"):
        return True
    elif usrin == ("*"):
        return True
    elif usrin == ("/"):
        return True
    elif usrin == ("^"):
        return True
    elif usrin == ("sqrt"):
        return True
    elif usrin == ("singrad"):
        return True
    elif usrin == ("doubrad"):
        return True
    elif usrin == ("trig"):
        return True
    elif usrin == ("polynomialwithc"):
        return True
    elif usrin == ("syntheticsub"):
        return True
    elif usrin == ("polynomialzeros"):
        return True
    elif usrin == ("factorpolynomial"):
        return True
    else:
        return False

#Gets a number input from the user
def getNum(userPrompt):
    while True:
        printPrompt(userPrompt)
        usrin = input(">>>")
        usrin = usrin.casefold().replace(" ", "")

        if isValidCommand(usrin):
            executeCommand(usrin)
        elif usrin == "pi":
            return math.pi
        else:
            try:
                return float(usrin)
            except:
                print("Invalid number.")

#Gets the input for the operation type
def getOperationType():
    while True:
        print("\nEnter the operation type")
        usrin = input(">>>")
        usrin = usrin.casefold().replace(" ", "")

        if isValidCommand(usrin):
            executeCommand(usrin)
        elif isValidOperator(usrin):
            return usrin
        else:
            print("Invalid entry.")

'''
Core Operator Methods
'''
#Gets the first number for a core operator
def getCoreOpN():
    return getNum("coreN")

#Gets the second number for a core operator
def getCoreOpN2():
    return getNum("coreN2")

'''
Radical Function Methods
'''
#Gets the first radical leading coefficient
def getRadLC():
    return getNum("radLC")

#Gets the first radical's number following x
def getRadN():
    return getNum("radN")

#Gets the second radical leading coefficient
def getRadLC2():
    return getNum("radLC2")

#Gets the second radical's number following x
def getRadN2():
    return getNum("radN2")

#Gets the number that the radical equation equals
def getRadEQ():
    return getNum("radequals")

#Gets whether two radicals are being added or subtracted
def getRadAddOrSub():
    while True:
        print("\nAre the radicals being added or subtracted\n")
        print("[1]Added     [2]Subtracted")
        usrin = input(">>>")
        usrin = usrin.casefold().replace(" ", "")

        if isValidCommand(usrin):
            executeCommand(usrin)
        elif usrin == "1":
            return False
        elif usrin == "2":
            return True
        else:
            print("Invalid input.")

#Checks if the user is entering an equation with an x in the equals or not
def isSingleRadWithX():
    while True:
        print("\nDoes the equation have an x variable on the side of equals opposite the radical\n")
        print("[1]Yes     [2]No")
        usrin = input(">>>")
        usrin = usrin.casefold().replace(" ", "")

        if isValidCommand(usrin):
            executeCommand(usrin)
        elif usrin == "1":
            return True
        elif usrin == "2":
            return False
        else:
            print("Invalid input.")

'''
Trigonometry Function Methods
'''
#Gets a number for a trigonometry function
def getTrigNum(prompt):
    return getNum(prompt)

#Gets the type of trigonometry function
def getTrigType():
    while True:
        print("\nSelect a Trigonometric function\n")
        print("[0] - sine(Angle)")
        print("[1] - cosine(Angle)")
        print("[2] - tangent(Angle)")
        print("[3] - Inverse sine(Angle)")
        print("[4] - Inverse cosine(Angle)")
        print("[5] - Inverse tangent(Angle)")
        print("[6] - Side a using sine")
        print("[7] - Side a using tangent")
        print("[8] - Side a using Pythagorean Theorem")
        print("[9] - Side b using cosine")
        print("[10] - Side b using tangent")
        print("[11] - Side b using Pythagorean Theorem")
        print("[12] - Side c using sine")
        print("[13] - Side c using cosine")
        print("[12] - Side c using Pythagorean Theorem\n")
        usrin = input(">>>")
        usrin = usrin.casefold().replace(" ", "")

        if isValidCommand(usrin):
            executeCommand(usrin)
        elif isValidTrigFunction(convertTrigSelection(usrin)):
            return convertTrigSelection(usrin)
        else:
            print("Invalid entry.")

#Checks if the user input is a valid trigonometry function
def isValidTrigFunction(usrin):
    if usrin == "sin":
        return True
    elif usrin == "cos":
        return True
    elif usrin == "tan":
        return True
    elif usrin == "invsin":
        return True
    elif usrin == "invcos":
        return True
    elif usrin == "invtan":
        return True
    elif usrin == "sideasin":
        return True
    elif usrin == "sideatan":
        return True
    elif usrin == "sideapyth":
        return True
    elif usrin == "sidebcos":
        return True
    elif usrin == "sidebtan":
        return True
    elif usrin == "sidebpyth":
        return True
    elif usrin == "sidecsin":
        return True
    elif usrin == "sideccos":
        return True
    elif usrin == "sidecpyth":
        return True
    else:
        return False

#Converts the trig selection from an integer to a working operation type
def convertTrigSelection(usrin):
    if usrin == "0":
        return "sin"
    elif usrin == "1":
        return "cos"
    elif usrin == "2":
        return "tan"
    elif usrin == "3":
        return "invsin"
    elif usrin == "4":
        return "invcos"
    elif usrin == "5":
        return "invtan"
    elif usrin == "6":
        return "sideasin"
    elif usrin == "7":
        return "sideatan"
    elif usrin == "8":
        return "sideapyth"
    elif usrin == "9":
        return "sidebcos"
    elif usrin == "10":
        return "sidebtan"
    elif usrin == "11":
        return "sidebpyth"
    elif usrin == "12":
        return "sidecsin"
    elif usrin == "13":
        return "sideccos"
    elif usrin == "14":
        return "sidecpyth"

'''
Polynomial Function Methods
'''
#Gets the list of leading coefficients based on a user specified number of exponents
def getLeadingCoeffs():
    count = getNum("lcquantity")
    lcs = []
    
    while True:
        print(f"\nEnter the leading coefficient for x^{count}")
        print("If the next degree in sequence does not exist, then enter 0")

        usrin = input(">>>")
        usrin = usrin.replace(" ", "").casefold()

        if isValidCommand(usrin):
            executeCommand(usrin)
        elif usrin == "pi":
            lcs.append(math.pi)
            count -= 1
        else:
            try:
                lcs.append(float(usrin))
                count -= 1
                if count == 0:
                    return lcs
            except:
                print("Invalid number.")

#Gets the variable N
def getPolynomialN():
    return getNum("polyn")

#Gets the variable Q
def getPolynomialQ():
    return getNum("polyq")

#Gets the variable P
def getPolynomialP():
    return getNum("polyp")

#Gets the variable C
def getPolynomialC():
    return getNum("polyc")               
