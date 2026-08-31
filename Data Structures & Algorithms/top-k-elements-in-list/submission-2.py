class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hs = defaultdict()
        for num in nums:
            hs[num] = hs.get(num, 0) + 1
        
        freq_list = []
        for num, freq in hs.items():
            freq_list.append([freq, num])

        freq_list.sort()
        # print(freq_list)

        i = 0
        while i < k:
            res.append(freq_list.pop()[1])
            i += 1
        return res