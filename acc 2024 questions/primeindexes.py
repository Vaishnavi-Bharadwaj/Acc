# Find the sum of values present in the prime indexes of an array
# Eg: input: n=10, arr[]={10,20,30,40,50,60,70,80,90,100}
#output= 30+40+60+80=210
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
    a=list(map(int,input().split()))
    sum=0
    for i in range(n):
        if is_prime(i):
            sum+=a[i]
    print(sum)

if __name__=='__main__':
    main()
