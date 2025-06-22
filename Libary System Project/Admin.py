from Book import Book
from User import User
from dataclasses import dataclass, field
from typing import List, Dict
from collections import defaultdict

@dataclass
class Admin:
    books: Dict[str, List[Book]] = field(default_factory=lambda: defaultdict(list))
    users: Dict[User, List[Book]] = field(default_factory=lambda: defaultdict(list))
    
    # --- Book Operations ---
    def add_books(self, id:int, name:str, quantity:int) -> str:
        try:
            # Check if book with same ID already exists
            for book_list in self.books.values():
                for book in book_list:
                    if book.id == id:
                        return f"Error: Book with ID {id} already exists!"
            
            self.books[name].append(Book(id, name, quantity))
            return "Book(s) successfully added!"
        except ValueError as e:
            return f"Error: {e}"
    
    def print_books(self) -> None:
        for key, value in self.books.items():
            print(f"Title: {key}, Amount: {len(value)}")
    
    def get_book_counts(self) -> list[tuple[str, int]]:
        book_counts = [(k,len(v)) for (k,v) in self.books.items()]
        
        return book_counts
    
    def find_book_by_name(self, name_to_find: str) -> tuple[str, int] | str:
        try:
            book_list = self.books[name_to_find]
            return name_to_find, len(book_list)
        except KeyError as e:
            return f"Error: {e}"
    
    def is_book(self, book_name:str) -> bool:
        return book_name in self.books
    
    def in_stock(self, book_name:str) -> bool:
        return self.is_book(book_name) and len(self.books[book_name]) > 0
    
    def borrow_book(self, book_name: str, user_name: str) -> str:
        # Find the user by name
        user = self._find_user_by_name(user_name)
        if not user:
            return f"No user with name: {user_name}!"
        
        # Check if book exists and is in stock
        if not self.is_book(book_name):
            return f"Book: {book_name} does not exist!"
        
        if not self.in_stock(book_name):
            return f"Book: {book_name} is out of stock!"
        
        # Borrow the book
        book_to_move = self.books[book_name].pop()
        self.users[user].append(book_to_move)
        return f"Book '{book_name}' successfully borrowed by {user_name}!"
    
    def return_book(self, book_name: str, user_name: str) -> str:
        # Find the user by name
        user = self._find_user_by_name(user_name)
        if not user:
            return f"No user with name: {user_name}!"
        
        # Check if user has borrowed this book
        user_books = self.users[user]
        for i, book in enumerate(user_books):
            if book.name == book_name:
                # Return the book
                returned_book = user_books.pop(i)
                self.books[book_name].append(returned_book)
                return f"Book '{book_name}' successfully returned by {user_name}!"
        
        return f"User {user_name} has not borrowed book '{book_name}'!"
    
    def _find_user_by_name(self, name: str) -> User | None:
        """Helper method to find user by name."""
        for user in self.users:
            if user.name == name:
                return user
        return None
    
    def _find_user_by_id(self, user_id: int) -> User | None:
        """Helper method to find user by ID."""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def is_user(self, name: str) -> bool:
        """Check if a user with given name exists."""
        return self._find_user_by_name(name) is not None
    
    # --- User Operations ---
    def add_user(self, id:int, name:str) -> str:
        try:
            # Check if user with same ID already exists
            if self._find_user_by_id(id):
                return f"Error: User with ID {id} already exists!"
            
            # Check if user with same name already exists
            if self._find_user_by_name(name):
                return f"Error: User with name '{name}' already exists!"
            
            self.users[User(id, name)] = []
            return "User successfully added!"
        except ValueError as e:
            return f"Error: {e}"
    
    def print_users(self) -> None:
        for key, value in self.users.items():
            print(f"User: {key.name} (ID: {key.id}), Borrowed Books: {len(value)}")
    
    def get_user_names(self) -> list[str]:
        user_list: list[str] = []
        for user in self.users:
            user_list.append(user.name)
        user_list.sort()
        return user_list
    
    def get_users_who_borrowed(self) -> dict:
        dict_of_borrowers = {k: v for k,v in self.users.items() if len(v) > 0 } 
        
        return dict_of_borrowers
    
    def get_user_info(self) -> dict:
        return self.users
    
    
    
    # --- Convenience ---
    def __iter__(self):
        """Iterate over all books in the library."""
        for book_list in self.books.values():
            for book in book_list:
                yield book
    
    def __len__(self):
        """Return a tuple of (number of users, total number of books)."""
        total_books = sum(len(book_list) for book_list in self.books.values())
        return (len(self.users), total_books)
