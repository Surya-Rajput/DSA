'''
 Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

 Input: nums = [1, 2, 3, 3]  Output: true
 Input: nums = [1, 2, 3, 4]  Output: false

'''

# Brute Force 

nums = [1,2,3,3]
class Solution1:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False
    
# Time Complexity O(n^2)
# Space Complexity O(1)


# Sorting

class Solution2:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
# time complexity : O(n log n)
# Space complexity : O(1) or O(n) depending on sorting algorithm 


# Hashset

class Solution3:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# Time complexity O(n)
# Space complexity O(n)

# hashset length 

class Solution4:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
    
# Time complexity O(n)
# Space complexity O(n)
        
 


