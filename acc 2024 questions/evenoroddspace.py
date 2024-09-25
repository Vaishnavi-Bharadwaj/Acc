# Calculate spaces of two strings and return a string with whether their difference is odd or even with ":" and count
# Eg: input1: "abc bcd cda" input2: "abc bc", output= "Odd:1"
def diff_bw_spaces(s1,s2):
    s1_space_count=0
    s2_space_count=0
    for i in range(0,len(s1)):
        if s1[i]==' ':
            s1_space_count+=1
    for i in range(0,len(s2)):
        if s2[i]==' ':
            s2_space_count+=1
    return abs(s1_space_count-s2_space_count)

def main():
    s1=input()
    s2=input()
    diff=diff_bw_spaces(s1,s2)
    if diff%2==0:
        print(f"Even:{diff}")
    else:
        print(f"Odd:{diff}")

if __name__=='__main__':
    main()