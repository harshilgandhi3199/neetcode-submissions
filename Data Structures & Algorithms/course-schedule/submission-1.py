class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj list course -> list of pre
        # Use a set to track current DFS path
        # For each course
            # Run DFS
            # If course is already in tje path: return False
            # Recursively call DFS on pre   
        # After successdully processing a course, clear its pre
        # If all courses are processed witrhout cycles, return True

        course_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            course_map[course].append(pre)

        path = set()

        def dfs(course):
            # base case - if course found in path return False - because a cycle
            if course in path:
                return False

            if course_map[course] == []:
                return True

            path.add(course)
            for pre in course_map[course]:
                if not dfs(pre):
                    return False
            
            path.remove(course)
            course_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
