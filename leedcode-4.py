class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		def median(k):
			i,j = 0
			if i == m:
				return nums2[j + k - 1]
			if j == n:
				return nums1[i + k - 1]
			if k ==1:
				return min(nums1[i],nums2[i])
			n1 = min(i + k // 2 - 1, m - 1)
			n2 = min(j + k // 2 -1 , n - 1)
			p1 = nums1[n1]
			p2 = nums2[n2]
			if p1 <= p2:
				k = k - (n1 - i + 1)
				i = n1 +1
			else:
				k = k - (n2 - j + 1)
				j = n2 + 1
		m,n = len(nums1),len(nums2)
		if (m + n) % 2 == 1:
			return median((m + n + 1) // 2)
		else:
			return (median((m + n) // 2) + median((m + n) // 2 + 1) / 2
#find the kth-smallest number
#Binary search 
#Keep updating the values of i, j, k 
#until one of the arrays is accessed or k is equal to 1, 
#and the answer is obtained at this time
