class MyCalendar:

    def __init__(self):
        self.srt_list = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.srt_list:
            self.srt_list.add((startTime, endTime))
            return True
        
        idx = bisect.bisect(self.srt_list, (startTime, endTime))
        if idx > 0:
            s, e = self.srt_list[idx - 1]
            if startTime < e:
                return False
        
        if idx < len(self.srt_list):
            s, e = self.srt_list[idx]
            if s < endTime:
                return False

        self.srt_list.add((startTime, endTime))
        
        return True