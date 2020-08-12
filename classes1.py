# Corey Shafer videos, learn classes

import datetime


# define a new class
class Employee:

    # class variable to track number of instances (employees)
    num_of_emps = 0

    # create a class variable
    raise_amt = 1.035

    # define attributes of the class "Employee"
    def __init__(self, id_number, first, last, pay):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.salary = pay
        self.email = first + '.' + last + '@company.com'

        # increments employee count class variable each time an instance is defined
        Employee.num_of_emps += 1

    # define methods to access different attributes of the class
    def id_number(self):
        return '{}'.format(self.id_number)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def first_name(self):
        return '{}'.format(self.first)

    def last_name(self):
        return '{}'.format(self.last)

    def salary(self):
        return '{}'.format(self.salary)

    def email(self):
        return '{}'.format(self.email)

    def all_info(self):
        return '\nEmployee ID: {}\nFull name: {} {}\nEmail address: {}\nSalary: {}\n'.format(self.id_number,
                                                                                             self.first,
                                                                                             self.last,
                                                                                             self.email,
                                                                                             self.salary)

    # define function to apply a salary increase using above class variable ("raise_amount")
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    # class method to change functionality of set_raise_amount method to change class instead of instance raise amount
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # static method to determine if a particular day of week is a weekday
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# define instances of the class
emp_1 = Employee(23488855, 'Douglas', 'Blinkhorn', 75000)
emp_2 = Employee(33567821, 'Emily', 'Blinkhorn', 77000)

print("\nCurrent employees: ")

print(emp_1.all_info())
print(emp_2.all_info())

print("Total employees: " + str(Employee.num_of_emps) + "\n")

print(emp_1.full_name() + '\'s current salary: ' + str(emp_1.salary))
print('Awarded raise multiplier: ' + str(emp_1.raise_amt))


# use apply_raise method from Employee class above to apply a raise to salary
emp_1.apply_raise()

print(emp_1.full_name() + '\'s new salary: ' + str(emp_1.salary))

# print namespace of Employee class
print("\nNamespace of Employee class: " + str(Employee.__dict__))

# uses is_workday static method to check whether date below is a weekday
my_date = datetime.date(2020, 7, 27)
print("\n" + str(Employee.is_workday(my_date)))
