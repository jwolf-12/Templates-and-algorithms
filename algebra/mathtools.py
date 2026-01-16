import operator as op
from functools import reduce
#operator gives function like op.mul(which is basically multiplication)
#reduce is reduce(f,arr,init). f on arr and init is initial value

#euclidian algorithm (gdc is also built in in python)
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

