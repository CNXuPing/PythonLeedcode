class Solution:
	def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
		graph = collections.defaultdict(list)
		#Build list-dictionary and storage graph
		for u,v in edges:
			graph[u].append(v)
			graph[v].append(u)
		if n == 1:
			return [0]
		#deque-heap
		#from the leaf nodes to root node
		queue = collections.deque()
		for u,v in graph.items()
			if len(v) == 1:
				queue.append(u)
		#Delete the old point and 
		#add the new point with an in-degree of 1 
		while n > 2:
			n = n - len(queue)
			for i in range(len(queue)):
				u = queue.popleft()
				for j in graph[u]:
					graph[j].remove(u)
					if len(graph[j]) == 1:
						queue.append(j)
		return list(queue)
		