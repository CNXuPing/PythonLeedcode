class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		dict1 = {}
		#Initialize the graph
		for (x,y),v in zip(equations,values):
			if x not in dict1:
				dict1[x] = {y:v}
			else:
				dict1[x][y] = values
			if y not in dict1:
				dict1[y] = {x:1/v}
			else:
				dict1[y][x] = 1/values
		
		def dfs(x,y):
			if x not in dict1:
				return -1
			if x == y:
				return 1
			for i in dict1[x].keys():
				if i == y:
					return dict1[x][y]
				else:
					if i not in num:
						num.add(i)
						v = dfs(i,y)
						if v != -1:
							return dict1[x][i] * v
			return -1
			
		ans = []
		for x,y in queries:
			num = set()
			ans.append(dfs(x,y))
		return ans
		
#Depth first search 