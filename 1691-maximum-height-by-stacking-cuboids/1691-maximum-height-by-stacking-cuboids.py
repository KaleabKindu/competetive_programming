from itertools import permutations

class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        
        cubes = []
        for cube in cuboids:
            seen = set()
            for perm in list(permutations(cube)):
                if (perm[0], perm[1], perm[2]) not in seen:
                    cubes.append(list(perm))
                    seen.add((perm[0], perm[1], perm[2]))
                    
        cubes = sorted(cubes, key=lambda cube: cube[0] * cube[1] * cube[2])
        n = len(cubes)
        valid = lambda cube1, cube2: cube1[0] <= cube2[0] and cube1[1] <= cube2[1] and cube1[2] <= cube2[2]
        
        dp = [cube[2] for cube in cubes]
        for i in range(n - 1, -1, -1):
            maxx = 0
            for j in range(i + 1, n):
                if valid(cubes[i], cubes[j]):
                    maxx = max(maxx, dp[j])
            dp[i] += maxx
        return max(dp)
        
        