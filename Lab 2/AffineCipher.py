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
    return t1
def encrypt(msg,k1,k2):
    l=list(msg)
    l1=len(l)
    for i in range(l1):
        l[i]=chr(((ord(l[i])-97)*k1+k2)%26+97)
    return ("".join(l))
def decrypt(msg,k1,k2):
    l=list(msg)
    l1=len(l)
    inv = multiplicative_inverse(k1,n)
    for i in range(l1):
        l[i]=chr(((ord(l[i])-97-k2)*inv)%26+97)
    return ("".join(l))

k1, k2, n = list(map(int, input("key1 key2 numberOfCharacters : ").split()))
msg = input("Plain Text : ")
enc_msg=encrypt(msg,k1,k2)
print(enc_msg)
dec_msg=decrypt(enc_msg,k1,k2)
print(dec_msg)
