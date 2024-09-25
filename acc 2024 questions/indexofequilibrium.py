# Return the index of the equilibrium point where the sum of elements on the left of the index is equal to the sum of elements on the right of the index. If no equilibrium point exists return -1
# eg: input: n=7 arr[]={-7,1,5,2,-4,3,0}, output=3
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    if n<=2:
        return -1
    left_sum=0
    right_sum=0
    index=0
    for i in range(1,n-1):
        for j in range(i):
            left_sum+=arr[j]

        for k in range(i+1,n):
            right_sum+=arr[k]
        
        if left_sum==right_sum:
            index=i
            break
        else:
            left_sum=0
            right_sum=0
        
    print(index)

if __name__=='__main__':
    main()
