"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.total = 0
        self.employee={} 
        def impo(employee):
            if employee:
                self.total += employee.importance
                for i in employee.subordinates:
                    impo(self.employee[i])
         
        for i in employees:
            self.employee[i.id] = i
        impo(self.employee[id])
        return self.total
        
        
        
            