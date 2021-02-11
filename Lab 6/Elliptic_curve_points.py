import math
def Elliptic_curve_points(a,b,p):
    x=0
    points=[]
    while(x < p):
        w=(x**3+a*x+b)%p
        result=w**((p-1)//2) % p
        if(w == 0):
            points.append((x,0))
        if(result == 1):
            root = math.sqrt(w)
            while math.ceil(root) != root:
                w+=p
                root = math.sqrt(w)
            points.append((x,int(root%p)))
            points.append((x,int((-root)%p)))
        if(result == -1):
            print("No solution")
            break
        x+=1
    return points


if __name__ == "__main__":
    a,b,p=list(map(int,input().split()))
    print(Elliptic_curve_points(a,b,p))