



def max_product_card_sum(array):


    i = 0
    j = len(array)-1

    max_prod = 0
    numbers = []

    while i < j:

        prod = array[i] * array[j]

        if prod > max_prod:
            max_prod = prod
            numbers.append(array[i])
            numbers.append(array[j])

        i = i+1
        j = j-1

    return numbers[0] + numbers[1]


if __name__ == '__main__':

    n  = int(input(""))
    nums = input("")
    nums = nums.split(" ")
    nums = list(map(int, nums))
    print(max_product_card_sum(nums))

