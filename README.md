 # CLICalculator
 A versatile calculator with a command line interface.

 Currently tested and verified to work on Windows only, but it may work 
 on other operating systems.

 ----
 ## Table of Contents
 -[Features](#features)  
 -[Technologies](#technologies)  
 -[Setup](#setup)  
 -[Usage](#usage)  
 -[Disclaimer](#disclaimer)  
 -[Ideas to Implement](#ideas-to-implement)  
 
 ----
 ## Features
 - Command line interface
 - Basic commands
 - Basic and complex functions
 
 ### Basic Functions
 - `+`
 - `-`
 - `/`
 - `*`
 - `^`
 - `sqrt`
 
 ### Complex Functions
 - `singrad` 
   - Solve a single radical equation
 - `doubrad`
   - Solve an equation with two radicals
 - `trig`
   - Solve a trigonometry function
 - `polynomialwithc`
   - Solve a polynomial function with a C value
 - `syntheticsub`
   - Solve a polynomial using substitution
 - `polynomialzeros`
   - Find the possible real zeros using the P and Q value
 - `factorpolynomial`
   - Factor a polynomial
 
 ### Commands
 - `help`
   - Brings up the help menu
 - `quit`
   - Quits the application
 - `clear`
   - Clears the command line
 
 ----
 ## Technologies
 Created with:
 - Python 3.8.7
 
 ----
 ## Setup
 To use this application, you need [Python](https://www.python.org/downloads/) 3.8+ 
 and [Git](https://git-scm.com/downloads) if you intend to clone using the command line.
 
 Using Git:
 ```
 git clone https://github.com/abacuscl/CLICalculator.git
 
 cd clicalculator
 
 python CLICalculator.py
 ```
 
 Cloning from web browser:
 
 1. Clone the repository as a .zip file
 
 2. Unzip the file in the desired directory
 
 3. Open the CLICalculator folder and double click on CLICalculator.py
 
 Or:
 
 1. Clone the CLICalculator.exe file from the dist folder
 
 2. Double click on the .exe file
 
 ----
 ## Usage
 
 ### Using the App
 Using the command line interface is simple and prompts are given for actions that
 can be performed. The valid operators can be found [here](#features) and in the
 help menu in the app. 
 
 ### Disclaimer
 I have made the calculator to the best of my ability and I have run multiple tests
 to ensure accuracy. However, results should not be relied upon to be accurate in
 critical situations and scenarios. If you are going to use this calculator, checking
 the results of the calculator is strongly advised.
 
 ### Inaccurate Results
 If you do find a result that is inaccurate, please create a new issue on the repository
 page with the following information:
 - Type of function used
 - All numbers entered as parameters
 - The inaccurate result
 - The correct result
 
 ----
 ## Bug Report
 To open a bug report or feature request, create an issue on the repository page.
 
 ----
 ## Ideas to Implement
 - [ ] New functions
