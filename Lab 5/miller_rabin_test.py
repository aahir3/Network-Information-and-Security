from MultiplyAndSquare import multiply_and_square
from random import randint
def millar_rabin(n):
    k=0
    d=n-1
    while (d % 2 == 0):
        k+=1
        d//=2
    if(d!= n-1):
        m=d
    else:
        m=n-1
    a=2+randint(0,n-4)
    b=multiply_and_square(a,m,n)
    if(b % n == 1):
        return True
    for i in range(k+1):
        if (b % n == n-1):
            return True
        else:
            b=b**2 % n
    return False

if __name__ == "__main__":
    n=int(input())
    if(millar_rabin(n) == True):
        print("n is prime")
    else:
        print("n is not prime(composite)")