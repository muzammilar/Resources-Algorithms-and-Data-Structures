class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # Stack to track asteroids in the current state

        for asteroid in asteroids:
            # Process the current asteroid
            while stack and asteroid < 0 and stack[-1] > 0:
                # Handle the collision between the asteroid and the one in the stack
                top = stack[-1]
                if top < -asteroid:
                    # The current asteroid destroys the one in the stack
                    stack.pop()
                    continue
                elif top == -asteroid:
                    # Both asteroids are destroyed
                    stack.pop()
                break
            else:
                # No collision, or asteroid is moving right (positive), so just add it to the stack
                stack.append(asteroid)

        return stack

# Test the solution
# if __name__ == "__main__":
#     solution = Solution()
#     # Example test case
#     asteroids = [5, 10, -5]
#     print(solution.asteroidCollision(asteroids))  # Output: [5, 10]
