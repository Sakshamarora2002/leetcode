class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        # we will be creating a list using default dictionary
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen=set()
        seen.add(source)
        def dfs(i):
            if i==destination:
                return True
            for neighbor in graph[i]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            return False
        return dfs(source)
                
            
        