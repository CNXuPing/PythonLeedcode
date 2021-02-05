class Solution:
	def avoidFlood(self, rains: List[int]) -> List[int]:
		l = len(rains)
		ans = [1 for i in range(l)]
		dict1 = {}
		list1 = []
		for i in range(l):
			temp = rains[i]
			if temp > 0:
				ans[i] = -1
				if temp not in dict1:
					dict1[temp] = i
				else:
					day = dict1[temp]
					dict1[temp] = i
					if list1:
						left = 0
						right = len(list1)-1
						while left < right:
							mid = left + (right-left)//2
							if day < list1[mid]:
								right = mid
							else:
								left = mid + 1
						if day < list1[left]:
							ans[list1[left]] = temp
							list1.remove(list1[left])
						else:
							return []   
					else:
						return [] 
			else:
				list1.append(i)
		return ans
#Greedy + binary search 