class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        sett = set()
        for r in range(len(s)):
            # check if window is valid and remove from left until it is valid
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            res = max(res, (r - l) + 1 )
            sett.add(s[r])
        return res