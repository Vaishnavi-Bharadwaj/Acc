# Task is to return a string with labels even or odd in sequence according to which the numbers appear in the array
# input: N=5 a[]={1,2,3,4,5}

def even_or_odd(n,a):
    ans=""
    for i in range(n):
        if a[i]%2==0:
            ans+="even"
        else:
            ans+="odd"
    return ans

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    print(even_or_odd(n,arr))

if __name__=='__main__':
    main()


