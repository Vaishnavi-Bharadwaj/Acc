# Find the hypotenuse of the right angled triangle, given two integers A and B 
# where A represents a point on x-axis and B is a point on the y-axis
# if the result is a decimal, round it off to the next greater number
import math
def hypotenuse(a,b):
    hypotenuse=math.ceil(math.sqrt((a*a)+(b*b)))
    return hypotenuse

def main():
    a=int(input())
    b=int(input())
    print(hypotenuse(a,b))

if __name__=='__main__':
    main()