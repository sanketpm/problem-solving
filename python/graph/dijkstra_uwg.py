class Solution:
    def dijkstra(self, src, n, adjList):
        dist = [float('inf')] * n

        dist[src] = 0

        pq = [[0, 0]]
        

        return 0


    def shortestPath(self, n, m, edges):
        adjList = {}

        for i in range(n):
            adjList[i] = []
        
        for u,v,d in edges:
            adjList[u].append([v, d]) 
            adjList[v].append([u, d]) 

        for i in range(n):
            print(adjList[i])

        dist = self.dijkstra(0, n, adjList)
        return 0

n = 6 
m = 7
edges = [
[0, 1, 2],
[0, 4, 1],
[4, 5, 4],
[4, 2, 2],
[1, 2, 3],
[2, 3, 6],
[5, 3, 1]]

print(edges)

res = Solution().shortestPath(n, m, edges)
print(res)

# arr = [float('inf')] * n
# print(arr)