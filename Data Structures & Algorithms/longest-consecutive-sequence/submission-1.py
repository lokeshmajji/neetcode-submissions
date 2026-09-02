class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # prev number to check the start of the sequence
        # add numbers to a set for easy lookup
        # no need to sort, since we increment the numbers to form a sequence and use the set for lookup
        numSet = set(nums)
        res = 0
        streak = 0
        # this loop goes through numbers in the list 
        for num in nums:
            # check start of sequence, if it is start counting
            if (num-1) not in numSet:
                length = 0
                # this loop increments by 1 to check if the sequence exists and not by looping the nums array
                while num + length in numSet:
                    length += 1
                res = max(res, length)
        return res

