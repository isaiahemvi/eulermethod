from sympy import sympify, symbols
import sympy

x,y = symbols('x y')
equation = input("Enter dy/dx: ") # gets dy/dx as user input 
expression = sympy.parsing.sympy_parser.parse_expr(equation) # parses through user input and converts to a mathematical expression

def EulersRecursive(xi,yi,h,n):
    yn = yi
    xn = xi
    xsub = expression.subs(x, xn)
    slope = xsub.subs(y, yn)  
    yn = yn + (slope*h)
    xn = xn + h

    if n==(xn):
        print(yn)
    else:
        EulersRecursive(xn,yn,h,n)
 
def EulersIterative(xi,yi,h,n):
    for a in range(0,n-xi):
        xn = xi+a
        xsub = expression.subs(x, xn) 
        slope = xsub.subs(y, yi)
        yi = yi + (slope*h)
    print(yi)

# INPUTS 
xinput = int(input("What is the initial value of x?"))
yinput = float(input("What is the initial value of y?"))
hinput = float(input("What is your step size?"))
ninput = int(input("For what n of f(n) do you want to estimate?"))
typeinput = input("Recursive, or Iterative? (Type R or I)")
if (typeinput == "R"):
    EulersRecursive(xinput, yinput, hinput, ninput)
else:
    EulersIterative(xinput, yinput, hinput, ninput)
