n=list(map(str,input()))
i=0
while i < len(n):
    n[i],n[i+1]=n[i+1],n[i]
    i+=2
print("".join(n))