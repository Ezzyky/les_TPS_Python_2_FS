def est_parfait(n):
    p=0
    for i in range(1,n):
        if n%i==0:
            p+=i
    if p==n:
       return True
    else:
        return False
print(est_parfait(6))

        