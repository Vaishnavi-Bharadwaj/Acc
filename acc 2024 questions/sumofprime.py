# Find the sum of all prime numbers till N
# Eg input: N=8, output=17(2+3+5+7)
import math
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def main():
    n=int(input())
    sum=0
    for i in range(n+1):
        if is_prime(i):
            sum+=i
    print(sum)

if __name__=='__main__':
    main()
