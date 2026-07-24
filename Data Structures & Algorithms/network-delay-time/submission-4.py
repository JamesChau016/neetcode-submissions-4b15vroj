import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d={}
        for i in times:
            if not d.get(i[0]):
                d[i[0]]=[(i[1],i[2])]
            else:
                d[i[0]].append((i[1],i[2]))
        def dijkstra(graph,start):
            dist=[math.inf]*n
            dist[start-1]=0

            minHeap=[(0,start)]

            while minHeap:
                distance, node = heapq.heappop(minHeap)
                if distance>dist[node-1]:
                    continue
                
                for neighbor, x in d.get(node,[]):
                    s=distance + x

                    if s<dist[neighbor-1]:
                        dist[neighbor-1]=s
                        heapq.heappush(minHeap, (s,neighbor))
            
            time=max(dist)
            return time if time!=math.inf else -1
        
        return dijkstra(d,k)
            

        
