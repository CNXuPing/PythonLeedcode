class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		def dfs(string):
			while graph[string]:
				nextstr = heapq.heappop(graph[string])
				dfs(nextstr)
			stack.append(string)
		
		#dictionary-list structure 
		graph = collections.defaultdict(list)
		for u,v in tickets:
			graph[u].append(v)
		#Make the list behave like a heap 
		for i in graph:
			heapq.heapify(graph[i])
			
		#Create stack
		stack = []
		dfs("JFK")
		stack.reverse() # stack[::-1]
		return stack
#Backtrack from the last node to the first node 
#and record the path, 
#then output in reverse order 