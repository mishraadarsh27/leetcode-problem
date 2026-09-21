class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = {} 
        debug = defaultdict(list)     
        for i in freq.keys():
            x = i 
            if x == 1:
                ans[1] = nums.count(1)
                continue                
            j = 0 
            while True:
                tar = x**(2**j)
                if tar in freq:
                    if freq[tar] >= 2:
                        ans[i] = ans.get(i,0) + 2
                        debug[i].append(tar)                       
                    elif freq[tar] == 1:
                        ans[i] = ans.get(i,0) + 1
                        debug[i].append(tar)
                        break
                else:
                    break
                j += 1
        print(ans)
        print(debug)
        res = max(ans.values())
        return res if res%2!=0 else res-1