class Employee:
    def __init__(self, employee_id, base_salary):
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.overtime_pay = 0
        self.bonus = 0
        self.total_salary = base_salary

    def calculate_salary(self):
        self.total_salary = self.base_salary + self.overtime_pay + self.bonus

    def add_salary_item(self, name, amount):
        if name == "overtime":
            self.overtime_pay += amount
        elif name == "bonus":
            self.bonus += amount
        else:
            # Handle invalid salary item names
            pass

class SalaryItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Payroll:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def calculate_salary(self):
        for employee in self.employee_list:
            employee.calculate_salary()

    def distribute_salary(self):
        # Code to distribute salaries to employees goes here
        pass

# Example usage:
employee1 = Employee(1, 50000)
employee1.add_salary_item("overtime", 5000)
employee1.add_salary_item("bonus", 10000)

employee2 = Employee(2, 60000)
employee2.add_salary_item("bonus", 5000)

employee_list = [employee1, employee2]

payroll = Payroll(employee_list)
payroll.calculate_salary()
payroll.distribute_salary()
