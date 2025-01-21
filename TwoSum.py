'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Input: nums = [3,4,5,6], target = 7

Output: [0,1]

'''

# Brute Force Method

class Solution:
    def twosum(self, nums : list[int], target : int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        return False
    
solution = Solution()
print(solution.twosum([3,4,5,6], 7))

# Time Complexity : O(n^2)
# Space complexity: O(1)


# Sorting method

class Solution2:
    def twosum(self, nums : list[int], target : int) -> list[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()
        i, j = 0, len(nums) -1
        while i<j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1],A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []

# Time Complexity : O(nlogn)
# Space complexity: O(n)

# Hash Map (Two Pass)

class Solution3:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i # {3:0, 4:1, 5:2, 6:3}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
solution3 = Solution3()
print(solution3.twosum([3,4,5,6], 7))


# Time Complexity O(n)
# Space Complexity O(n)


# Hash Map (one Pass)

class Solution4:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        indict = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in indict:
                return [indict[diff], i]
            indict[n] = i
solution4 = Solution4()
print(solution4.twosum([3,4,5,6], 7))

# Time Complexity O(n)
# Space Complexity O(n)


