class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []

        for i in reversed(num):
            k += i
            res.append(k % 10)
            k //= 10

        while k:
            res.append(k % 10)
            k //= 10

        return res[::-1]        