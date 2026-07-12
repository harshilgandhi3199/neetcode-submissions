from collections import deque

class Solution:
    # Kahn's Algorithm - BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an indegrees list where an indegree 
        # represents the dependency on that course by some other course
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        # 1. add all the nodes with indegree = 0 to the queue
        # if queue empty return False
        # 2. while queue is not empty:
                # pop the node from the queue
                # decrement it's indegree by 1
                # if indegree of node is 0, add it to the queue

        # return True

        queue = deque([u for u in range(numCourses) if indegree[u] == 0])

        if not queue:
            return False

        count = 0
        while queue:
            curr = queue.popleft()
            count += 1

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses
    