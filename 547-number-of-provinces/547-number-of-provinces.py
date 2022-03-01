class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        self.province = 0
        def dfs(city):
            self.visited.add(city)
            for i in range(len(isConnected[city])):
                if i not in self.visited and isConnected[city][i] == 1:
                    dfs(i)
                
        for i in range(len(isConnected)):
            if i not in self.visited:
                self.province += 1
                dfs(i)
        return self.province
                
            