T=int(input())

while(T > 0):
    n=int(input())
    string="abcdefghijklmnop"
    encoded_string=input()
    if (len(encoded_string) == 4):
        s=""
        for _ in range(len(encoded_string)):
            if(int(encoded_string[_]) == 0):
                l=len(string)//2
                s=string[0:l]
                string=string[0:l]
            else:
                l=len(string)//2
                s=string[l:]
                string=string[l:]
        print(s,"In if")
    else:
        devided_l=len(encoded_string)//4
        l1=[]
        for _ in range(devided_l):
            string="abcdefghijklmnop"
            for _ in range(len(encoded_string)):
                if(int(encoded_string[_]) == 0):
                    l=len(string)//2
                    s=string[0:l]
                    string=string[0:l]
                else:
                    l=len(string)//2
                    s=string[l:]
                    string=string[l:]
            l1.append(s)
    print("".join(l1))
    T-=1
    