class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [year for year in range(1950,2051)]
        answer = [0, 0]
        for year in years:
            population = 0
            for birth, death in logs:
                if birth <= year < death:
                    population += 1
            if population > answer[0]:
                answer = [population, year]
            
        return answer[1]