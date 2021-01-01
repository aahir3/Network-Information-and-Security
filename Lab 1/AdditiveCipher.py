def encrypt(msg,key):
    l=list(msg)
    l1=len(l)
    for i in range(l1):
        l[i]=chr((ord(l[i])-97+key)%26+97)
    return ("".join(l))
def decrypt(msg,key):
    l=list(msg)
    l1=len(l)
    for i in range(l1):
        l[i]=chr((ord(l[i])-97-key)%26+97)
    return ("".join(l))
def cryptanalysis(enc_msg):
    l=list(enc_msg)
    l1=len(l)
    for k in range(0,26):
        for i in range(l1):
            l[i]=chr((ord(l[i])-97-k)%26+97)
        print("".join(l))
        l=list(enc_msg)
    return 0 

m,key=input().split()
key=int(key)
enc_msg=encrypt(m,key)
print("Encrypted Message:"+enc_msg)
dec_msg=decrypt(enc_msg,key)
print("Decrypted Message:"+dec_msg)
print("Cryptanalysis:")
final_key=cryptanalysis(enc_msg)
