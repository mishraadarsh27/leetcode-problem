class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = timeSeries[0] + duration - 1
        c = duration

        for i in range(1, len(timeSeries)):
            if timeSeries[i] <= res:
                c += duration - (res - timeSeries[i] + 1)
            else:
                c += duration
            res = timeSeries[i] + duration - 1
        return c
        