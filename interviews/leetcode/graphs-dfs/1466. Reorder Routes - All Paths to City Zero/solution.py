class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(n)]

        # Populate the graph with the connections
        for u, v in connections:
            # Add the edge u -> v with a flag 1 indicating this edge needs to be reordered
            graph[u].append([v, 1])
            # Add the edge v -> u with a flag 0 indicating no reordering is needed
            graph[v].append([u, 0])

        # Initialize the visited array to track which cities we have already visited
        visited = [False] * n
        reorder_count = 0  # To count the roads that need to be reordered

        # Helper function to perform DFS on the graph
        def dfs(city: int):
            nonlocal reorder_count
            visited[city] = True  # Mark the current city as visited
            # Explore all the neighboring cities
            for neighbor, need_reorder in graph[city]:
                # If the neighbor city has not been visited
                if not visited[neighbor]:
                    # If the edge needs to be reordered, increase the reorder_count
                    if need_reorder == 1:
                        reorder_count += 1
                    # Continue DFS with the neighboring city
                    dfs(neighbor)

        # Start DFS from city 0
        dfs(0)

        # Return the total number of roads that need to be reordered
        return reorder_count

# Uncomment the following line to test the function
# print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))  # Expected output: 3
