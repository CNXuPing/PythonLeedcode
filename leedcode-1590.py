class Solution:
	def minSubarray(self, nums: List[int], p: int) -> int:
		l = len(nums)
		presum = 0
		for num in nums:
			presum += num
		if presum % p == 0:
			return 0      
		if presum < p:
			return -1 
		mod = presum % p
		dict1 = {}
		dict1[0] = -1
		ans = float('inf')
		presum = 0
		for i in range(l):
			presum = (presum + nums[i]) % p
			target = (presum - mod + p) % p
			if target in dict1:
				ans = min(ans,i - dict1[target])
			dict1[presum] = i
		return ans if ans < len(nums) else -1