class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        su=ml=0
        j=0
        for i in range(len(s)):
            su+=abs(ord(s[i])-ord(t[i]))
            while j<=i and su>maxCost:
                su-=abs(ord(s[j])-ord(t[j]))
                j+=1
            ml=max(ml,i-j+1)
        return ml

        