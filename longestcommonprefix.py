# Within a collection of strings, your task is to employ Binary Search to identify the longest common prefix. Devise a solution that efficiently determines the shared prefix among the given strings, utilizing the principles of Binary Search.
# Example:
# Input: strings = ["flower", "flow", "flight"]
# Output: Longest Common Prefix: 'fl'

def main():
    n=int(input())
    strings=list(map(str,input().split()))
    strings.sort()
    s1=strings[0]
    s2=strings[n-1]
    i=0
    while i<len(s1) and i<len(s2):
        if s1[i]==s2[i]:
            i+=1
        else:
            break
    print(s1[0:i])

if __name__=='__main__':
    main()

