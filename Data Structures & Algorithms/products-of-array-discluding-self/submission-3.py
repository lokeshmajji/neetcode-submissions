class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ls = [1] * n
        l = 1
        for i in range(1, n):
            l = l * nums[i - 1]
            ls[i] = l
        r = 1
        # print(ls)
        for i in range(n - 2, -1, -1):
            r = r * nums[i + 1]
            ls[i ] = ls[i] * r
        # print(ls)

        return ls