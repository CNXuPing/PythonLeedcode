class Solution:
	def divide(self, dividend: int, divisor: int) -> int:
	
		if dividend == 0:
			return 0
		
		i = 0
		ans = 0
		sign = 1
		if (dividend > 0) != (divisor > 0):
			sign = -1
		dividend = abs(dividend)
		divisor = abs(divisor)
		
		while divisor << i <= dividend:
			i += 1

		for j in reversed(range(i)):
			if (divisor << j) <= dividend:
				dividend -= (divisor << j)
				ans += (1 << j)
				
		if sign == -1:
			ans = -ans
		
		return min(ans,(1 << 31) - 1)
#Bit Operation-Division 