#217 - Contains Duplicate

class Solution(object):
	def contains_duplicate(self, nums):
		hashset = set()

		for n in nums:
			if n in hashset:
				return True
			hashset.add(n)
		return False
	
test = Solution()
print(test.contains_duplicate([1,2,3,4]))
print(test.contains_duplicate([1,2,3,4,4]))