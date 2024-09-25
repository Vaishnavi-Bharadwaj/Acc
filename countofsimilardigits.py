#Compose a program to determine the count of matching digits at corresponding indices in two given numbers, denoted as N and M.
# Example:
# Input: N = 123, M = 321
# Output: 1
# Explanation: Digit 2 satisfies the condition

# Input: N = 123, M = 111
# Output: 1

def main():
    m=int(input())
    n=int(input())
    new_m=str(m)
    new_n=str(n)
    count=0
    for i in range(0,len(new_m)):
        if new_m[i]==new_n[i]:
            count+=1
    print(count)

if __name__=='__main__':
    main()