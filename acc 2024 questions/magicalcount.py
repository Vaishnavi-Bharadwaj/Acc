# Find the count of magical numbers from 1 to N, given N
# A number is magical if:
# convert to binary
# replace 0 with 1 and 1 with 2 in binary string
# calculate sum of all digits in binary string
# resultant must be an odd number
# Eg input: n=5, output=2

def count_magical_nums(n):
    count=0
    for num in range(1,n+1):
        breakpoint()
        bin_num=bin(num)
        bin_str=str(bin_num[2:])
        # while replacing 0 with 1 and 1 with 2, first replace 0 with a temp var x
        bin_str=bin_str.replace('0','x')
        bin_str=bin_str.replace('1','2')
        bin_str=bin_str.replace('x','1')
        sum=0
        for i in range(len(bin_str)):
            sum+=int(bin_str[i])
        if sum%2!=0:
            count+=1
    return count

def main():
    n=int(input())
    print(count_magical_nums(n))

if __name__=='__main__':
    main()