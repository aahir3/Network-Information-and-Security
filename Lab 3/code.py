class Solution:
    def solve(self, n, a, b, c):
        print(findNthTerm(a, b, c, n))

def gcd(a, b): 
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  
def lcm(a, b): 
    return ((a * b) // gcd(a, b)) 

def divTermCount(a, b, c, num): 
    return ((num // a) + (num // b) + (num // c) 
            - (num // lcm(a, b)) 
            - (num // lcm(b, c)) 
            - (num // lcm(a, c)) 
            + (num // lcm(a, lcm(b, c)))) 
  
def findNthTerm(a, b, c, n): 
    low = 1
    high = 10**9
    mid=0
    while (low < high): 
        mid = low + (high - low) // 2
        if (divTermCount(a, b, c, mid) < n): 
            low = mid + 1
  
        # If current term is greater than equal to 
        # n then high = mid     
        else: 
            high = mid 
    return low