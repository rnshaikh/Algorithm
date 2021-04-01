

#t cases

#size n, rotate d

#ele space separated

# method 1:
# stored first d element in temporary array
# stored remaining element in new array
# append two temp to new array


#method 2:
#  rotate elements of array by on for d times
# rotate left by 1: store first element in temp , store each i+1 into i then store oth element at n-1


def rotate_left(ele_list, n):

    first_ele = ele_list[0]

    for i in range(0, n-1):
        ele_list[i] = ele_list[i+1]

    ele_list[n-1] = first_ele
    return ele_list


def rotate(ele_list, d, n):
    # result = []
    # for i in range(d):
    #     rotate_left(ele_list,n)
    # print(*ele_list)

    temp_list = ele_list[:d]
    new_list = ele_list[d:n]
    ele_list= new_list + temp_list

    print(*ele_list)

if __name__== '__main__':

        t = int(input())
        while t>0:
            n, d = input().split()
            n = int(n)
            d = int(d)
            e = [int(x) for x in input().split()]
            rotate(e,d,n)
            t = t-1

