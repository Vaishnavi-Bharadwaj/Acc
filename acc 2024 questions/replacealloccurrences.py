# Given a string and two characters ch1, ch2 as input, replace all occurrences of ch1 with ch2 and ch2 with ch1 in the input string
# input: s='shaurya', ch1='s', ch2='a'
# output='ahsurys'

def solve(s,ch1,ch2):
    result=''
    for i in range(0,len(s)):
        if s[i]==ch1:
            result+=ch2
        elif s[i]==ch2:
            result+=ch1
        else:
            result+=s[i]
    return result

def main():
    ch1=input()
    ch2=input()
    s=input()
    print(solve(s,ch1,ch2))

if __name__=='__main__':
    main()
    