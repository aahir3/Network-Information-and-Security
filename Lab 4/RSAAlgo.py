from random import randint
from ExtendedEuclidian import multiplicative_inverse as mi
from MultiplyAndSquare import multiply_and_square
def phi(a):
    return a-1
def encryption(m,e,n):
    return multiply_and_square(m,e,n)
def decryption(c,d,n):
    return multiply_and_square(c,d,n)
def generate_keys(p,q):
    e=randint(2,(phi(p)*phi(q))-1)
    gcd,_=mi(e,phi(p)*phi(q))
    while(gcd != 1):
        e=randint(2,(phi(p)*phi(q))-1)
        gcd,_=mi(e,phi(p)*phi(q))
    _,d=mi(e,phi(p)*phi(q))
    public=(e,p*q)
    private=(d,p*q)
    return public,private
if __name__ == "__main__":
    p,q=list(map(int,input("Enter p q : ").split()))
    if(p == q):
        q=input("p and q can't be same so again Enter q : ")
    public,private=generate_keys(p,q)
    encrypted_txt=encryption(int(input("Enter plain text : ")),public[0],public[1])
    print("Encrypted text : "+str(encrypted_txt))
    decrypted_txt=decryption(encrypted_txt,private[0],private[1])
    print("Decrypted text : "+str(decrypted_txt))