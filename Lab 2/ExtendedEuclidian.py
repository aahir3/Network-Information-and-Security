def multiplicative_inverse(a,n):
    r,t,t1,t2=0,0,0,1
    r1=n
    r2=a
    while(r2 > 0):
        q=r1//r2
        r=r1-q*r2
        r1=r2
        r2=r
        t=t1-q*t2
        t1=t2
        t2=t
    return r1,t1

a,n=map(int,input().split())
gcd,inverse=multiplicative_inverse(a,n)
inverse=inverse%n
if( gcd != 1):
    inverse=-1 #Here,-1 shows that Inverse is not possible
print("gcd is : "+str(gcd)+"  inverse is : "+str(inverse))