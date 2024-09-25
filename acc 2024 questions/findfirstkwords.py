# Find first k words of a string
# Eg: input: str= "my name is abc def", k=3
# output= "my name is"

def find_k_words(k,str):
    list_of_words=str.split(' ')
    print(list_of_words)
    new_string=''
    for i in range(k):
        new_string+=list_of_words[i]+' '
    return new_string

def main():
    k=int(input())
    string=input()
    print(find_k_words(k,string))

if __name__=='__main__':
    main()