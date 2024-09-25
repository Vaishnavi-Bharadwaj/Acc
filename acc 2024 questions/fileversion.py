import re
def check_format_find_highest(str_arr,n):
    if n==0:
        return -1
    res_arr=[]
    pattern=re.compile(r'File_\d')
    for i in str_arr:
        if re.match(pattern,i):
            res_arr.append(i)
    if len(res_arr)<1:
        return -1
    nums_arr=[]
    for str in res_arr:
        num=str.split('_')
        nums_arr.append(int(num[-1]))
    nums_arr.sort()
    return nums_arr[len(nums_arr)-1]

def main():
    s=list(map(str, input().split()))
    n=int(input())
    print(check_format_find_highest(s,n))

if __name__=='__main__':
    main()