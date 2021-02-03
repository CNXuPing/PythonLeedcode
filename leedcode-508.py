class Solution:
	def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
		import collections
		dict1 = collections.defaultdict(int)
		if not root:
			return []
		
		def dfs(root):
			if not root:
				return 0
			num = root.val + dfs(root.left) + dfs(root.right)
			dict1[num] += 1
			return num
		
		dfs(root)
		maxnum = None
		result = []
		for i,v in sorted(dict1.items(),key = lambda x:x[1],reverse = True):
			if maxnum is None:
				maxnum = v
			if v == maxnum:
				result.append(i)
			else:
				break
		return result
		
	#Record the sum of the elements of each subtree, 
	#and then sort from largest to smallest 