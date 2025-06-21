# terminal operations manager
# frontend manager
from ERIntake import ERIntake
from datetime import time
from typing import Optional

class FrontendManager:
    def __init__(self):
        self.er_intake = ERIntake()
        self.running = True
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("🏥 HOSPITAL ER MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Patient")
        print("2. View Next Patient")
        print("3. View All Patients")
        print("4. Find Patient by Name")
        print("5. Remove Patient")
        print("6. Update Patient Status")
        print("7. Load Mock Data")
        print("8. Exit")
        print("-"*50)
    
    def get_user_choice(self) -> int:
        """Get user input for menu selection"""
        while True:
            try:
                choice = int(input("Enter your choice (1-8): "))
                if 1 <= choice <= 8:
                    return choice
                else:
                    print("❌ Please enter a number between 1 and 8")
            except ValueError:
                print("❌ Please enter a valid number")
    
    def add_patient(self):
        """Add a new patient to the queue"""
        print("\n--- ADD NEW PATIENT ---")
        
        # Get patient name
        name = input("Enter patient name: ").strip()
        if not name:
            print("❌ Patient name cannot be empty")
            return
        
        # Get arrival time
        while True:
            try:
                time_input = input("Enter arrival time (HH:MM format, e.g., 14:30): ")
                hour, minute = map(int, time_input.split(':'))
                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    arrival_time = time(hour, minute)
                    break
                else:
                    print("❌ Invalid time format. Use HH:MM (00:00-23:59)")
            except (ValueError, TypeError):
                print("❌ Invalid time format. Use HH:MM (e.g., 14:30)")
        
        # Get patient status (priority)
        while True:
            try:
                print("\nPatient Status (Priority):")
                print("1 - Critical (Highest Priority)")
                print("2 - Serious")
                print("3 - Stable")
                print("4 - Minor (Lowest Priority)")
                status = int(input("Enter status (1-4): "))
                if 1 <= status <= 4:
                    break
                else:
                    print("❌ Please enter a number between 1 and 4")
            except ValueError:
                print("❌ Please enter a valid number")
        
        # Add patient to queue
        self.er_intake.add_patient(arrival_time, name, status)
        print(f"✅ Patient '{name}' added successfully!")
    
    def view_next_patient(self):
        """Display the next patient in queue"""
        print("\n--- NEXT PATIENT ---")
        next_patient = self.er_intake.next_patient()
        
        if next_patient:
            status_names = {1: "Critical", 2: "Serious", 3: "Stable", 4: "Minor"}
            print(f"📋 Patient: {next_patient.name}")
            print(f"🏥 Status: {status_names.get(next_patient.status, 'Unknown')} (Priority: {next_patient.status})")
            print(f"⏰ Arrival Time: {next_patient.arrival_time.strftime('%H:%M')}")
        else:
            print("📭 No patients in queue")
    
    def view_all_patients(self):
        """Display all patients in queue"""
        print("\n--- ALL PATIENTS IN QUEUE ---")
        
        if not self.er_intake.patients:
            print("📭 No patients in queue")
            input("\nPress Enter to continue...")
            return
        
        status_names = {1: "Critical", 2: "Serious", 3: "Stable", 4: "Minor"}
        
        print(f"{'Position':<10} {'Name':<20} {'Status':<15} {'Arrival Time':<12}")
        print("-" * 60)
        
        # Display patients without modifying the queue
        for position, patient in enumerate(self.er_intake.patients, 1):
            status_text = f"{status_names.get(patient.status, 'Unknown')} ({patient.status})"
            print(f"{position:<10} {patient.name:<20} {status_text:<15} {patient.arrival_time.strftime('%H:%M'):<12}")
        
    
    def find_patient(self):
        """Find and display patient by name"""
        print("\n--- FIND PATIENT ---")
        name = input("Enter patient name to search: ").strip()
        
        if not name:
            print("❌ Patient name cannot be empty")
            return
        
        patient = self.er_intake.find_by_name(name)
        
        if patient:
            status_names = {1: "Critical", 2: "Serious", 3: "Stable", 4: "Minor"}
            print(f"\n✅ Patient found:")
            print(f"📋 Name: {patient.name}")
            print(f"🏥 Status: {status_names.get(patient.status, 'Unknown')} (Priority: {patient.status})")
            print(f"⏰ Arrival Time: {patient.arrival_time.strftime('%H:%M')}")
        else:
            print(f"❌ Patient '{name}' not found in queue")
    
    def remove_patient(self):
        """Remove patient from queue"""
        print("\n--- REMOVE PATIENT ---")
        name = input("Enter patient name to remove: ").strip()
        
        if not name:
            print("❌ Patient name cannot be empty")
            return
        
        # Check if patient exists first
        if self.er_intake.find_by_name(name):
            self.er_intake.remove_patient(name)
            print(f"✅ Patient '{name}' removed successfully!")
        else:
            print(f"❌ Patient '{name}' not found in queue")
    
    def update_patient_status(self):
        """Update patient status"""
        print("\n--- UPDATE PATIENT STATUS ---")
        name = input("Enter patient name: ").strip()
        
        if not name:
            print("❌ Patient name cannot be empty")
            return
        
        # Check if patient exists
        if not self.er_intake.find_by_name(name):
            print(f"❌ Patient '{name}' not found in queue")
            return
        
        # Get new status
        while True:
            try:
                print("\nNew Patient Status (Priority):")
                print("1 - Critical (Highest Priority)")
                print("2 - Serious")
                print("3 - Stable")
                print("4 - Minor (Lowest Priority)")
                new_status = int(input("Enter new status (1-4): "))
                if 1 <= new_status <= 4:
                    break
                else:
                    print("❌ Please enter a number between 1 and 4")
            except ValueError:
                print("❌ Please enter a valid number")
        
        self.er_intake.update_status(name, new_status)
        print(f"✅ Patient '{name}' status updated successfully!")
    
    def load_mock_data(self):
        """Load hardcoded mock data into the system"""
        print("\n--- LOADING MOCK DATA ---")
        
        try:
            from ERData import get_mock_patients
            
            # Clear existing patients
            self.er_intake.patients.clear()
            
            # Get mock patients
            mock_patients = get_mock_patients()
            
            # Add patients to the queue ONE AT A TIME using the heap method
            for patient_data in mock_patients:
                self.er_intake.add_patient(
                    patient_data["time"], 
                    patient_data["name"], 
                    patient_data["status"]
                )
            
            print(f"✅ Loaded {len(mock_patients)} mock patients into the system!")
            print("\n📊 Mock Data Summary:")
            print(f"   • Critical patients: {sum(1 for p in mock_patients if p['status'] == 1)}")
            print(f"   • Serious patients: {sum(1 for p in mock_patients if p['status'] == 2)}")
            print(f"   • Stable patients: {sum(1 for p in mock_patients if p['status'] == 3)}")
            print(f"   • Minor patients: {sum(1 for p in mock_patients if p['status'] == 4)}")
            print(f"   • Time range: 08:00 - 11:00")
            
        except ImportError:
            print("❌ ERData.py file not found!")
        except Exception as e:
            print(f"❌ Error loading mock data: {e}")
    
    def run(self):
        """Main application loop"""
        print("🏥 Welcome to the Hospital ER Management System!")
        
        while self.running:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == 1:
                self.add_patient()
            elif choice == 2:
                self.view_next_patient()
            elif choice == 3:
                self.view_all_patients()
            elif choice == 4:
                self.find_patient()
            elif choice == 5:
                self.remove_patient()
            elif choice == 6:
                self.update_patient_status()
            elif choice == 7:
                self.load_mock_data()
            elif choice == 8:
                print("\n👋 Thank you for using the Hospital ER Management System!")
                self.running = False
            
            if self.running:
                input("\nPress Enter to continue...")