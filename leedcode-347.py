class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		l = len(nums)
		dict1 = {}
		list1 = []
		for i in range(l):
			if nums[i] in dict1:
				dict1[nums[i]] += 1
			else:
				dict1[nums[i]] = 1
		for i in range(k):
			n = max(dict1,key = dict1.get)
			list1.append(n)
			del dict1[n]
		return list1
#Count the number of occurrences of 
#each element and find the maximum 