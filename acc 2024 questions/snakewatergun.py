# Snake beats water, water beats gun and gun beats snake
# First round: moves played by A and B are stored as "snakewater"
# Second round: moves are stored as "snakewatergunsnake"
# There are total n rounds and your task is to find and return a value representing how many rounds A wins
# Eg: n=2, str='snakewatergunwater'

def solve(n,s):
    flag=True
    # a and b has to store the first letter of the words so that it is easier to count the times a wins
    a=''
    b=''
    word=''
    for i in range(0,len(s)):
        word+=s[i]
        if word=='snake':
            if flag:
                b+='s'
            else:
                a+='s'
            flag=not flag
            word=''
        elif word=='water':
            if flag:
                b+='w'
            else:
                a+='w'
            flag=not flag
            word=''
        elif word=='gun':
            if flag:
                b+='g'
            else:
                a+='g'
            flag=not flag
            word=''
    
    #count to check how many times a wins
    count=0
    for i in range(0,n):
        if (a[i]=='s' and b[i]=='w') or (a[i]=='w' and b[i]=='g') or (a[i]=='g' and b[i]=='s'):
            count+=1
    return count

def main():
    n=int(input())
    s=input()
    print(solve(n,s))

if __name__=='__main__':
    main()
 

