from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Book:
    _id_counter: ClassVar[int] = 0  # Class-level ID counter (shared across all instances)

    id: int = field(init=False)     # Will be auto-generated
    name: str

    def __post_init__(self):
        self.id = Book._id_counter
        Book._id_counter += 1
