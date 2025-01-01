class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)  # Number of cities
        visited = [False] * n  # To track if a city has been visited

        # Helper function to perform DFS and mark connected cities as visited
        def dfs(city: int):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:  # Check for direct connection
                    visited[neighbor] = True  # Mark the neighbor city as visited
                    dfs(neighbor)  # Recursively visit all the connected cities

        provinces = 0  # Count of provinces

        # Iterate through each city
        for city in range(n):
            if not visited[city]:  # If the city is unvisited
                visited[city] = True  # Mark the current city as visited
                dfs(city)  # Perform DFS to mark all cities connected to the current city
                provinces += 1  # Increment province count

        # Return the total number of provinces
        return provinces

# Uncomment the following line to test the function
# print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Expected output: 2
