
import math





def permutation(st, left, right):

    if left == right :
        print(st)
    else:

        for i in range(left, right):
            st = swap(st, left, i)
            permutation(st, left+1, right)
            st = swap(st, left, i)


def swap(st, left, i):
    st = list(st)
    st[i], st[left] = st[left], st[i]
    st = "".join(st)
    return st


st = 'abcd'
left = 0
right = len(st)

permutation(st, left, right)

