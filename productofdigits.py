# Given an integer N, the task is to check whether the product of digits at even and odd places of a number are equal. If they are equal, print Yes otherwise print No.
# Example:
# Input: N = 2841 
# Output: Yes 
# Product of digits at odd places = 2 * 4 = 8 
# Product of digits at even places = 8 * 1 = 8

def main():
    n = int(input())  # Input the number
    s = str(n)  # Convert the number to a string for easy indexing
    
    product_at_even = 1  # Initialize product for even positions
    product_at_odd = 1   # Initialize product for odd positions
    
    for i in range(len(s)):
        digit = int(s[i])
        # Positions are 1-based, so i+1 gives the actual position
        if i % 2 == 0:  # Even position
            product_at_even *= digit
        else:  # Odd position
            product_at_odd *= digit
    
    if product_at_even == product_at_odd:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()


