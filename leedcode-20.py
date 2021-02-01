class Solution:
	def isValid(self, s: str) -> bool:
		if len(s) % 2 == 1:
			return False
		list1 = list()
		leftparens = "([{"
		rightparens = ")]}"
		parens = {")":"(","]":"[","}":"{"}
		for i in s:
			if i in leftparens:
				list1.append(i)
			elif i in rightparens:
				if not list1:
					return false
				if parens[i] != list1[-1]:
					return False
				list1.pop()
		if not list1:
			return True
		return False
		
#Use the stack to handle 
#the left and right matching of parentheses 