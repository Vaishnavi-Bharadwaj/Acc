# You have the distance D from the tree's trunk to the edge of the shadow.Your task is to calculate and return an integer value representing the shadow area of the canopy
# round off the result to the nearest integer
#input: an integer D (5)
# output: int value representing the shadow area (78)

def main():
    d=int(input())
    area=3.14*d*d
    print(int(area))

if __name__=='__main__':
    main()