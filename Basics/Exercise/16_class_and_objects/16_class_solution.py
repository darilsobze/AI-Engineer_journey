class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

emp = Employee(1, "coder")
# print(emp)
del emp.id
try:
    print(emp.id)
except Exception as err:
    print(f"emp.id isn't defined")


