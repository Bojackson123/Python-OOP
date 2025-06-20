from dataclasses import dataclass, field
from datetime import time


@dataclass(order=True) # order changes the default __lt__ method (less than) and __gt__ (greater than) to compare class objects.
class Patient:
    status: int
    arrival_time: time 
    name: str = field(compare=False) # excludes from __lt__ method
