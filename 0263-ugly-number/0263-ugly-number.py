class Solution:
    def isUgly(self, n: int) -> bool:
        F = [2,3,5]
        x = 0

        while n > 1 and x < len(F):
            d = F[x]
            if n % d == 0:
                n //= d
            else:
                x += 1
                
        return True if n == 1 else False