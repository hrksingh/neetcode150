import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Build a frequency map to see how many times each task occurs
        task_counts = {}
        for task in tasks:
            task_counts[task] = task_counts.get(task, 0) + 1

        # 2. Identify the highest frequency (f_max) and how many tasks share that frequency (max_freq_tasks_count)
        max_freq = 0
        max_freq_tasks_count = 0

        for count in task_counts.values():
            if count > max_freq:
                max_freq = count
                max_freq_tasks_count = 1
            elif count == max_freq:
                max_freq_tasks_count += 1

        # 3. Calculate the minimum time using the "Block" formula:
        # Think of it as (max_freq - 1) groups of size (n + 1) plus the remaining tasks that also had the max frequency.

        # Example: A appears 3 times, n = 2
        # Blocks(Groups): [A, _, _] [A, _, _]
        # The last 'A' sits outside the full cooling blocks.

        gap_count = max_freq - 1
        gap_length = n + 1

        theoretical_min_time = (gap_count * gap_length) + max_freq_tasks_count

        # 4. Final check:
        # If we have many unique tasks, the theoretical_min_time might be
        # smaller than the actual number of tasks. We can't finish 10 tasks
        # in 8 slots, so we take the maximum of the two.
        return max(len(tasks), theoretical_min_time)

    def leastIntervalHeapq(self, tasks: List[str], n: int) -> int:
        # 1. Count frequencies
        counts = Counter(tasks)
        # 2. Use a Max-Heap to always pick the most frequent available task
        # Python is min-heap, so negate the counts
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        # 3. Queue to store tasks that are cooling down: (negated_count, idle_until_time)
        queue = deque()

        while max_heap or queue:
            time += 1

            if max_heap:
                # Pick the most frequent task
                cnt = heapq.heappop(max_heap) + 1  # Reduce frequency (closer to 0)
                if cnt != 0:
                    # Task still has remaining occurrences, put in cooldown
                    queue.append((cnt, time + n))

            # 4. Check if the task at the front of the queue is ready to be re-added
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time


if __name__ == "__main__":
    solution = Solution()

    # Example 1: Idle slots needed
    # A _ _ A _ _ A -> (3-1)*(2+1) + 1 = 7
    print(f"Result 1a: {solution.leastInterval(['A', 'A', 'A'], 2)}")
    print(f"Result 1b: {solution.leastIntervalHeapq(['A', 'A', 'A'], 2)}")

    # Example 2: No idle slots needed (Tasks fill the gaps)
    # A B C A B C D -> len(tasks) = 9
    print(
        f"Result 2a: {solution.leastInterval(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D'], 2)}"
    )
    print(
        f"Result 2b: {solution.leastIntervalHeapq(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D'], 2)}"
    )
