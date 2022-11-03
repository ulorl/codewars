from sympy import Symbol, diff
import re

def differentiate(equation, point):
    equation = equation.replace('^', '**')
    equation = re.sub(r'(\d+)(x)', r'\1*\2',  equation)
    x = Symbol('x')
    y = diff(equation)
    return y.subs(x, point)

print(differentiate("12x+2", 3), 12)
print(differentiate("x^2-x", 3), 5)
print(differentiate("-5x^2+10x+4", 3), -20)
