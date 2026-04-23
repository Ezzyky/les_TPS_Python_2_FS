def f(x):
    return (x**2)-2
def zero(a,b,eps):
    while b-a>eps:
        m=(a+b)/2
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
    return (a+b)/2
