class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		n = len(heights)
		l,r = [0] * n, [n] * n
		list1 = list()
		for i in range(n):
			#When the stack is not empty and the top value 
			#of the stack is higher than the current height 
			while list1 and heights[list1[-1]] >= heights[i]:
				r[list1[-1]] = i
				list1.pop()
			if list1：
				#The top value of the stack is lower than 
				#the current height, record the index 
				l[i] = list1[-1]
			else:
				#No limit to the left of the current height 
				l[i] = -1
			list1.append(i)
		if n > 0:
			ans = max((r[i] - l[i] - 1) * heights[i] for i in range(n))
		else:
			ans = 0
		return ans
#Maximum heap 			