"""
    Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

    Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.

"""


"""
 We have discussed a queue based solution. Both solutions (discussed in previous and this posts) are based on the fact that a number is divisible by 3 if and only if sum of digits of the number is divisible by 3.
For example, let us consider 555, it is divisible by 3 because sum of digits is 5 + 5 + 5 = 15, which is divisible by 3. If a sum of digits is not divisible by 3 then the remainder should be either 1 or 2.
If we get remainder either ‘1’ or ‘2’, we have to remove maximum two digits to make a number that is divisible by 3:


If remainder is ‘1’ : We have to remove single digit that have remainder ‘1’ or we have to remove two digit that have remainder ‘2’ ( 2 + 2 => 4 % 3 => ‘1’)
If remainder is ‘2’ : .We have to remove single digit that have remainder ‘2’ or we have to remove two digit that have remainder ‘1’ ( 1 + 1 => 2 % 3 => 2 ).

"""



MAX_SIZE = 10

class Solution:

    def sortArray(self, arr):

        count = [0] * MAX_SIZE

        for i in range(len(arr)):
            count[arr[i]] = count[arr[i]]+1

        j = 0
        for i in range(MAX_SIZE):
            while count[i] > 0:
                arr[j] = i
                count[i] = count[i]-1
                j = j+1

        return arr

    def create_num_str(self, arr, l1=-1, l2=-1):

        print("arr, l1, l2", arr, l1, l2)
        str_num = ""
        for i in range(len(arr)-1, -1, -1):
            if i == l1:
                print("continue on ele", arr[i], i, l1)
                continue
            elif i == l2:
                continue
            else:
                str_num = str_num + str(arr[i])

        print("Ans str_num", str_num)
        if str_num != "":
            int_sum = int(str_num)
            str_num = str(int_sum)
        return str_num

    def largestMultipleOfThree(self, digits: List[int]) -> str:

        arr = self.sortArray(digits)
        sum_num = 0
        for i in arr:
            sum_num = sum_num+i

        if sum_num % 3 == 0:
            print("0 remainder")
            str_num = self.create_num_str(arr)
            return str_num

        remainder = sum_num % 3

        if remainder == 1:
            for i in range(len(arr)):
                if arr[i] % 3 == 1:
                    print("1 remainder with 1 index,", arr, i)
                    str_num = self.create_num_str(arr, i, -1)
                    return str_num

            rem_1, rem_2 = -1, -1
            for i in range(len(arr)):
                if arr[i]%3 == 2:
                    if rem_1 == -1:
                        rem_1 = i

                    else:
                        rem_2 = i
                        break

            if rem_1 != -1 and rem_2 != -1:
                str_num = self.create_num_str(arr, rem_1, rem_2)
                return str_num
            else:
                return ""

        if remainder == 2:

            for i in range(len(arr)):
                if arr[i] % 3 == 2:
                    print("2 remainder with 2 index,", arr, i)
                    str_num = self.create_num_str(arr, i, -1)
                    return str_num

            rem_1, rem_2 = -1, -1
            for i in range(len(arr)):
                if arr[i] % 3 == 1:
                    if rem_1 == -1:
                        rem_1 = i
                    else:
                        rem_2 = i
                        break

            if rem_1 != -1 and rem_2 != -1:
                str_num = self.create_num_str(arr, rem_1, rem_2)
                return str_num

            else:
                return ""
