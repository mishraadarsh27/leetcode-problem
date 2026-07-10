class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        r = 0
        counter = Counter(stones)
        for j in jewels:
            if j in counter:
                r += counter[j]
        return r
        