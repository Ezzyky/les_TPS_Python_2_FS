def crible_eratoshene(n):
    p=[True]*(n+1)
    p[0]=p[1]=False
    i=2
    P1=[]
    while i*i<=n:
        if p[i]:
            for j in range (i*2,n+1,i):
                p[j]=False
        i+=1
    for i in range(2,n+1):
        if p[i]==True:
            P1.append(i)
    return P1
print (crible_eratoshene(1000))