from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets
def fun(x):
    return x
#interact(fun,x=10)
interact(fun,x=True)  # to create a checkbox
@interact(x=True,y=1.0)
def g(x,y):
    return(x,y)

interact(fun,x=['a','b','c'])
interact(fun,x={'a':10,'b':20,'c':30})

from IPython.display import display
def f(a,b):
    display(a+b)
    return a+b
w=interactive(f,a=10,b=15)
display(w)

