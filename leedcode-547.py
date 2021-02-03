class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		def dfs(i):
			for j in range(len(isConnected)):
				if isConnected[i][j] == 1 and j not in visited:
					visited.add(j)
					dfs(j)
		
		visited = set()
		num = 0
		for i in range(len(isConnected)):
			if i not in visited:
				dfs(i)
				num = num + 1
		
		return num
#Use depth first search,
#and add all connected nodes to the set at once 