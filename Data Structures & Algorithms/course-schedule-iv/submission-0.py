class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for p, c in prerequisites:
            adj[c].append(p)

        
        def dfs(course):
            if course not in prereqMap:
                prereqMap[course] = set()

                for pre in adj[course]:
                    prereqMap[course] |= dfs(pre) # "|=" means union sets
                prereqMap[course].add(course)
            
            return prereqMap[course]

        prereqMap = {}

        for c in range(numCourses):
            dfs(c)

        res = []
        for pre, crs in queries:
            res.append(pre in prereqMap[crs])

        return res



                