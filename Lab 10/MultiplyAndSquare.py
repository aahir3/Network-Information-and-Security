def multiply_and_square(a,x,n):
    x=bin(x)
    x=x[2:] #removing extra part from binary string
    x=x[::-1] #reversing string
    y=1
    for i in range(0,len(x)):
        if (int(x[i]) == 1):
            y=(y*a)%n
        a=(a**2)%n
    return y