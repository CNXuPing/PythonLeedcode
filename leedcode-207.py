class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		edges = collections.defaultdict(list):
		index = [0] * numCourses
		for i in prerequisites:
			edges[i[1]].append([0])
			index[i[0]] += 1
		queue = collections.deque([i for i in range(numCourses) if index[i] == 0])
		visited = 0
		while queue:
			visited += 1
			j = queue.popleft()
			for i in edges[j]:
				index[i] -= 1
				if index[i] == 0:
					queue.append(i)
		return visited == numCourses
#First record the number of parent nodes of each node, 
#and then record the child nodes of each node, 
#and use list-dictionary storage 

#Through the deque, continue to join the nodes without (other) parent nodes, 
#and visit their child nodes in order 