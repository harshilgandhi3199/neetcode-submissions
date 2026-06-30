class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build an adjancency list
        pre_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        
        path = set()

        def dfs(course):
            if course in path:
                return False
            
            if pre_map[course] == []:
                return True

            path.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            pre_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

