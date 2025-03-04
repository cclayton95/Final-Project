import tkinter as tk
from tkinter import messagebox, ttk

# Main Application Class
class EHRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Electronic Health Record System")
        self.create_main_menu()
        self.patient_records = []  # Store patient records

    def create_main_menu(self):
        """Creates the main menu with options to search or create new patient records."""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        label = tk.Label(self.root, text="Welcome to the EHR System", font=("Arial", 16))
        label.pack(pady=20)
        
        search_button = tk.Button(self.root, text="Search Existing Patient Records", command=self.search_patient)
        search_button.pack(pady=10)
        
        create_button = tk.Button(self.root, text="Create New Patient Record", command=self.create_patient)
        create_button.pack(pady=10)
    
    def search_patient(self):
        """Opens the patient search window."""
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Patient Records")
        
        tk.Label(search_window, text="Search by First Name:").pack()
        first_name_entry = tk.Entry(search_window)
        first_name_entry.pack()
        
        tk.Label(search_window, text="Search by Last Name:").pack()
        last_name_entry = tk.Entry(search_window)
        last_name_entry.pack()
        
        tk.Label(search_window, text="Search by DOB (mm/dd/yyyy):").pack()
        dob_entry = tk.Entry(search_window)
        dob_entry.pack()
        
        search_button = tk.Button(search_window, text="Search", command=lambda: self.perform_search(first_name_entry.get(), last_name_entry.get(), dob_entry.get()))
        search_button.pack(pady=10)
    
    def perform_search(self, first_name, last_name, dob):
        """Searches for patients based on input criteria."""
        matches = [p for p in self.patient_records if (p['first_name'] == first_name or p['last_name'] == last_name or p['dob'] == dob)]
        if matches:
            messagebox.showinfo("Search Result", f"Found {len(matches)} record(s)")
        else:
            messagebox.showinfo("Search Result", "No records found")
    
    def create_patient(self):
        """Opens the patient creation form."""
        create_window = tk.Toplevel(self.root)
        create_window.title("Create New Patient Record")
        
        # Entry Fields
        fields = {
            "First Name": tk.Entry(create_window),
            "Last Name": tk.Entry(create_window),
            "Diagnosis 1": tk.Entry(create_window),
            "Diagnosis 2": tk.Entry(create_window),
            "Diagnosis 3": tk.Entry(create_window),
            "Birthdate (mm/dd/yyyy)": tk.Entry(create_window),
            "Street Address": tk.Entry(create_window),
            "City": tk.Entry(create_window)
        }
        
        row = 0
        for label, entry in fields.items():
            tk.Label(create_window, text=label).grid(row=row, column=0)
            entry.grid(row=row, column=1)
            row += 1
        
        # Gender Selection
        tk.Label(create_window, text="Gender:").grid(row=row, column=0)
        gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(create_window, text="Male", variable=gender_var, value="Male").grid(row=row, column=1)
        tk.Radiobutton(create_window, text="Female", variable=gender_var, value="Female").grid(row=row, column=2)
        tk.Radiobutton(create_window, text="Transgender", variable=gender_var, value="Transgender").grid(row=row, column=3)
        row += 1
        
        # Marital Status
        tk.Label(create_window, text="Marital Status:").grid(row=row, column=0)
        marital_status = ttk.Combobox(create_window, values=["Single", "Married", "Widowed", "Separated"])
        marital_status.grid(row=row, column=1)
        row += 1
        
        # State Dropdown
        tk.Label(create_window, text="State:").grid(row=row, column=0)
        state_var = ttk.Combobox(create_window, values=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])
        state_var.grid(row=row, column=1)
        row += 1
        
        # Save Button
        save_button = tk.Button(create_window, text="Save", command=lambda: self.save_patient(fields, gender_var.get(), marital_status.get(), state_var.get()))
        save_button.grid(row=row, column=1, pady=10)
    
    def save_patient(self, fields, gender, marital_status, state):
        """Validates and saves the patient record."""
        patient_data = {label: entry.get() for label, entry in fields.items()}
        if not all(patient_data.values()) or not gender or not marital_status or not state:
            messagebox.showerror("Error", "All fields must be filled.")
        else:
            patient_data.update({"Gender": gender, "Marital Status": marital_status, "State": state})
            self.patient_records.append(patient_data)
            messagebox.showinfo("Success", "Patient record saved.")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = EHRApp(root)
    root.mainloop()

