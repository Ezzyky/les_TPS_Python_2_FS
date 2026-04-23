def fct(n):
    if n==0:
        return 1
    else:
        f=1
        for i in range (1,n+1):
            f*=i
    return f
def exp1(x,n):
        exp=1
        for i in range (1,n+1):
            exp+=(x**i)/(fct(i))
        return exp
def exp2(x):
    e=10**(-8)
    i=0
    s=0
    t=1
    while True:
        t=(x**i)/fct(i)
        if t<e:
            break
        else:
            s+=t
            i+=1  
    return s
print(exp2(8))
