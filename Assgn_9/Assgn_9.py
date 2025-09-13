#Name:Roshan Yadav
#Roll No: 2311144
#Assignment_9: Finding Roots of polynomial

from Func_for_assgn_9 import *

# Initial Guess
a=pRNG()

# For P_1(x):= x^4 - x^3 -7x^2 + x + 6

L_1=[1,-1,-7,1,6]
P_1 = poly(L_1)
print(f"\nFinding Roots of P_1(x):= x^4 - x^3 -7x^2 + x + 6") # Output= Finding Roots of P_1(x):= x^4 - x^3 -7x^2 + x + 6
Roots= P_1.root(a)
print(f"\nRoots of P_1 is {Roots}") # Output= Roots of P_1 is [0.9999999973060356, -0.9999999959590532, 3.000000000808189, -2.0000000021551716]

# For P_2(x):= x^4 -5x^2 + 4

L_2=[1,0,-5,0,4]
P_2 = poly(L_2)
print(f"\nFinding Roots of P_2(x):= x^4 -5x^2 + 4") # Output= Finding Roots of P_2(x):= x^4 -5x^2 + 4
Roots= P_2.root(a)
print(f"\nRoots of P_2 is {Roots}") # Output= Roots of P_2 is [0.9999999504535537, -0.9999999504518052, 2.0000000247727856, -2.000000024774534]

# For P_3(x):= 2x^5 - 19.5x^3 + 0.5x^2 + 13.5x - 4.5

L_3=[2,0,-19.5,0.5,13.5,-4.5]
P_3 = poly(L_3)
print(f"\nFinding Roots of P_3(x):= 2x^5 - 19.5x^3 + 0.5x^2 + 13.5x - 4.5") # Output=Finding Roots of P_3(x):= 2x^5 - 19.5x^3 + 0.5x^2 + 13.5x - 4.5
Roots= P_3.root(a)
print(f"\nRoots of P_3 is {Roots}") # Output= Roots of P_3 is [0.5001317512702191, 0.49986823914063494, -0.9999999873419141, 2.9999999984810297, -3.00000000154997]
