from dataclasses import dataclass, field
from typing import ClassVar

@dataclass(frozen=True)
class User:
    _id_counter: ClassVar[int] = 0  # class-level counter (not part of instance)

    id: int = field(init=False)     # exclude from init, will set manually
    name: str

    def __post_init__(self):
        cls = self.__class__
        object.__setattr__(self, 'id', cls._id_counter)
        cls._id_counter += 1
