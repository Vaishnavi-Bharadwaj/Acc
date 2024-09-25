# You are provided with a string that has a sequence of 1s and 0s. The sequence is the encoded version of a english word. You are supposed to write a program to decode the provided string and find the english word.
# Each uppercase alphabet is representing by a sequence of 1s
# Also, two alphabets are separated by a 0
# Eg: input: s='10111011', output='ACB' (here 1->A, 11->B, 111->C and so on)

def solve(s):
    count=0
    ans=''
    for i in range(len(s)):
        if s[i]=='1':
            count+=1
        else:
            ans+=chr(ord('A')+(count-1))
            count=0
    ans+=chr(ord('A')+(count-1))
    return ans

def main():
    string=input()
    print(solve(string))

if __name__=='__main__':
    main()