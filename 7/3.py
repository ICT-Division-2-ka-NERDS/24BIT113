# Sample data
employees = [
    {"dept_no": "D01", "emp_roll": "E101", "salary": 50000},
    {"dept_no": "D01", "emp_roll": "E102", "salary": 60000},
    {"dept_no": "D02", "emp_roll": "E201", "salary": 45000},
    {"dept_no": "D02", "emp_roll": "E202", "salary": 70000},
    {"dept_no": "D03", "emp_roll": "E301", "salary": 40000},
    {"dept_no": "D03", "emp_roll": "E302", "salary": 80000},
]

# Dictionary to store department-wise salaries
dept_salaries = {}

# Group salaries by department
for emp in employees:
    dept = emp["dept_no"]
    salary = emp["salary"]
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)

# Find min and max salary per department
dept_salary_summary = {
    dept: {"min_salary": min(salaries), "max_salary": max(salaries)}
    for dept, salaries in dept_salaries.items()
}

# Output result
for dept, summary in dept_salary_summary.items():
    print(f"Department {dept} - Min Salary: {summary['min_salary']}, Max Salary: {summary['max_salary']}")
