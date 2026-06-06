from collections import Counter
from typing import List


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequencies of each task
        frequencies = Counter(tasks)

        # Step 2: Find the maximum frequency
        f_max = max(frequencies.values())

        # Step 3: Count how many tasks have that maximum frequency
        count_max = sum(1 for count in frequencies.values() if count == f_max)

        # Step 4: Calculate the minimum intervals needed by formula
        min_time = (f_max - 1) * (n + 1) + count_max

        # Step 5: Return the maximum of the formula or the total number of tasks
        return max(min_time, len(tasks))