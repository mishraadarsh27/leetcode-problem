class Solution:
    def average(self, salary: list[int]) -> float:
        n = len(salary)
        maxSalary = max(salary)
        minSalary = min(salary)
        total = 0
        for s in salary:
            if s != maxSalary and s != minSalary:
                total += s
        return total / (n - 2)