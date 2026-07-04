class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        arr = {}
        for i in range(len(widths)):
            arr[chr(i +97)] = widths[i]
        count = 1
        store = 0
        for i in s:
            if store + arr[i] > 100:
                store = arr[i]
                count += 1
            else:
                store += arr[i]
        return [count,store]

        