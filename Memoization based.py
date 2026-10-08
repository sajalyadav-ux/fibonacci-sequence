def fibo3(n,memo={}):#create dict(memo)
    if n in memo:
        return memo[n]#check n present in memo
    if n<0:
        return "invalid value"
    if n==0:
        return 0
    if n==1:
        return 1
    memo[n]=fibo3(n-1,memo)+fibo3(n-2,memo)#pass memo(write everything in this)
    return memo[n]
n=int(input("enter the value :"))
print(fibo3(n))
