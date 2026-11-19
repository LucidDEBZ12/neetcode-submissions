class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        # 1. Create graph
        order=[]
        g = defaultdict(list)
        courses = prerequisites

        # 2. Fill graph
        for a, b in courses:
            g[a].append(b)

        # 3. Define states
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # 4. Create states array
        states = [UNVISITED] * numCourses

        # 5. Define DFS
        def dfs(node):
            state = states[node]

            if state == VISITED:
                return True
            elif state == VISITING:
                return False

            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            order.append(node)
            return True

        # 6. Start checking all courses
        for i in range(numCourses):
            if not dfs(i):
                return []

        return order