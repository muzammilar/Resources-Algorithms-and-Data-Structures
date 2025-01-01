class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # Graph representation using an adjacency list
        graph = {}

        # Build the graph with equations and values
        for (u, v), value in zip(equations, values):
            # add default value for `u` as empty list if it doesn't exist
            graph[u] = graph.get(u, [])
            # add default value for `v` as empty list if it doesn't exist
            graph[v] = graph.get(v, [])
            # add division values
            graph[u].append((v, value))
            graph[v].append((u, 1 / value))

        # Helper function for DFS
        def dfs(start, end, visited):
            # If the start equals the end, return 1 (a / a = 1)
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return result * weight
            return -1.0

        # Answer the queries
        result = []
        for u, v in queries:
            if u not in graph or v not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(u, v, set()))

        return result

# Uncomment the following line to test the function
# print(Solution().calcEquation([["a","b"], ["b","c"]], [2.0, 3.0], [["a","c"], ["b","a"], ["a","e"], ["a","a"], ["x","x"]]))  # Expected output: [6.0, 0.5, -1.0, 1.0, -1.0]
