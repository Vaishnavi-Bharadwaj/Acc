# From the array return the word that rhymes the most  with the given word. 
# Input: n=4, arr=['gender','blender','blunder','under'] str='thunder'
# output='under'
# to do this find the longest common suffix
# Also, if two words rhymes the most, then return the word with less char count
def longest_common_suffix(word1,word2):
    length=0
    i=len(word1)-1
    j=len(word2)-1
    while(i>=0 and j>=0 and word1[i]==word2[j]):
        length+=1
        i=i-1
        j=j-1
    return length

def find_best_rhyme(n,arr,str):
    longest_suffix_length=0
    best_word=''
    for word in arr:
        suffix_length=longest_common_suffix(word,str)
        if suffix_length>longest_suffix_length or (suffix_length==longest_suffix_length and len(word)<len(best_word)):
            longest_suffix_length=suffix_length
            best_word=word
    return best_word

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    str=input()
    print(find_best_rhyme(n,arr,str))

if __name__=='__main__':
    main()    
