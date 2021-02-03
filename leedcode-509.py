class Solution:
	def fib(self, n: int) -> int:
		if n < 2:
			return n
		num1,num2,num3 = 0,1,0
		for i in range(n):
			num3 = num1 + num2
			num1 = num2
			num2 = num3
		return num3
		
#sqrt5 = 5**0.5
#fibN = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
#return round(fibN / sqrt5)