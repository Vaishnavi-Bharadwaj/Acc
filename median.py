# In the context of two sorted arrays, namely a[] and b[], with N and M elements, the objective is to devise an algorithm to determine the median of the combined array. Your task is to formulate a solution that efficiently computes the median, considering the total number of elements in both arrays. Develop an algorithm that accurately identifies the median of the merged sorted arrays, with N and M denoting the number of elements in the respective arrays.
# Example:
# Input: a[] = {-5, 3, 6, 12, 15}, b[] = {-12, -10, -6, -3, 4, 10}
# Output: The median is 3.
# Explanation: The merged array is: ar3[] = {-12, -10, -6, -5 , -3, 3, 4, 6, 10, 12, 15}.
# So the median of the merged array is 3

# Input: a[] = {2, 3, 5, 8}, b[] = {10, 12, 14, 16, 18, 20}
# Output: The median is 11.
# Explanation : The merged array is: ar3[] = {2, 3, 5, 8, 10, 12, 14, 16, 18, 20}
# If the number of the elements are even. So there are two middle elements.
# Take the average between the two: (10 + 12) / 2 = 11.

def main():
    a,b=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    result=list1+list2
    result.sort()
    if len(result)%2==0:
        middle_element1=result[int(len(result)/2)]
        middle_element2=result[int((len(result)/2)-1)]
        median=int((middle_element1+middle_element2)/2)
    else:
        median=result[int(len(result)/2)]
    print(median)

if __name__=='__main__':
    main()