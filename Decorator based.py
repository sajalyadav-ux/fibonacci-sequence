#fibonacci sequence by decorater
from functools import lru_cache
@lru_cache(maxsize=None)
def fibo(n):
    if n<0:
        return "invalid number"
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
n=int(input("enter the value :"))
print(fibo(n))
