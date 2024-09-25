# Easy
# Find and return an integer value representing the total number of days where the stock market price decreased indicating negative growth
# Eg: input: N=6 A[]={2,3,1,4,5,2}, output=2
# input: N=1 A[]={0}, output=0

def negative_growth(n,a):
    count=0
    if n==1:
        return 0
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            count+=1
    return count

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    print(negative_growth(n,arr))

if __name__=='__main__':
    main()
