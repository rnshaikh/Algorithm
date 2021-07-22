


def reverse(st, n):

    stack = []

    for i in st:
        stack.append(i)

    st = ''
    for i in range(n):
        s = stack.pop(-1)
        st = st+s

    return st


