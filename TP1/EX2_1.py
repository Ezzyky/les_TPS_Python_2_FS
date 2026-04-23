def exp1(x,n):
    if n==0:
        return 1
    else:
        F=[1]
        f=1
        for i in range (1,n+1):
            f=f*i
            F.append(f)
        exp=0
        for i in range (0,n+1):
            exp+=(x**i)/(F[i])
        return exp
print(exp1(2,3))