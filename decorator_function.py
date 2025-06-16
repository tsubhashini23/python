# Decorator: 
#     It is a function that takes another function as input
#     Wraps it with additional behaviour
#     Returns a new function
#     A decorator enhances another function
#     @staticmethod @classmethod are some builtin decorators available in python. User can also create decorators

class Employee:
    company = "OpenAI"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        print("Changing company name...")
        cls.company = new_name

    @staticmethod
    def is_workday(day):
        print("Checking if workday...")
        return day.lower() not in ['saturday', 'sunday']


e1 = Employee("Alice", 50000)

print(f"Initial company: {Employee.company}")   

Employee.change_company("DeepMind") 
print(f"Updated company: {Employee.company}")  

print(Employee.is_workday("Monday")) 
print(Employee.is_workday("Sunday")) 