class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # prev number to check the start of the sequence
        # add numbers to a set for easy lookup
        numSet = set(nums)
        res = 0
        streak = 0
        for num in nums:
            # check start of sequence, if it is start counting
            if (num-1) not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                res = max(res, length)
        return res

