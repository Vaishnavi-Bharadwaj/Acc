# Tossing a coin multiple times: if you get a H you get 2 points, if you get a T you lose 1 point
# If you get 3 H in a row, the game ends
# Eg: input: s='HTHHTTHTHHHT', output: 10

def solve(s):
    score=0
    head_count=0 #to keep track of heads since 3H in a row should end the game
    for i in range(0,len(s)):
        if s[i]=='H':
            score+=2
            head_count+=1
        elif s[i]=='T':
            score=score-1
            head_count=0
        if head_count==3:
            break
    return score

def main():
    s=input()
    print(solve(s))

if __name__=='__main__':
    main()  

        