# You are given a number N. if N is odd, print the product of digits of the number else print sum of digits of the number
# Eg: input: 11, output=1
# input: 16, output=7

def sum_or_product(n):
    sum=0
    product=1
    if n%2==0:
        even_str=str(n)
        for i in range(0,len(even_str)):
            sum+=int(even_str[i])
        return sum
    else:
        odd_str=str(n)
        for i in range(0,len(odd_str)):
            product*=int(odd_str[i])
        return product
    
def main():
    n=int(input())
    print(sum_or_product(n))

if __name__=='__main__':
    main()
    

