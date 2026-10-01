class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj map
        courses = defaultdict(list)
        for course, dep in prerequisites:
            courses[course].append(dep)

        path = set()

        def dfs(course):
            # base case
            if course in path:
                return False
            
            if courses[course] == []:
                return True

            path.add(course)
            for dep in courses[course]:
                if not dfs(dep):
                    return False

            path.remove(course)
            courses[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True