# Find the count of second largest element in the array:
# if the array contains same element, return 0
# the array has only consecutive elements (sorted order)
# Eg: input: n=5 a=[1,2,3,3,4,4], output=2
# input: n=4, a=[2,2,2,2], output=0

def count_second_largest(n,a):
    arr_set=set(a)
    if len(arr_set)==1:
        return 0
    arr_set_list=list(arr_set)
    second_largest=arr_set_list[len(arr_set_list)-1]
    count_dict={}
    for i in range(0,n):
        if a[i] in count_dict:
            count_dict[a[i]]+=1
        else:
            count_dict[a[i]]=1
    return count_dict[second_largest]

def main():
    n=int(input())
    a=list(map(int,input().split()))
    print(count_second_largest(n,a))

if __name__=='__main__':
    main()