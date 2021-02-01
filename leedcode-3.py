class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		l = len(s)
		set1 = set()
		num,k = 0,0
		for i in range(l):
			if i != 0:
				set1.remove(s[i-1])
			while k < l and s[k] not in set1:
				set1.add(s[k])
				k += 1
			num =  max(num,k-i)
		return num
		
#Create a collection that does not contain 
#repeated elements to record substrings
		