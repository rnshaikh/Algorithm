






def add_non_prime_number(num):

    sum_num = 0
    num = str(num)

    for i in num:

        if int(i) == 0:
            continue
        elif int(i) == 1:
            continue
        elif int(i) % 2  != 0:
            continue
        else:
            sum_num = sum_num + int(i)

    return sum_num




print(add_non_prime_number(45673))
