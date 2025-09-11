#Name:Roshan Yadav
#Roll No: 2311144
#Assignment_9: Finding Roots of polynomial

import math


class poly():

    """This Class defines a polynomial and 
    does various operations on it."""
    
    def __init__(self,L):

        """If P(x) = sum(i=n to 0)( (a_i) * (x^i)), 
        then L is list of coefficients i.e L= {a_i}
        for all i=(n to 0) where n is the degree of the polynomial"""

        self.coff = L
        self.degree = len(L) - 1

    def comp(self,a):

        """ This function computes P(a). """

        N=self.coff
        n=len(N)
        val=0

        for i in range(n):
            val = val + (N[i])*(a**(n-1-i))

        return val
         
        

    def poly_der(self,m):

        """ This Function returns the mth derivative 
        of the polynomial"""

        C=self.coff
        n=len(C)
        R=[]
        for i in range(m):
            for j in range(n):
                a= (C[j]) *(n-1-j)
                R.append(a)
        b=poly(R)
        return b
    
    def SDM(self,a):

        """ This function does synthetic division of P(x)
        by x-a where input 'a' is a root of P(x). """

        R=[]
        R.append(0)
        L=self.coff
        n=len(L)
        
        for i in range(n-1):
            b=L[i] + a*R[i]
            R.append(b)
        
        c=poly(R)

        return c
    
    def lag(self,a,e=10**-6,max_iter=100):

        """ This Function finds one root of polynomial through
        Laguerre's Method. The input 'a' is the intial guess 
        and e is the error tolerence. """

        if abs(self.comp(a)) < e:
            return a
        else:
            n=self.degree
            P_1=self.poly_der(1)
            P_2=self.poly_der(2)

            G= P_1.comp(a)/self.comp(a)
            H= G**2 - (P_2.comp(a)/self.comp(a)) 

            d_1=(G + ((n-1*(n*H - G**2)))**0.5)
            d_2=(G - ((n-1*(n*H - G**2)))**0.5)

            if abs(d_1) > abs(d_2):
                d = d_1

            else:
                d = d_2
            
            b=n/d

            a_new=a-b

            for i in range(max_iter):
                if abs(a_new - a) < e:
                    return a
                elif i == max_iter -1:
                    return a
                else:
                    return self.lag(self,a_new)
            
    def root(self,a):

        """ This Function finds roots of polynomial through
        Laguerre's Method and do deflation through synthetic 
        division method. The input 'a' is the intial guess 
        and e is the error tolerence. """

        R=[]
        n=self.degree
        P=poly(self.coff)

        for i in range(n):
            r=P.lag(a)
            R.append(a)
            P=self.SDM(r)
        
        return R
            

def pRNG(s=0.1, c=3.95, n=10000):
    '''This function is a Pseudo random number generator 
    which uses equation x(i+1) = c*x(i)*(1-x(i)), 
    where x(0)=s and c are given as input.
    Returns a list of n random numbers'''

    L = []
    L.append(s)  # x(0) = s
    
    for i in range(n-1):
        t = c * L[i] * (1 - L[i])  # x(i+1) = c*x(i)*(1-x(i))
        L.append(t)
    
    return L[n]





        



        