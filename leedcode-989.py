class Solution:
	def addToArrayForm(self, A: List[int], K: int) -> List[int]:
		n = len(A)
		i = 0
		c = 0
		num = 0
		ans = []
		while i < n or K > 0:
			if i >= n:
				num = 0
			else:
				num = A[n-i-1]
			if num + K % 10 + c >= 10:
				ans.insert(0,(num + K % 10 + c) % 10)
				c = 1
			else:
				ans.insert(0,num + K % 10 + c)
				c = 0
			if K >= 10:
				K = K // 10
			else:
				K = 0
			i += 1
		if c == 1:
			ans.insert(0,1)
		return ans
#num : record the lowest carry value in A
#C : record the carry
#ans : store the carry answer in turn