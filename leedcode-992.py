class Solution:
	def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
		n = len(A)
		dict1 = {}
		dict2 = {}
		num1,num2 = 0,0
		left1,left2 = 0,0
		ans = 0
		for right, num in enumerate(A):
			if num not in dict1:
				dict1[num] = 0
				num1 += 1
			else:
				dict1[num] += 1
				
			if num not in dict2:
				dict2[num] = 0
				num2 += 1
			else:
				dict2[num] += 1
			
			while num1 > K:
				dict1[A[left1]] -= 1
				if dict1[A[left1]] == 0:
					num1 -= 1
				left1 += 1
				
			while num2 > K - 1:
				dict2[A[left2]] -= 1
				if dict2[A[left2]] == 0:
					num2 -= 1
				left2 += 1
			
			ans += left2 - left1
		
		return ans