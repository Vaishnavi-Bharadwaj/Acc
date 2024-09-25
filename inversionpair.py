# Count the number of Inversion pairs (if j and k are two indices, if j<k and a[j]>a[k] thenv(j,k) is called an inversion pair)
# Eg: input: n=5 a=[1,20,6,4,5]
# output: 5
def main():
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                count+=1
    print(count)

if __name__=='__main__':
    main()
