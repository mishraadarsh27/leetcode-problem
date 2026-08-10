import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @cache
        def dfs(stones):
            if stones == 0:
                return False 

            for i in range(int(math.sqrt(stones)),0,-1):
               if not dfs(stones - i*i):
                return True     

          
            return False

        return dfs(n) 

