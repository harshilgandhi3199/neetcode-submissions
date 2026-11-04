from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bfs
        if amount == 0:
            return 0

        seen = {amount}
        queue = deque([amount])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for c in coins:
                    rem = curr - c
                    if rem == 0:
                        return steps
                    if rem > 0 and rem not in seen:
                        queue.append(rem)
                        seen.add(rem)

        return -1