class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = -1
        max2 = -1
        for  ch in str(n):
            digit = int(ch)
            if digit > max1:
                max2 = max1
                max1 = digit
            elif digit > max2:
                max2 = digit
        return max1 * max2
            