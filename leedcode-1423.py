class Solution:
	def maxScore(self, cardPoints: List[int], k: int) -> int:
		l = len(cardPoints)
		list1 = []
		ans = 0
		num = 0
		for i in range(-k,k):
			num += cardPoints[(l + i) % l]
			if i >= 0:
				num -= cardPoints[i + l - k]
			ans = max(ans,num)
			print(ans)
		return ans
#Find the maximum sum of consecutive subsequences 
#and contain the point[0] or point[l-1] 
		