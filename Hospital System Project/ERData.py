from datetime import time

# Hardcoded mock data for the ER system
MOCK_PATIENTS = [
    # Critical patients (Priority 1)
    {"name": "Sarah Johnson", "time": "08:15", "status": 1},
    {"name": "Michael Chen", "time": "09:30", "status": 1},
    {"name": "Emily Rodriguez", "time": "10:45", "status": 1},
    
    # Serious patients (Priority 2)
    {"name": "David Thompson", "time": "08:45", "status": 2},
    {"name": "Lisa Wang", "time": "09:15", "status": 2},
    {"name": "Robert Davis", "time": "10:20", "status": 2},
    {"name": "Jennifer Lee", "time": "11:00", "status": 2},
    
    # Stable patients (Priority 3)
    {"name": "Christopher Brown", "time": "08:30", "status": 3},
    {"name": "Amanda Wilson", "time": "09:00", "status": 3},
    {"name": "James Miller", "time": "09:45", "status": 3},
    {"name": "Nicole Garcia", "time": "10:10", "status": 3},
    {"name": "Kevin Martinez", "time": "10:30", "status": 3},
    
    # Minor patients (Priority 4)
    {"name": "Rachel Taylor", "time": "08:00", "status": 4},
    {"name": "Daniel Anderson", "time": "08:20", "status": 4},
    {"name": "Michelle White", "time": "08:40", "status": 4},
    {"name": "Steven Jackson", "time": "09:10", "status": 4},
    {"name": "Jessica Moore", "time": "09:25", "status": 4},
    {"name": "Ryan Lewis", "time": "09:50", "status": 4},
    {"name": "Ashley Hall", "time": "10:05", "status": 4},
    {"name": "Matthew Allen", "time": "10:25", "status": 4}
]

def get_mock_patients():
    """Return the list of mock patients with proper time objects"""
    patients = []
    for patient_data in MOCK_PATIENTS:
        hour, minute = map(int, patient_data["time"].split(':'))
        arrival_time = time(hour, minute)
        patients.append({
            "name": patient_data["name"],
            "time": arrival_time,
            "status": patient_data["status"]
        })
    return patients 