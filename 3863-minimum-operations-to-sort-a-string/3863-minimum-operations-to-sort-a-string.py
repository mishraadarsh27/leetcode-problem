class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mn = s[0]
        mx = s[0]
        sorted_string = True

        for i in range(1, n):
            if s[i] < s[i - 1]:
                sorted_string = False

            if s[i] < mn:
                mn = s[i]

            if s[i] > mx:
                mx = s[i]

        if sorted_string:
            return 0

        if n == 2:
            return -1

        if s[0] == mn or s[n - 1] == mx:
            return 1

        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        return 3