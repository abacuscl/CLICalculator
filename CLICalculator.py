#Imports
import sys

#App module imports
try:
    from computation_handler import computeSolution
    from input_handler import getOperationType
except Exception as e:
    print(f"Error loading critical files\n{e}")
    input("Press Enter to quit...")
    sys.exit()

#Variables and Constants
PROG_VERSION = "v1.0.0"

#Runs the program
def run():
    printInitialText()
    while True:
        computeSolution(getOperationType())
        printDivider()

#Prints the text that appears upon first launch
def printInitialText():
    print("Command Line Calculator " + PROG_VERSION)
    print("~-------------------------------------------------------------------~")
    print("Welcome to my command line calculator built in Python\n")
    print("Typing help at any point will provide a basic help tooltip")
    print("In-depth help can be found in the User Manual document\n")
    print("Typing quit at any time will exit the program")
    print("~-------------------------------------------------------------------~")

#Prints a divider to make the interface easier to read
def printDivider():
    print("~-------------------------------------------------------------------~")

#Runs the app if this module is executed   
if __name__ == "__main__":
    run()
