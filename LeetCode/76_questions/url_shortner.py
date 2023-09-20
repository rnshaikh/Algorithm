import random 

class Solution:
	def idToShortURL(self,n):
		# code here
		
        code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        ans = ""
        while n:
            rem = n % 62
            ans = code[rem] + ans
            n = n // 62

		return ans

