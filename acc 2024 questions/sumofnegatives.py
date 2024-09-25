# Find the sum of negative integers
# input: A single line containing 4 integers a,b,c,d
# output: sum of negative numbers
# Eg: input: 2 -3 -14 7, output:-17

def sum(a,b,c,d):
    sum=0
    if a<0:
        sum+=a
    if b<0:
        sum+=b
    if c<0:
        sum+=c
    if d<0:
        sum+=d
    return sum

def main():
    a,b,c,d=map(int,input().split())
    print(sum(a,b,c,d))

if __name__=='__main__':
    main()