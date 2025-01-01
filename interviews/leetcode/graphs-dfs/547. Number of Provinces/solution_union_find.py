class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)  # Number of cities

        # Parent array to track the root of each city
        parent = list(range(n))
        # Rank array to keep tree flat (optional, but improves performance)
        rank = [1] * n

        # Find operation with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Union operation with union by rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1  # Increase rank if both roots are the same

        # Union cities that are directly connected
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        # Count the number of provinces by counting unique roots
        provinces = 0
        for i in range(n):
            if find(i) == i:  # Each root represents a province
                provinces += 1

        return provinces

# Uncomment the following line to test the function
# print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Expected output: 2
