# print 
# 1
# 1 2
# 1 2 3
# 1 2 3 4

def main():
    n=int(input())
    for i in range(1,n+1): 
        for j in range(1,i+1):
            print(j ,end=' ')
        print()
if __name__=='__main__':
    main()