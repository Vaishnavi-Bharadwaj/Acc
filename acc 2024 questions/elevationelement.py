# Easy
# Eg input: n=7, arr=[1,2,3,4,3,2,1]
# output: 4 (elevation element)

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    elevated_element=0
    if n==0:
        elevated_element=-1
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            elevated_element=arr[i]
            break
    print(elevated_element)

if __name__=='__main__':
    main()

