from dataclasses import dataclass, field
from Patient import Patient
import heapq
from datetime import time
from typing import Optional, List


@dataclass
class ERIntake:
    patients: List[Patient] = field(default_factory=list)
    
    def add_patient(self, arrival_time: time, name: str, status: int) -> None:
        heapq.heappush(self.patients, Patient(arrival_time, name, status))
    
    def next_patient(self) -> Optional[Patient]:
        if self.patients:
            return heapq.heappop(self.patients)
        return None
    
    def update_queue(self) -> None:
        heapq.heapify(self.patients)
    
    def find_by_name(self, name_to_find: str) -> Patient:
        for pat in self.patients:
            if pat.name == name_to_find:
                return pat
        return None
    
    def remove_patient(self, name_to_remove: str) -> None:
        pat = self.find_by_name(name_to_remove)
        if pat:
            self.patients.remove(pat)
            self.update_queue()
        else:
            print("Patient not found!")

    
    def update_status(self, name_to_update: str, new_status: int) -> None:
        pat = self.find_by_name(name_to_update)
        if pat:
            pat.status = new_status
            self.update_queue()
        else:
            print("Patient not found!")
        
    
    
    
    