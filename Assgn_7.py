#Assignment_7: Fixed Point Iteration and Newton Raphson
#Name: Roshan Yadav
#Roll No: 2311144

from Func_lib_for_assgn_7 import *

# Question-1: Finding Roots of f(x)= 3x + sin(x) - exp(x)

## By Bisection method:
root,iter=Bisection(a=-1.5,b=1.5,t=0)
print(f'\nRoot of f(x) = 3x + sin(x) - exp(x), found by Bisection method in {iter}, is {root}.')

## By Regular Falsi:
root,iter =regular_falsi(a=-1.5,b=1.5,t=0)
print(f'\nRoot of f(x) = 3x + sin(x) - exp(x), found by Regular Falsi in {iter}, is {root}.')

## By Newton Raphson Method:
root,iter =newton_raphson(x=0,t_0=0,t_1=1)
print(f'\nRoot of f(x) = 3x + sin(x) - exp(x), found by Newton Raphson method in {iter}, is {root}.')



# Question-2: Finding Roots of f(x)= x^2 -2x -3 using fixed point method

#root,iter=fixed_point(x=0,t=2)
#print(f'\nRoot of f(x)= x^2 -2x -3, found by Fixed Point method in {iter}, is {root}.')



# Outputs #

## Output of question-1 by Bisection method:Root of f(x) = 3x + sin(x) - exp(x), found by Bisection method in 22, is -0.34912705421447754.

## Output of question-1 by Regular Falsi method:Root of f(x) = 3x + sin(x) - exp(x)-0.34912705421447754.

## Output of question-1 by Newton-Raphson method:Root of f(x) = 3x + sin(x) - exp(x) -0.34912705421447754.

## Output of question-2 by Fixed point method:Root of f(x) = 3x + sin(x) - exp(x) is -1