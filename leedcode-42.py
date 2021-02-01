class Solution:
	def trap(self, height: List[int]) -> int:
		v,l,r = 0,0,0
		for i in range(len(height)):
			l = max(l,height[i])
			r = max(r,height[~i])
			v = v + l + r -height[i]
		return  v - len(height)*l
#Ingenious method, easy to understand combined with images 