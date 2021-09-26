







# def fibonacci(num):
#     a,b = 0, 1

#     lis = []
#     lis.append(a)
#     lis.append(b)

#     for i in range(2, num):
#         temp = a+b
#         a = b
#         b = temp
#         lis.append(temp)


#     return lis


def recursive(num):

    if num == 1:
        return num
    elif num == 0:
        return num
    else:
        return recursive(num-1) + recursive(num-2)


for i in range(9):
    print(recursive(i))



