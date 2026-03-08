class Employee:
    raise_amt = 1.07
    num_of_employees = 0

    def __init__(self, first, last, pay, contract):
        self.first = first
        self.last = last
        self.salary = pay
        self.contract = contract
        self.full_name()
        Employee.num_of_employees += 1

    def create_email(self):
        self.email = self.first + "." + self.last + "@comapny.com"

    def apply_raise(self):
        self.salary = self.salary * self.raise_amt

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def new_cls_emp(cls, emp_str):
        first, last, pay, contract = emp_str.split("-")
        return cls(first, last, pay, contract)

    @staticmethod
    def is_workday(date):
        if date.day() == 5 or date.day() == 6:
            return False
        return True

    def full_name(self):
        self.full_name = self.first + " " + self.last

    def __repr__(self):
        return "Employee({} , {} , {}, {})".format(
            self.first, self.last, self.salary, self.contract
        )

    def __str__(self):
        return "{},{}".format(self.full_name, self.contract)


class Developer(Employee):
    def __init__(self, first, last, pay, contract, prog_lang):
        super().__init__(first, last, pay, contract)
        self.prog_lang = prog_lang
        raise_amt = 1.20


class Manager(Employee):
    def __init__(self, first, last, pay, contract, employees=None):
        super().__init__(first, last, pay, contract)
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        """A function to add employees"""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        """To remove an employee"""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for employees in self.employees:
            print("-->{}".format(employees.full_name))


Employee.set_raise_amount(1.09)
emp_1 = Employee("Abhi", "Bijish", 100000, "20 years")
emp_2 = Employee("Bijish", "Sidharthan", 9000, "15")
manager_1 = Manager("Abhinav", "Bijish", "10000000", "30 years", [emp_1, emp_2])

emp_1.create_email()
emp_1.apply_raise()
emp_2.apply_raise()
emp_1_str = "John-Doe-8000-14"
emp_2_str = "Mary-Ane-8500-12"
new_emp_3 = Employee.new_cls_emp(emp_1_str)
manager_1.add_employee(new_emp_3)
manager_1.remove_employee(emp_2)
print(emp_1)
