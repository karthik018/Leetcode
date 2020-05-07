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
        d = {each.id: (each.importance, each.subordinates) for each in employees}

        total_importance = d[id][0]
        subs = d[id][1]

        while subs:
            n_subs = []
            for s in subs:
                total_importance += d[s][0]
                n_subs += d[s][1]

            subs = n_subs
            
        return total_importance
