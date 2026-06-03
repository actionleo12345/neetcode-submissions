class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            prereqs[c].append(p)

        def cycle(course, seen):
            if course in seen:
                return True
            
            if prereqs[course] == []:
                return False

            seen.add(course)
            for pre in prereqs[course]:
                if cycle(pre, seen):
                    return True
            prereqs[course] = [] # clean up the prereq course
            seen.remove(course)

            return False


        seen = set()
        for course in range(numCourses):
            if cycle(course, seen):
                return False

        return True