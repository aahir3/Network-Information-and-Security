def encrypt(msg):
    cipher=[]
    for char in msg:
        cipher.append(map_list2[map_list1.index(char)])
    return "".join(cipher)
def decrypt(msg):
    plain=[]
    for char in msg:
        plain.append(map_list1[map_list2.index(char)])
    return "".join(plain)

map_list1=['a','b','c','d',' ','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','e']
map_list2=['c','e','f','j','k','l','n','o','s','p','w','z','y','x','a','d','g','h','i','b','m','r','q','t','u','v',' ']
msg=input("Enter text: ")
enc_msg=encrypt(msg)
print("Encrypted text: "+enc_msg)
dec_msg=decrypt(enc_msg)
print("Decrypted text: "+dec_msg)

