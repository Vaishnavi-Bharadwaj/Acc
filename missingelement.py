# Consider an array of size N-1 containing distinct integers in the range of 1 to N. Your task is to find the missing element in the array.
# Write a function or algorithm to efficiently solve this problem.
# Example:
# Input:
# Array: [1, 2, 4, 6, 3, 7, 8]
# Output:
# Missing Element: 5
# Explanation:
# The missing element in the array is 5.

def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    j=1
    for i in a:
        if i==j:
            j+=1
        else:
            break
    print(j)

if __name__=='__main__':
    main()
        
            