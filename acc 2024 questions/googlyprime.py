# Googly prime number
# For eg: if n=43, the sum of its digits is 4+3=7 which is prime, therefore it is a googly prime number
#input=43
#output=yes
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
    string=str(n)
    sum=0
    for i in range(len(string)):
        sum+=int(string[i])
    if is_prime(sum):
        print("yes")
    else:
        print("no")

if __name__=='__main__':
    main()