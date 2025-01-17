'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: s = "racecar", t = "carrace"    Output: true
Input: s = "jar", t = "jam"            Output: false

'''

# Brute Force Method 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
# Time complexity = O(n+m)
# Space complexity = O(1) or O(n+m) depending in the sorting algorithm 

    

# HashMap solution (Dictionary)

class Solution2:
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i],0) + 1
            t_count[t[i]] = t_count.get(t[i],0) + 1

        return s_count == t_count
    
solution2 = Solution2()
solution2.isAnagram("racecar", "carrace")

# Time complexity = O(n+m)
# Space complexity = O(1) as we have atmost 26 different characters


# Hashmap (optimal)

class Solution3:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i])-ord('a')] += 1
            counter[ord(t[i])-ord('a')] -= 1

        for val in counter:
            if val != 0:
                return False
        return True
            
solution3 = Solution3()
print(solution3.isAnagram("racecar", "carrace"))
