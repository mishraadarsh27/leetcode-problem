class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        import heapq
        from sortedcontainers import SortedList

        free_servers = SortedList(range(k))  
        busy_servers = []  
        handled_requests = [0] * k  

        for i in range(len(arrival)):
            while busy_servers and busy_servers[0][0] <= arrival[i]:
                _, server_index = heapq.heappop(busy_servers)
                free_servers.add(server_index)
            server_index = i % k
            if server_index not in free_servers:
                idx = free_servers.bisect_right(server_index)  
                if idx == len(free_servers): 
                    if not free_servers:  
                        continue  
                    server_index = free_servers[0]  
                else:
                    server_index = free_servers[idx] 
            if server_index in free_servers:
                finish_time = arrival[i] + load[i]
                heapq.heappush(busy_servers, (finish_time, server_index))
                handled_requests[server_index] += 1
                free_servers.remove(server_index)
        max_requests = max(handled_requests)
        return [i for i in range(k) if handled_requests[i] == max_requests]