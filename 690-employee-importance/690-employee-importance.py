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
        def impo(employee):
            if employee:
                self.total += employee.importance
                for i in employee.subordinates:
                    for j in employees:
                        if j.id == i:
                            impo(j)
                            break
        
        for employee in employees:
            if employee.id == id:
                impo(employee)
                break
        return self.total
        
        
        
            