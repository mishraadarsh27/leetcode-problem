class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        even_pos = []
        odd_pos = []
        n = len(str(num))
        ans = [0] * n
        for c, i in enumerate(str(num)):
            x = int(i)
            if x % 2 == 0:
                even.append(x)
                even_pos.append(c)
            else:
                odd.append(x)
                odd_pos.append(c)
        even.sort(reverse=True)
        odd.sort(reverse=True)
        for i,j in zip(even_pos, even):
            ans[i] = j
        for i,j in zip(odd_pos, odd):
            ans[i] = j
        s = 0
        c = 10**len(ans)
        for i in ans:
            c //= 10
            s += i*c
        return s