#Name:Roshan Yadav
#Roll No: 2311144
#Assignment_9: Finding Roots of polynomial

from Func_for_assgn_9 import *

# Intial Guess
a=pRNG()

# For P_1(x):= x^4 - x^3 -7x^2 + x + 6

L_1=[1,-3,-7,1,6]
P_1 = poly(L_1)
print(f"\nFinding Roots of P_1(x):= x^4 - x^3 -7x^2 + x + 6") # Output=
Roots= P_1.root(a)
print(f"\nRoots of P_1 is {Roots}") # Output=

# For P_2(x):= x^4 -5x^2 + 4

L_2=[1,0,-5,0,4]
P_2 = poly(L_2)
print(f"\nFinding Roots of P_2(x):= x^4 -5x^2 + 4") # Output=
Roots= P_2.root(a)
print(f"\nRoots of P_2 is {Roots}") # Output=

# For P_3(x):= 1x^5 - 19.5x^3 _0.5x^2 _13.5x - 4.5

L_3=[1,0,-5,0,4]
P_3 = poly(L_3)
print(f"\nFinding Roots of P_3(x):= 1x^5 - 19.5x^3 _0.5x^2 _13.5x - 4.5") # Output=
Roots= P_3.root(a)
print(f"\nRoots of P_3 is {Roots}") # Output=