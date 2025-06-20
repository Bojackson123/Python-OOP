import tkinter as tk
from EmployeeManager import EmployeeManager
from Exception import EmployeeNotFoundError

class FrontendManager():
    def __init__(self, root, employee_manager: EmployeeManager):
        self.root = root
        self.root.title("Employees System Project")
        self.root.geometry("800x600")
        self.manager = employee_manager

    # --- Helper Functions ---
    def refresh_employee_list(self):
        self.populate_employee_list()
        
    def add_employee(self, name, age, salary):
        # Get the string content from the Text widgets
        name = name.get("1.0", tk.END).strip()
        age = age.get("1.0", tk.END).strip()
        salary = salary.get("1.0", tk.END).strip()
        
        # Validate inputs - simple checks
        if not name or not age or not salary:
            self._toast("Please fill all fields!", is_error=True)
            return
        
        try:
            age_int = int(age)
            salary_float = float(salary)
        except ValueError:
            self._toast("Age must be an integer and Salary must be a number.", is_error=True)
            return
        
        
        self.manager.add(name, age_int, salary_float)
        self.refresh_employee_list()
        self._toast("Employee Successfully Added!")
    
    
    def remove_employee(self, name):
        name = name.get("1.0", tk.END).strip()
        
        # Validate inputs - simple checks
        if not name:
            self._toast("Please fill all fields!", is_error=True)
            return
        try:
            self.manager.remove_employee(name)
        except EmployeeNotFoundError as e:
            print(e)
            self._toast(e, is_error=True)
            return
        
        self.refresh_employee_list()
        self._toast("Employee Successfully Removed!")
    
    
    def search_employees(self, name):
        name = name.get("1.0", tk.END).strip()
        
        if not name:
            self._toast("Please fill all fields!", is_error=True)
            return
        
        try:
            emp = self.manager.require_by_name(name)
        except EmployeeNotFoundError as e:
            self._toast(e, is_error=True)
            return
        list_emp = [emp]
        self.display_filtered_employees(list_emp)
        self._toast(f"Found {len(list_emp)} employee(s)!")
    
    def remove_by_age_range(self, start, stop):
        start = start.get("1.0", tk.END).strip()
        stop = stop.get("1.0", tk.END).strip()
        
        try:
            start_int = int(start)
            stop_int = int(stop)
        except ValueError:
            self._toast("Age must be an integer.", is_error=True)
            return
        
        msg = self.manager.delete_by_age_range(start_int, stop_int)
        self.refresh_employee_list()
        self._toast(msg)
    
    
    def _toast(self, msg: str, ms: int = 2500, is_error: bool = False):
        """Popup a small borderless window that auto-dismisses."""
        toast = tk.Toplevel(self.root)
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)

        bg_color = "#cc0000" if is_error else "#0EA809"
        fg_color = "white"

        lbl = tk.Label(toast, text=msg,
                    bg=bg_color, fg=fg_color,
                    padx=12, pady=6, font=("Segoe UI", 10, "bold" if is_error else "normal"))
        lbl.pack()

        # Position: center of root window
        self.root.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width()  // 2) - (toast.winfo_reqwidth()  // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (toast.winfo_reqheight() // 2) - 20

        toast.geometry(f"+{x}+{y}")

        toast.after(ms, toast.destroy)


    
    
    # --- User Interface --- 
    def load_ui(self):
        self.add_employee_ui()
        self.search_employees_ui()
        self.remove_employee_ui()
        self.remove_by_age_ui()
        self.build_employee_list_frame()
    
    def add_employee_ui(self):
        # Add Employee Label
        add_label = tk.Label(self.root, text="Add Employee")
        add_label.grid(row=0, column=0, columnspan=3)
        
        # Name label and box
        name_add_label = tk.Label(self.root, text="Name:")
        name_add_label.grid(row=1, column=0, sticky="w", padx=5)
        self.name_add_box = tk.Text(self.root, height=1, width=20)
        self.name_add_box.grid(row=2, column=0, padx=5)
        
        # Age label and box
        age_label = tk.Label(self.root, text="Age:")
        age_label.grid(row=1, column=1, sticky="w", padx=5)
        self.age_box = tk.Text(self.root, height=1, width=5)
        self.age_box.grid(row=2, column=1, padx=5)
        
        # Salary label and box
        salary_label = tk.Label(self.root, text="Salary:")
        salary_label.grid(row=1, column=2, sticky="w", padx=5)
        self.salary_box = tk.Text(self.root, height=1, width=10)
        self.salary_box.grid(row=2, column=2, padx=5)
    
        add_employee_button = tk.Button(self.root, text="Submit", command=lambda: self.add_employee(self.name_add_box, self.age_box, self.salary_box))
        add_employee_button.grid(row=3, column=0,columnspan=3, padx=5, pady=20)
    
    def remove_employee_ui(self):
        # remove Employee Label
        remove_label = tk.Label(self.root, text="Remove Employee")
        remove_label.grid(row=0, column=3, columnspan=2)
        
        # Name label and box
        name_remove_label = tk.Label(self.root, text="Name:")
        name_remove_label.grid(row=1, column=3, sticky="w", padx=70)
        self.name_remove_box = tk.Text(self.root, height=1, width=20)
        self.name_remove_box.grid(row=2, column=3, padx=70)
        
        remove_employee_button = tk.Button(self.root, text="Submit", command=lambda: self.remove_employee(self.name_remove_box))
        remove_employee_button.grid(row=3, column=3,columnspan=2, padx=5, pady=20)
    
    
    def search_employees_ui(self):
        search_label = tk.Label(self.root, text="Search Employees")
        search_label.grid(row=4, column=0, columnspan=3)

        # Name label and box
        name_search_label = tk.Label(self.root, text="Name:")
        name_search_label.grid(row=5, column=0, sticky="w", padx=5)
        self.name_search_box = tk.Text(self.root, height=1, width=20)
        self.name_search_box.grid(row=6, column=0, padx=5)
        
        # submit button
        search_employee_button = tk.Button(self.root, text="Submit", command=lambda: self.search_employees(self.name_search_box))
        search_employee_button.grid(row=7, column=0,columnspan=3, padx=5, pady=20)
    
    
    def remove_by_age_ui(self):
        # remove Employee Label
        remove_label = tk.Label(self.root, text="Remove Employees by Age Range")
        remove_label.grid(row=4, column=3, columnspan=2)
        
        # Age 1 label and box
        age_range1_label = tk.Label(self.root, text="Age (Start):")
        age_range1_label.grid(row=5, column=3, sticky="w", padx=5)
        self.age_range1_box = tk.Text(self.root, height=1, width=5)
        self.age_range1_box.grid(row=6, column=3, padx=5, sticky="w")
        
        # Age 2 label and box
        age_range2_label = tk.Label(self.root, text="Age: (Stop)")
        age_range2_label.grid(row=5, column=4, sticky="w", padx=5)
        self.age_range2_box = tk.Text(self.root, height=1, width=5)
        self.age_range2_box.grid(row=6, column=4, padx=5, sticky="w")
        
        remove_employee_button = tk.Button(self.root, text="Submit", command=lambda: self.remove_by_age_range(self.age_range1_box, self.age_range2_box))
        remove_employee_button.grid(row=7, column=3,columnspan=2, padx=5, pady=20)
    
    
    def build_employee_list_frame(self):
        # Label for the employee list
        self.list_label = tk.Label(self.root, text=f"Employee List: {len(self.manager)} entries")
        self.list_label.grid(row=8, column=0, columnspan=5, sticky="ew", padx=5, pady=(10, 0))

        # Container for scrollable list
        container = tk.Frame(self.root)
        container.grid(row=9, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

        # Resize handling
        self.root.grid_rowconfigure(9, weight=1)
        for col in range(5):
            self.root.grid_columnconfigure(col, weight=1)

        # Canvas + scrollbar
        self.canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Frame inside canvas
        self.list_frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.list_frame, anchor="nw")

        def resize_frame(event):
            self.canvas.itemconfig(self.canvas_window, width=event.width - 6)
        self.canvas.bind("<Configure>", resize_frame)

        def on_frame_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.list_frame.bind("<Configure>", on_frame_configure)

        def _on_mousewheel(event):
            self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")
        self.list_frame.bind_all("<MouseWheel>", _on_mousewheel)

        # Button to trigger refresh
        refresh_button = tk.Button(self.root, text="Refresh List", command=self.refresh_employee_list)
        refresh_button.grid(row=10, column=0, columnspan=5, pady=10)


    def populate_employee_list(self):
        # Clear old labels
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        # Rebuild labels
        for emp in self.manager.employees:
            text = f"{emp.name} | Age: {emp.age} | Salary: {emp.salary}"
            label = tk.Label(
                self.list_frame,
                text=text,
                borderwidth=1,
                relief="solid",
                padx=10,
                pady=5,
                anchor="center",
                justify="center"
            )
            label.pack(fill="x", expand=True, pady=2)

        # Update the label count
        self.list_label.config(text=f"Employee List: {len(self.manager)} entries")
        
    def display_filtered_employees(self, filtered_employees):
        # Clear current list
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        # Show filtered results
        for emp in filtered_employees:
            text = f"{emp.name} | Age: {emp.age} | Salary: {emp.salary}"
            label = tk.Label(
                self.list_frame,
                text=text,
                borderwidth=1,
                relief="solid",
                padx=10,
                pady=5,
                anchor="center",
                justify="center"
            )
            label.pack(fill="x", expand=True, pady=2)

        # Update label count
        self.list_label.config(text=f"Search Results: {len(filtered_employees)} entries")




    
