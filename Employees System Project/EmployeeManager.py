from dataclasses import dataclass, field
from typing import List, Optional
from Employee import Employee
from Exception import EmployeeNotFoundError

@dataclass
class EmployeeManager:
    employees: List[Employee] = field(default_factory=list)
    
    # -- CRUD operations -- 
    def add(self, name:str, age:int, salary:float) -> None:
        self.employees.append(Employee(name, age, salary))
        self.employees.sort(key=lambda x: x.name.strip().lower())
        
    def print_employees(self) -> None:
        for emp in self.employees:
            print(f'Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}')
            
    def find_by_name(self, name_to_find: str) -> Optional[Employee]:
        for emp in self.employees:
            if emp.name == name_to_find:
                return emp
        return None
    
    def require_by_name(self, name_to_find:str) -> Employee:
        for emp in self.employees:
            if emp.name == name_to_find:
                return emp
        raise EmployeeNotFoundError(f"No employee with name: {name_to_find}")
    
    def remove_employee(self, name_to_remove):
        self.employees.remove(self.require_by_name(name_to_remove))
    
    def update_salary(self, name:str, new_salary:float) -> None:
        self.require_by_name(name).salary = new_salary
        
    def delete_by_age_range(self, start:int, stop:int, inclusive:bool = True) -> None:
        low = (lambda x: x >= start) if inclusive else (lambda x: x > start)
        hi = (lambda x: x <= stop) if inclusive else (lambda x: x < stop)
        
        before_del = len(self.employees)
        self.employees = [i for i in self.employees if not (low(i.age) and hi(i.age))]
        amount_del = before_del - len(self.employees)
        
        return f"Successfully deleted {amount_del} employees!"
        
    def sort_employees(self):
        self.employees.sort(key=lambda x: x.name.strip().lower())

    # -- Convenience --
    def __iter__(self):
        return iter(self.employees)
    
    def __len__(self):
        return len(self.employees)
        
        