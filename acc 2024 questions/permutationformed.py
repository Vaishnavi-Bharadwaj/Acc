# you are given a string S and your task is to find and return the count of permutation formed by fixing the positions of the vowels present in the string
# Ensure the result is non negative
# if there are no consonants then return 0
# Eg input: s="abec", output=2
# input: s="ABC", output=2
# approcah: count the no. of consonants and find the factorial of its count
import re
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

def main():
    string=input()
    count=0
    pattern=re.compile(r'a|e|i|o|u')
    for i in range(len(string)):
        if not pattern.search(string[i]):
            count+=1
    print(fact(count))

if __name__=='__main__':
    main()
