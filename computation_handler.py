#Imports
import sys

#Enabling access to the functions directory
sys.path.append("..")

#App module imports
try:
    from functions import *
    from input_handler import *
except Exception as e:
    print(f"Error loading critical files\n{e}")
    input("Press Enter to quit...")
    sys.exit()

#Computes the solution based on the operation type
def computeSolution(op_type):
    if op_type == "+":
        a = Addition(getCoreOpN(), getCoreOpN2())
        print(f"\nThe solution is: {a.getSolution()}")
        print(a.getEquation())
    elif op_type == "-":
        s = Subtraction(getCoreOpN(), getCoreOpN2())
        print(f"\nThe solution is: {s.getSolution()}")
        print(s.getEquation())
    elif op_type == "*":
        m = Multiplication(getCoreOpN(), getCoreOpN2())
        print(f"\nThe solution is: {m.getSolution()}")
        print(m.getEquation())
    elif op_type == "/":
        d = Division(getCoreOpN(), getCoreOpN2())
        print(f"\nThe solution is: {d.getSolution()}")
        print(d.getEquation())
    elif op_type == "^":
        p = Power(getCoreOpN(), getCoreOpN2())
        print(f"\nThe solution is: {p.getSolution()}")
        print(p.getEquation())
    elif op_type == "sqrt":
        sq = SquareRoot(getCoreOpN())
        print(f"\nThe solution is: {sq.getSolution()}")
        print(sq.getEquation())
    elif op_type == "singrad":
        if isSingleRadWithX():
            srx = SingleRadicalWithX(getRadLC(), getRadN(), getRadLC2(), getRadN2())
            print(srx.getEquation())
            print(srx.getSolution())
        else:
            sr = SingleRadical(getRadLC(), getRadN(), getRadEQ())
            print(sr.getSolution())
            print(sr.getEquation())
    elif op_type == "doubrad":
        dr = DoubleRadical(getRadLC(), getRadN(), getRadLC2(), getRadN2(), getRadEQ(), getRadAddOrSub())
        print(dr.getEquation())
        print(dr.getSolution())
    elif op_type == "trig":
        usrin = getTrigType()
        t = Trigonometry(usrin)
        if usrin == "sin":
            print(t.getSolution(getTrigNum("A"), "null"))
        elif usrin == "cos":
            print(t.getSolution(getTrigNum("A"), "null"))
        elif usrin == "tan":
            print(t.getSolution(getTrigNum("A"), "null"))
        elif usrin == "invsin":
            print(t.getSolution(getTrigNum("a"), getTrigNum("c")))
        elif usrin == "invcos":
            print(t.getSolution(getTrigNum("b"), getTrigNum("c")))
        elif usrin == "invtan":
            print(t.getSolution(getTrigNum("a"), getTrigNum("b")))
        elif usrin == "sideasin":
            print(t.getSolution(getTrigNum("A"), getTrigNum("c")))
        elif usrin == "sideatan":
            print(t.getSolution(getTrigNum("A"), getTrigNum("b")))
        elif usrin == "sideapyth":
            print(t.getSolution(getTrigNum("c"), getTrigNum("b")))
        elif usrin == "sidebcos":
            print(t.getSolution(getTrigNum("A"), getTrigNum("c")))
        elif usrin == "sidebtan":
            print(t.getSolution(getTrigNum("A"), getTrigNum("a")))
        elif usrin == "sidebpyth":
            print(t.getSolution(getTrigNum("c"), getTrigNum("a")))
        elif usrin == "sidecsin":
            print(t.getSolution(getTrigNum("A"), getTrigNum("a")))
        elif usrin == "sideccos":
            print(t.getSolution(getTrigNum("A"), getTrigNum("b")))
        elif usrin == "sidecpyth":
            print(t.getSolution(getTrigNum("a"), getTrigNum("b")))
        print(t.getEquation())
    elif op_type == "polynomialwithc":
        sdiv = SyntheticDivision(getLeadingCoeffs(), getPolynomialN())
        print(sdiv.getSolutionWithC(getPolynomialC()))
    elif op_type == "syntheticsub":
        sdiv = SyntheticDivision(getLeadingCoeffs(), getPolynomialN())
        print(sdiv.doSyntheticSubstitution(getPolynomialC()))
    elif op_type == "polynomialzeros":
        sdiv = SyntheticDivision("null" , "null")
        print(sdiv.getZeros(getPolynomialQ(), getPolynomialP()))
    elif op_type == "factorpolynomial":
        sdiv = SyntheticDivision(getLeadingCoeffs() , getPolynomialN())
        print(sdiv.fullyFactor(getPolynomialQ(), getPolynomialP()))
        

