class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        ans = [''] * n
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        def f(i, flag):
            if i == n:
                return flag
            st = 0
            if not flag:
                st = ord(target[i]) - ord('a')
            for j in range(st, 26):
                if freq[j] > 0:
                    temp = chr(j + ord('a'))                   
                    new_flag = flag or temp > target[i]
                    freq[j] -= 1
                    ans[i] = temp
                    if f(i + 1, new_flag):
                        return True
                    freq[j] += 1
            return False
        if f(0, False):
            return ''.join(ans)
        return ""