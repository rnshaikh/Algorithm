"""
690. Employee Importance
You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

"""

"""
    store emp obj in hashmap
    then perform dfs on subordinate and add importance

    return importance

"""




"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:

    def find_employee(self, id, employees):

        employee = None
        for i in range(len(employees)):
            if employees[i].id == id:
                employee = employees[i]

        return employee


    def dfs_util(self, id, hash_map, imp):

        emp = hash_map.get(id)
        imp = imp + emp.importance

        for i in emp.subordinates:
            imp = self.dfs_util(i, hash_map, imp)

        return imp

    def getImportance(self, employees: List['Employee'], id: int) -> int:


        hash_map = {}
        for i in employees:
            hash_map[i.id] = i

        imp = hash_map.get(id).importance
        return self.dfs_util(id, hash_map, 0)




#         employee = None
#         employee = self.find_employee(id, employees)

#         if employee:
#             importance = employee.importance
#             subordinates = []
#             subordinates = subordinates + employee.subordinates
#             while(len(subordinates)):
#                 sub = subordinates.pop(0)
#                 sub_emp = self.find_employee(sub, employees)

#                 importance = importance + sub_emp.importance
#                 subordinates = subordinates + sub_emp.subordinates

#             return importance
