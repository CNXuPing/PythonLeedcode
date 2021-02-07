class Solution:
	def checkPossibility(self, nums: List[int]) -> bool:
		l = len(nums)
		n = 0
		start = 0
		end = 0
		for i in range(1,l):
			a = nums[i-1]
			b = nums[i]
			start = nums[i-2] if i - 2 >= 0 else 0
			end = nums[i+1] if i + 1 < l else float('inf')
			if a > b:
				n += 1
				if b >= start:
					nums[i-1] = start
				elif a <= end:
					nums[i] = a
				else:
					return False
			if n >= 2:
				return False
		return True