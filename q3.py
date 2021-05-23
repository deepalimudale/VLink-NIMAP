import math
def isPrime(n):
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
            
    return True

n = int(input())
l = []
if n > 9:
    if not isPrime(n):
        c = 0
        for i in range(3, n+1):
            if n%i == 0:
                while n%i ==0 :
                    n = n//i
                    c+=1
                l.append(i)
        print(l[::-1])
        
    else:
        print("Please input a different number")
else:
    print("Invalid number")
