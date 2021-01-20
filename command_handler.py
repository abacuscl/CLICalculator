#Imports
import os
import sys

#Executes a specified command
def executeCommand(command):
    if command == "quit":
        quitProg()
    elif command == "help":
        printHelp()
    elif command == "clear":
        clearConsole()

#Checks if a command is a valid command
def isValidCommand(command):
    if command == "quit":
        return True
    elif command == "help":
        return True
    elif command == "clear":
        return True
    else:
        return False

#Quits the program
def quitProg():
    sys.exit()

#Prints the help box
def printHelp():
    printDivider()
    print("\nValid Operators")
    print("Core Operators")
    print("+, -, *, /, ^, sqrt")
    print("\nFunction Operators")
    print("singrad - Solve a single radical equation")
    print("doubrad - Solve a radical equation with two radicals")
    print("trig - Solve a trigonometry function")
    print("polynomialwithc - Solve a polynomial function with a C value")
    print("syntheticsub - Solve a polynomial function using substitution")
    print("polynomialzeros - Solve a polynomial for its possible real zeros using P and Q")
    print("factorpolynomial - Factor the polynomial")
    print("\nAny valid number, including a decimal, will work")
    print("Typing pi will use the value of pi instead of a number")
    print("Valid Commands")
    print("quit - Quit the program")
    print("help - Bring up the help menu")
    print("clear - Clear the command line\n")
    printDivider()

#Clears the console window
def clearConsole():
    os.system("cls")

#Prints a divider to make the interface easier to read
def printDivider():
    print("~-------------------------------------------------------------------~")
