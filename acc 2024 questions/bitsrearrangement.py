# Given a positive number N, you have to rearrange the bits of the number in its binary representation such that all set bits are in 
# consecutive order. Your task is to find and return an integer value representing the minimum possible number that can be formed after
# rearranging the bits of the number N

def main():
    n=int(input())
    count=0
    while n: #until n is not zero
        count+=n&1
        n>>=1
    ans=(2**count)-1
    print(ans)

if __name__=='__main__':
    main()