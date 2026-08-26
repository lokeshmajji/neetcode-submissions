class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        sum = 0
        ni = []
        for i, num in enumerate(nums):
            ni.append([num, i])

        ni.sort()
            
        while left < right:
            sum = ni[left][0] + ni[right][0]
            print("sum", sum, "left:", left, "right", right)
            if sum == target:
                return sorted([ni[left][1], ni[right][1]])
            elif sum > target:
                right -= 1
            else:
                left += 1
        return []