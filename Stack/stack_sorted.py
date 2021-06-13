# your task is to complete this function
# function sort the stack such that top element is max
# funciton should return nothing
# s is a stack

"""
    element should sorted in descending order bc top start from 0 in array

    traverse array from 0 to len(a)-1
        traverse array fron i+1 to last:
            if a[i] < a[j]:
                swap both element
                a[i], a[j] = a[j], a[i]


"""



def sorted(s):
    # Code here

    for i in range(len(s)):
        for j in range(i+1, len(s)):

            if s[i]<s[j]:
                temp = s[j]
                s[j] = s[i]
                s[i] = temp


