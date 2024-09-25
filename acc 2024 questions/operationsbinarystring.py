# input: 1C0C1C1A0B1
# output: 1
# A denotes and AND operation, B denotes OR operation, C denotes XOR operation, scan the string from left to right and display the output

def main():
    string=input()
    result=0
    for i in range(len(string)):
        if string[i]=='A':
            result=int(string[i-1])&int(string[i+1])
        elif string[i]=='B':
            result=int(string[i-1])|int(string[i+1])
        elif string[i]=='C':
            result=int(string[i-1]) ^ int(string[i+1])
    print(result)

if __name__=='__main__':
    main()