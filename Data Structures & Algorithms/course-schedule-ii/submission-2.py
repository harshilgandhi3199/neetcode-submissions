class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            course_map[course].append(pre)

        path = set()
        # allows us to keep original graph intact
        # process each course and append it to the result
        visited = set()
        result = []

        def dfs(course):
            nonlocal result
            # base case - if course found in path return False - because a cycle
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            for pre in course_map[course]:
                if not dfs(pre):
                    return False
            
            path.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result 