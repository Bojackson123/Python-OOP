from Frontend import FrontendTUI
from Admin import Admin

admin = Admin()

options = [
    {
        "label": "Add Books", 
        "function": admin.add_books,
        "prompt_args": ["Enter name of book", "Enter quantity"],
        "prompt_types": [str, int]
    },
    
    {
        "label": "Add User", 
        "function": admin.add_user,
        "prompt_args": ["Enter user name"],
        "prompt_types": [str]
        
    }
]

frontend = FrontendTUI(options, "Libary System Project")
frontend.run()
