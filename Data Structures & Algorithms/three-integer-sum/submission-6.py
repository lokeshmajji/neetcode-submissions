class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        nums.sort()
        i = 0
        res = []
        while i < len(nums)  - 2:
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            # print("target:", target, "l:", l, "r:", r)
            while l < r:
                two_sum = nums[l] + nums[r]
                # print("two_sum:", two_sum, "nums[l]:", nums[l], "nums[r]:", nums[r])
                if two_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    # while l < r  and nums[r] == nums[r + 1]:
                    #     r -= 1
                elif two_sum > target:
                    r -= 1
                else:
                    l += 1
            i += 1
        return res

