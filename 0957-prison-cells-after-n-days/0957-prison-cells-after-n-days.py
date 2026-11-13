class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        d = defaultdict(int)
        arr = []
        while True:
            tmp = [0]
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1] == 1 or cells[i-1] == cells[i+1] == 0:
                    tmp.append(1)
                else:
                    tmp.append(0)
            tmp.append(0)
            if tuple(tmp) in d:
                break
            else:
                d[tuple(tmp)] = len(d)+1
                if d[tuple(tmp)] == n:
                    return list(tmp)
                arr.append(tmp)
                cells = tmp[:]
        n %= len(d)
        return arr[n-1]
        