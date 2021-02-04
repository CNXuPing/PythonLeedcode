class Solution:
	def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
		graph = collections.defaultdict(list)
		# Create a dictionary-list to record path
		for u,v,w in times:
			graph[u].append((v,w))
			
		# Record the distance from point k to other points 
		dist1 = {i:float('inf') for i in range(1,N+1)}
		dist1[k] = 0
		
		# Record which point have been visited
		visited = (N+1) * [False]
		
		#
		while True:
			node = -1
			time = float('inf')
			for i in range(1,N+1):
				if not visited[i] and dist1[i] < time:
					time = dist1[i]
					node = i
			if node < 0:
				#All connected nodes are recorded 
				break
			else:
				#Record visited point and update the path
				visited[node] = True
				for v,w in graph[node]:
					dist1[v] = min(dist1[v],dist1[node] + w)
					
		ans = max(dist1.values())
		if ans < float('inf'):
			return ans
		else:
			return -1
#Find the shortest path to the furthest point