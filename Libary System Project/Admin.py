from Book import Book
from User import User
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from collections import defaultdict

@dataclass
class Admin:
    books: Dict[str, List[Book]] = field(default_factory=lambda: defaultdict(list))  # Uses a defaultdict to add new books never added before easily
    users: Dict[User, List[Book]] = field(default_factory=lambda: defaultdict(list))
    
    # --- Book Operations ---
    def add_books(self, id:int, name:str, quantity:int) -> str:
        try:
            self.books[name].append(Book(id, name, quantity))
            return "Book(s) successfully added!"
        except ValueError as e:
            return f"Error: {e}"
    
    def print_books(self) -> None:
        for key, value in self.books.items():
            print(f"Title: {key}, Amount: {value}")
    
    def get_book_counts(self) -> list[tuple[str, int]]:
        book_counts = [(k,len(v)) for (k,v) in self.books.items()]
        
        return book_counts
    
    def find_book_by_name(self, name_to_find: str) -> list[Book] | str:
        try:
            book_list = self.books[name_to_find]
            return book_list
        except KeyError as e:
            return f"Error: {e}"
             
    # --- User Operations ---
    def add_user(self, id:int, name:str) -> str:
        try:
            self.users[User(id, name)] = []
            return "User successfully added!"
        except ValueError as e:
            return f"Error: {e}"
    
    def print_users(self) -> None:
        for key, value in self.users.items():
            print(f"User: {key.name}, Borrowed Books: {value}")
    
    def get_user_names(self) -> list[str]:
        user_list = []
        for user in self.users:
            user_list.append(user.name)
        return user_list.sort()
    
    # --- Convenience ---
    def __iter__(self):
        pass
    
    def __len__(self):
        pass
