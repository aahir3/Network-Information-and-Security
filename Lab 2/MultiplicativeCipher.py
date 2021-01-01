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
def encrypt(msg,key):
    l=list(msg)
    l1=len(l)
    for i in range(l1):
        l[i]=chr(((ord(l[i])-97)*key)%26+97)
    return ("".join(l))
def decrypt(msg,key,n):
    l=list(msg)
    l1=len(l)
    gcd,inv = multiplicative_inverse(key,n)
    for i in range(l1):
        l[i]=chr(((ord(l[i])-97)*inv)%26+97)
    return ("".join(l))

key,n=input().split()
key=int(key)
n=int(n)
msg=input("Enter Plain Text:")
enc_msg=encrypt(msg,key)
print("Encrypted Message:"+enc_msg)
dec_msg=decrypt(enc_msg,key,n)
print("Decrypted Message:"+dec_msg)