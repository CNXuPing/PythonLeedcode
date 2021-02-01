class Solution:
	def twoSum(self,nums,target):
		dict1 = {}
		for i,num1 in enumerate(nums):
			num2 = target - num1
			if num2 in dict1:
				return [dict1[num2],i]
			dict1[num1] = i 
		return None

#Traverse this sequence, record the current value, 
#and then add tags and data to the dictionary 
#while looking for another value that meets the conditions in the dictionary 
