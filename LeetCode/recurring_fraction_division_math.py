"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parenthese
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

"""


"""
    school math division

    take result string
    take qu_result string
    take dict for stoing rem as value and len(result) where it occur

    first calulate queotiot  que_ans = num // deno  append in qu_result

    calculate rem = num % deno

    while loop until rem != 0 and rem not in dic:
        append rem in dict with value len(result)
        rem = rem * 10 multiple rem by 10
        result_part = rem // den  calculate result
        result = result + result_part  append in result str
        rem = rem % deno  calculate new rem


    if result == 0 :
        result = result + qu_result result only consist qu_resul
    else:
        if rem == 0:
            result = result = qu_result +"."+result[:-1]
            there is recurring part
        else:
            else put recurring part in "()"
            result = qu_result +"." +result[:dic[rem]] + "("+result[dic[rem]:]+")"



"""






class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:


        result = ""
        qu_result = ""
        sign = True
        if ((numerator < 0) ^ (denominator < 0)):
            sign = False

        if (numerator == 0) or (denominator == 0):
            return result+"0"


        numerator = abs(numerator)
        denominator = abs(denominator)

        qu = numerator // denominator
        qu_result = qu_result + str(qu)
        rem = numerator % denominator

        dic = {}
        while(dic != 0 and rem not in dic):

            dic[rem] = len(result)
            rem = rem * 10
            result_part = rem // denominator
            result = result + str(result_part)
            rem = rem % denominator

        if int(result) == 0:
            result = qu_result
        else:
            if rem == 0:
                result = result = qu_result +"."+result[:-1]
            else:
                result = qu_result +"." +result[:dic[rem]] + "("+result[dic[rem]:]+")"

        if sign:
            return result
        else:
            return "-" + result



