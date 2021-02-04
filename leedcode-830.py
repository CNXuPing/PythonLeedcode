class Solution:
	def largeGroupPositions(self, s: str) -> List[List[int]]:
		list1 = []
		num = 1
		l = len(s)
		for i in range(1,l):
			if s[i] != s[i-1]:
				if num >= 3:
					list1.append([i-num,i-1])
				num = 1
			else:
				num += 1
		if num >= 3:
			list1.append([l-num,l-1])
		return list1