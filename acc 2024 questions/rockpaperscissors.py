# Easy
# Your task is to find and return a string value representing the winning move for B
# Eg: input->rock, output->paper
# input->paper, output->scissors
# input->scissors, output->rock

def main():
    string=input()
    if string=='rock':
        print('paper')
    elif string=='paper':
        print('scissors')
    else:
        print('rock')

if __name__=='__main__':
    main()