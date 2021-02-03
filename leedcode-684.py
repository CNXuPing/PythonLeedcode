class Solution:
	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
		parent = list(range(len(edges) + 1))
		
		def find(index):
			if parent[index] != index:
				parent[index] = find(parent[index])
			return parnet[index]
		
		def union(index1,index2):
			parent[find(index1)] = find(index2)
			
		for node1,node2 in edges:
			if find(node1) != find(node2):
				union(node1,node2)
			else:
				return [node1,node2]
		
		return []
	
	#If the two points of an edge cannot find another connected path, the two points are merged, 
	#otherwise it means that there is a ring, and the edge is a redundant edge