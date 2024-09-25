# Find the element at the mid index ignoring all the indices at which negative numbers are present in the array
# if there are 2 mid indices, return the element at the smaller index 
# Eg: input: n=6 a=[12,-3,14,-56,77,13], output= 14

def mid_positive_element(n,a):
    temp_arr=[]
    for i in range(0,n):
        if a[i]>=0:
            temp_arr.append(a[i])
    
    if len(temp_arr)%2==0:
        mid_index=(len(temp_arr)/2)-1
    else:
        mid_index=len(temp_arr)/2
    return temp_arr[int(mid_index)]

def main():
    n=int(input())
    a=list(map(int,input().split()))
    print(mid_positive_element(n,a))

if __name__=='__main__':
    main()
