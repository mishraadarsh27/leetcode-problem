class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        ans = []
        for _ in range(k):
            max_freq = 0
            max_key = 0
            for key in freq:
                if freq[key] > max_freq:
                    max_freq = freq[key]
                    max_key = key
            ans.append(max_key)
            del freq[max_key]
        return ans