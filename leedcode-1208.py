lass Solution:
	def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
		list1 = []
		l = len(s)
		for i in range(l):
			list1.append(abs(ord(s[i]) - ord(t[i])))
			
		begin = 0
		end = 0
		cost = 0
		ans = 0
		for end in range(l):
			cost += list1[end]
			while cost > maxCost:
				cost -= list1[begin]
				begin += 1
			ans = max(ans,end - begin + 1)
		return ans
#Sliding window 
#finds the maximum length and the cumulative sum lower than maxCost 
			
			