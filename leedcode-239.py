class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		window = []
		ans = []
		for i,value in enumerate(nums):
			#move window
			if i >= k and window[0] <= i - k:
				window.pop(0)
			while window and nums[window[-1]] <= value:
				window.pop()
			window.append(i)
			if i >= k - 1:
				ans.append(nims[window[0]])
		return ans
#Maximum heap 