class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        """
        This function determines whether it's possible to visit all rooms starting from room 0.

        :param rooms: list[list[int]] - a list of rooms where each room contains a list of keys
        :return: bool - True if all rooms are visitable, False otherwise
        """
        # A set to keep track of visited rooms
        visited = set()

        # DFS function to explore rooms
        def dfs(room):
            # Mark the current room as visited
            visited.add(room)
            # Visit all the rooms we can reach with the keys from the current room
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        # Start DFS from room 0
        dfs(0)

        # Check if all rooms were visited
        return len(visited) == len(rooms)

# Example usage:
# sol = Solution()
# print(sol.canVisitAllRooms([[1],[2],[3],[]]))  # Output: True
