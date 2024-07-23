# Given a string s, find the length of the longest substring without repeating
# characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        available = set()
        start, end, max_length = 0, 0 ,0
        n = len(s)
        if n <= 1:
            return n

        while end < n:
            if s[end] not in available:
                available.add(s[end])
                max_length = max(max_length, end - start + 1)
                end += 1
            else:
                available.remove(s[start])
                start += 1

            return max_length

s = " "
print(lengthOfLongestSubstring(s))
