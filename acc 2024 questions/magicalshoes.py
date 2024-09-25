# Alice can reach the roof of only those houses where the number is a multiple of 3. Your task is to find and return integer value representing the count of the number of houses whose roof Alice can climb
# Eg: input: n=4, a[]={12,16,21,20}, output=2
# input: n=1, a[]={6}, output=1

def multiple_of_three(n,a):
    count=0
    for i in range(0,n):
        if a[i]%3==0:
            count+=1
    return count

def main():
    n=int(input())
    a=list(map(int,input().split()))
    print(multiple_of_three(n,a))

if __name__=='__main__':
    main()