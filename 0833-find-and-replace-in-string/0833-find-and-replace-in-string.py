class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        d,j,res = dict(),0,''
        for k in range(len(s)):
            d[k] = s[k]    
        for i in range(len(indices)):
            if s[indices[i]:].startswith(sources[i]):
                d[indices[i]] = targets[i]
                if len(sources[i])>1:
                    for g in range(indices[i]+1,indices[i]+len(sources[i])):
                        d[g] = ''
        for l in d.values():
            res += l
        return res
        