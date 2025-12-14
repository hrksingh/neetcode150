from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Simulate asteroid collisions in space.

        Rules:
        - Positive values: asteroids moving right →
        - Negative values: asteroids moving left ←
        - When they collide, smaller one explodes
        - Same size: both explode

        Args:
            asteroids: List of integers representing asteroid sizes and directions

        Returns:
            List of asteroids remaining after all collisions

        Time Complexity: O(n) - each asteroid pushed/popped at most once
        Space Complexity: O(n) - stack stores surviving asteroids
        """
        stack = []  # Stores asteroids that haven't collided yet

        for current_asteroid in asteroids:
            # Process collisions while conditions are met:
            # 1. Stack is not empty
            # 2. Current asteroid moving left (negative)
            # 3. Top of stack moving right (positive)
            # This creates a collision scenario: → ←
            while stack and current_asteroid < 0 < stack[-1]:
                # Calculate collision result (sum of sizes)
                # If positive: right-moving wins
                # If negative: left-moving wins
                # If zero: both explode
                collision_result = stack[-1] + current_asteroid

                # If top asteroid is smaller or equal, it explodes
                if collision_result <= 0:
                    stack.pop()

                # If current asteroid is smaller or equal, it explodes
                # Break because current asteroid is destroyed
                if collision_result >= 0:
                    break

                # If collision_result < 0, current asteroid survived
                # Loop continues to check next collision
            else:
                # No collision occurred (or current survived all collisions)
                # Add current asteroid to stack
                # This happens when:
                # 1. Stack is empty
                # 2. Both moving same direction (no collision)
                # 3. Current moving right (can't collide with left-moving)
                # 4. Current survived all collisions (while loop ended naturally)
                stack.append(current_asteroid)

        return stack
