from random import randint
from MultiplyAndSquare import multiply_and_square as ms
from ExtendedEuclidian import multiplicative_inverse as mi

def primitive_roots_order(p):
    order=[None]*p
    for r in range(1,p):
        first_one=True
        for c in range(1,p):
            mas=ms(r,c,p)
            if((first_one) and (mas == 1)):
                order[r]=c
                first_one=False
    return order
def all_roots(order,p):
    proots=[]
    phi_p=phi(p)
    for i in range(1,len(order)):
        if(order[i] == phi_p):
            proots.append(i)
    return proots
def phi(a):
    return a-1
def generate_keys(p,proots):
    e1=proots[randint(0,len(proots)-1)]
    d=randint(1,p-2)
    e2=ms(e1,d,p)
    public=(e1,e2,p)
    private=d
    return public,private
def encrypt(m,e1,e2,p,proots):
    r=proots[randint(0,len(proots)-1)]
    c1=ms(e1,r,p)
    c2=((e2**r)*m)%p
    return c1,c2,r
def decrypt(c1,c2,d,p):
    m= (c2*mi(c1**d,p))%p
    return m
def f1(e1,r,p,q):
    s1=((e1**r)%p)%q
    return s1
def f2(m,d,r,q,s1):
    s2=((m+d*s1)*mi(r,q))%q
    return s2
def f3(s1,s2,e1,e2,p,q,m):
    inv=mi(s2,p)
    t1=(((e1**(m*inv))*(e2**(s1*inv)))%p)%q
    t2=s1
    return t1,t2
if __name__ == "__main__":
    p=int(input("Enter large prime number p :"))
    q=int(input("Enter large prime number q :"))
    m=int(input("Enter Message:"))
    order=primitive_roots_order(p)
    proots=all_roots(order,p)
    public_key,d=generate_keys(p,proots)
    c1,c2,r=encrypt(m,public_key[0],public_key[1],public_key[2],proots)
    dec_msg=decrypt(c1,c2,d,p)
    s1=f1(public_key[0],r,p,q)
    s2=f2(m,d,r,q,s1)
    ans=f3(s1,s2,public_key[0],public_key[1],p,q,m)
    if ans is True:
        print("Accept")
    else:
        print("Reject")