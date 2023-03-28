from latex2sympy2 import latex2sympy, latex2latex
import sys

# Terrible latex calculator
try:
 tex = sys.argv[1]
except:
    tex = input()

latex2sympy(tex)
result = latex2latex(tex)
print(result)
