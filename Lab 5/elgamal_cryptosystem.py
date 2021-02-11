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
    return c1,c2
def decrypt(c1,c2,d,p):
    m= (c2*mi(c1,d))%p
    return m
if __name__ == "__main__":
    p=int(input("Enter large prime number:"))
    m=int(input("Enter Message:"))
    order = primitive_roots_order (p)
    proots = all_roots (order, p)
    public_key,private_key=generate_keys(p,proots)
    c1,c2=encrypt(m,public_key[0],public_key[1],public_key[2],proots)
    print("Encrypted messages:",c1,c2)
    dec_msg=decrypt(c1,c2,private_key,p)
    print("Decrypted message",dec_msg)