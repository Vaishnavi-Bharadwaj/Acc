# You are given an integer N and string S. Your task is to find and return new string which consists of the original string repeated N times
# input: N=3, string="ABC"
# output: "ABCABCABC"

def main():
    n=int(input())
    s=input()
    print(repeat_n_times(n,s))

def repeat_n_times(n,s):
    new_string=''
    for i in range(n):
        new_string+=s
    return new_string

if __name__=='__main__':
    main()
