# Task is find and return an integer value representing the maximum number of favorite songs(letters repeating in the substring) that she can get in a single playlist(substring)
# Eg: input: s="acdbaaca" k=3, output=2

def find_max_songs(str,k):
    #find all the distinct substrings of length k
    substrings_with_repeated_char=set()
    for i in range(len(str)-k): #Loop to get substrings of length k
        substring=str[i:i+k]
        if len(set(substring))<len(substring): # Check if any character is repeated in the substring
            substrings_with_repeated_char.add(substring)
    return len(substrings_with_repeated_char)

def main():
    str=input()
    k=int(input())
    print(find_max_songs(str,k))

if __name__=='__main__':
    main()