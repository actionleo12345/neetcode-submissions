class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)

        res = []

        seen, visited = set(), set()
        def dfs(course):
            if course in seen:
                return False

            if course in visited:
                return True
            
            seen.add(course)
            
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False

            visited.add(course)
            seen.remove(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res                
            