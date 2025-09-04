#Assignment_7: Fixed Point Iteration and Newton Raphson
#Name: Roshan Yadav
#Roll No: 2311144
import math

def f(x,f):
    """This function defines the functions."""
    if f==0: # for question 1 returns f(x)
        a= float(3*x)
        b= math.sin(x)
        c= -math.exp(x)
        return a-b-c
    
    if f==1: # for question 1 returns derivative of f(x)
        a= float(3)
        b= math.cos(x)
        c= -math.exp(x)
        return a+b+c
    
    if f==3: # for question 2 returns f(x)
        a=x**2
        b=-2*x
        c=-3
        return a+b+c

    if f==2: # for question2 returns g(x)
        a= float(x**2)
        c= -float(3)
        return (a+c)/2

def Bisection(a=1.5,b=3.0,t=0,iter=0,e=10**-6,d=10**-6):

    """This function utilises the bisection method 
    to find te roots of a monotonic function."""

    if f(a,t) * f(b,t) <=0:
        if abs(b-a) < e:
            if abs(f(a,t)) < d:
                return a,iter
            if abs(f(b,t)) < d:
                return b,iter
    
        else:
            iter_new=iter+1
            c=(a + b)/2
            if f(c,t)*f(a,t)<0:
                return Bisection(a=a,b=c,t=t,iter=iter_new)
            if f(c,t)*f(b,t) <0:
                return Bisection(a=c,b=b,t=t,iter=iter_new)
    else:
        return 'No root found in the given interval'
    
def regular_falsi(a,b,t,iter=0,e=10**-6,d=10**-6):

    """This function utilises sthe Regular Falsi method 
    to find roots of a monotonic function."""

    if f(a,t)*f(b,t) <=0:
        if abs(b-a) < e:
            if abs(f(a,t)) < d:
                return a,iter
            if abs(f(b,t)) < d:
                return b,iter
        else:
            iter_new=iter+1
            c=a
            c_new = (b - (((b -a)*f(b,t))/(f(b,t)-f(a,t))))
            if f(a,t)*f(c_new,t) <= 0:
                if abs(c_new - c) < e: 
                    return c,iter
                else:
                    return regular_falsi(a=a,b=c_new,c=c_new,t=t,iter=iter_new)
            
            if f(b,t)*f(c,t) <= 0:
                if abs(c_new - c) < e: 
                    return c,iter
                else:
                    return regular_falsi(a=c_new,b=b,c=c_new,t=t,iter=iter_new)
            
    else:
        return 0,0


def fixed_point(x=0,t=2,iter=0,e=10**-6,max_iter=1000):
    """This Function returns roots of a 
    function employing Fixed point Method"""

    for i in range(max_iter):
        # Iteration step
        x_new = f(x,t)
        iter_new = iter + 1

        # Checking convergence
        if abs(x_new - x) < e:
            return float(x_new),float(iter_new)
    

def newton_raphson(x=2,t_0=0,t_1=1,iter=0,e=10**-6,d=10**-6):
    """This Function returns roots of a 
    function employing Newton-Raphson Method"""

    # Iteration step
    a=f(x,t_0)
    b=f(x,t_1)
    x_new= x-(a/b)
    iter_new = iter + 1

    # Checking convergence
    if abs(x_new - x) < e and abs(f(x_new,t_0)) < d:
        return x_new,iter
    else:
        return newton_raphson(x=x_new,t_0=t_0,t_1=t_1,iter=iter_new)



