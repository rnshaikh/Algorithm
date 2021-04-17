
"""
    union of two sorted array
    method1:
        a.union(b)
    method2:
        i, j = 0
        travese array a and b
        if a[i]<b[j]: push in result array and increment i by 1
        if a[i]>b[j]: push in result array inde increment j by 1
        if both equal push 1 in result increment i and j by 1

        tramvers remeaining element in a
        traverse remaining element in b
"""

def mergeArrays(self,a,b,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    # code here
    # res = set(a).union(set(b))
    # res = list(res)
    # res.sort()
    # return res
    i, j=0, 0
    result = []
    while(i<n and j<m):
        if a[i] == b[j]:
            result.append(a[i])
            i = i+1
            j = j+1

        elif a[i] < b[j]:
            result.append(a[i])
            i = i+1

        elif a[i] > b[j]:
            result.append(b[j])
            j = j+1


    while i < n :
        if a[i] != a[i-1]:
            result.append(a[i])
            i = i+1

    while j < m:
        if b[j] != b[j-1]:
            result.append(b[j])
            j = j + 1
    return result
