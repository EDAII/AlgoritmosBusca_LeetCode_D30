import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, height, 0))

        events.sort()

        skyline = [[0, 0]]
        active_heights = [(0, float('inf'))]

        for x, height, right in events:
            # Removendo edifícios do heap que já terminaram
            while x >= active_heights[0][1]:
                heapq.heappop(active_heights)
            
            if height < 0:
                # Adicionando um novo edifício ao heap
                heapq.heappush(active_heights, (height, right))

            current_max_height = -active_heights[0][0]
            
            if skyline[-1][1] != current_max_height:
                skyline.append([x, current_max_height])
        
        return skyline[1:]