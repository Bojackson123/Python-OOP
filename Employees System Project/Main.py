from EmployeeManager import EmployeeManager
from Data import EMPLOYEE_MANIFEST
from Exception import EmployeeNotFoundError
import tkinter as tk
from FrontendManager import FrontendManager

# initialize employee manager and load the manifest data
employees = EmployeeManager()
for emp in EMPLOYEE_MANIFEST:
    employees.add(emp[0], emp[1], emp[2])


# initialize tkinter
root = tk.Tk()
app = FrontendManager(root, employees)
app.load_ui()
root.mainloop()


### __iter__, __len__, and PRINT EMPLOYEES methods
# print(len(employees))
# employees.print_employees()


### --- FIND BY NAME & REQUIRE BY NAME
# print(employees.find_by_name("Carol Williams"))
# print(employees.find_by_name("Rashid Al-Marri")) # this one will simply return None if not in system (less strict)

# print(employees.require_by_name("Carol Williams"))
# print(employees.require_by_name("Rashid Al-Marri")) # this one will throw an error (name not in system but REQUIRED)


### --- UPDATE SALARY ---
# try:
#     employees.update_salary("Carol Williams", 10000)
#     employees.update_salary("Rashid Al-Mari", 10000) # this uses the require_by_name method so should throw an error. Catch the error in a try:except and print it instead

# except EmployeeNotFoundError as e:
#     print(e)

# print(employees.find_by_name("Carol Williams"))


# ### --- DELETE BY AGE RANGE ---
# employees.delete_by_age_range(30, 40)
