"""Author:Chase Clayton
Date Finalized: 03/05/2025
Final Project: ClaytonEMR
This program serves as a basic Electronic Medical Record system, which can be used for entering and storing patient data"""


import tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkcalendar import DateEntry
from tkinter import Frame, Canvas
from PIL import Image, ImageTk


#Function for Save and Print Chart button.
def save_data():
    #This section of the function gets the information that has been entered in each widget
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    gender = gender_combobox.get()
    age = age_spinbox.get()
    dob = dob_picker.get()
    ethnicity_race = ethnicity_combobox.get()
    insurance_Status = insurance_check_var.get()
    insurance_provider = insuranceProvider_combobox.get()
    memberID = memberID_entry.get()
    homeAddress = homeAddress_entry.get()
    homeState = homeState_combobox.get()
    phoneNumber = phoneNumber_entry.get()
#This section prints each gathered data point from the widgets
    print("Patient name: ", first_name, last_name, "Gender: ", gender,)
    print("Ethnicity/Race: ", ethnicity_race, "DOB: ", dob, "Age: ", age)
    print("Insurance Status: ", insurance_Status)
    print("Insurance Provider: ", insurance_provider, "Member ID: ", memberID)
    print("Home Address: ", homeAddress, "State: ", homeState, "Phone Number: ", phoneNumber)
    print("----------------------------------------------------------------------------------")
()

#function that operates the Discard and Clear Changes button
#This function uses a for loop to clear all entered data out of each widget in list of widges
def clear_data():
     widgets = (first_name_entry, last_name_entry, gender_combobox, age_spinbox, dob_picker, 
               ethnicity_combobox, insuranceProvider_combobox, memberID_entry,
               homeAddress_entry, homeState_combobox, phoneNumber_entry)
     for widget in widgets:
          widget.delete(0, tkinter.END)
          ()

#Function for Exit EMR button which ends program
def exit_EMR():
    exit()
    ()

#Function for creating a note
def chart_note():
    noteWindow = tkinter.Toplevel()
    noteWindow.title("Chart Note")
    tkinter.Label(noteWindow, text="Chart Note").pack()
    text_box = tkinter.Text(noteWindow, height=50, width=100)
    text_box.pack()
    

#Main window, titled Clayton EMR - name of the EMR system
window = tkinter.Tk()
window.title("Clayton EMR")

label=tkinter.Label(window)
label.pack

#Patient Information frame for identifying demographics
frame = tkinter.Frame(window)
frame.pack()

#sets frame to be labeled Patient Information
patient_info_frame = tkinter.LabelFrame(frame, text="Patient Information")
patient_info_frame.grid(row= 0, column =0, padx=20, pady=20)

#Sets labels for First Name and Last Name fields
first_name_label = tkinter.Label(patient_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(patient_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

#Sets Entry widgets for entering Patient first anem and last name
first_name_entry = tkinter.Entry(patient_info_frame)
last_name_entry = tkinter.Entry(patient_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

#Sets Label 'Gender' for combobox which will select gender options
gender_label= tkinter.Label(patient_info_frame, text="Gender")
#Combobox set up, including values which will appear in drop-down list
gender_combobox = ttk.Combobox(patient_info_frame, values=["Male", "Female", "Transgender"])
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=1, column=2)

#Sets Label 'Age' and spinbox allowing ages 1 to 110 to be selected
age_label = tkinter.Label(patient_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(patient_info_frame, from_=1, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

#Sets 'Date of Birth' Label
dob_label = tkinter.Label(patient_info_frame, text="Date of Birth")
dob_label.grid(row=2, column=1)
#DateEntry calendar widget, imported from tkcalendar
dob_picker = DateEntry(patient_info_frame, text="Date of Birth")
dob_picker.grid(row=3, column=1)

#Sets label 'Ethnicity/Race'
ethnicity_label = tkinter.Label(patient_info_frame, text="Ethnicity/Race")
#Combobox with values for choosing patient ethnicity/race
ethnicity_combobox = ttk.Combobox(patient_info_frame, values=["White", "African American", "American Indian", "Hispanic/Latino", "Pacific Islander"])
ethnicity_label.grid(row=2, column=2)
ethnicity_combobox.grid(row=3, column=2)

#sets padding options which will apply to all widgets inside patient_info_frame grid
for widget in patient_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Demographic/extra patient information frame
demographics_frame = tkinter.LabelFrame(frame)
demographics_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

#Sets label for 'Insurance Status'
insurance_label = tkinter.Label(demographics_frame, text="Insurance Status")
#Sets check button for 'Active Insurance' to check if listed insurance info is currently active for member or not
#These variables are used choose a print statement during save_data function reflected off status of check button
#There is validation for if the button has not been pressed, to account for default empty selection
insurance_check_var = tkinter.StringVar(value="Insurance Status unconfirmed.")
insurance_check = tkinter.Checkbutton(demographics_frame, text="Active Insurance", 
                                      variable=insurance_check_var, onvalue= "Member has Active Insurance", offvalue="Member does not have Active Insurance")
insurance_label.grid(row=0, column=0)
insurance_check.grid(row=1, column=0)

#Sets label for 'Insurance Provider' combobox
insuranceProvider_label = tkinter.Label(demographics_frame, text="Insurance Provider")
#Sets combobox for a list of Insurance Providers which are accepted by Care Center
insuranceProvider_combobox = ttk.Combobox(demographics_frame, values=["Traditional Medicaid", "Anthem", "MdWise", "MHS", "CareSource"])
insuranceProvider_label.grid(row=0, column=1)
insuranceProvider_combobox.grid(row=1, column=1)

#Sets label for 'Member ID' field
memberID_label = tkinter.Label(demographics_frame, text="Member ID")
memberID_label.grid(row=0, column=3)
#Entry field for 'Member ID' which will store Insurance plan ID number
memberID_entry = tkinter.Entry(demographics_frame)
memberID_entry.grid(row=1, column=3)

#sets padding options which will apply to all widgets inside demographics_frame
for widget in demographics_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#sets frame to be labeled 'Contact Information'
contact_info_frame = tkinter.LabelFrame(frame, text="Contact Information")
contact_info_frame.grid(row= 2, column =0, sticky="news", padx=20, pady=20)

#sets label for 'Home Address' field
homeAddress_label = tkinter.Label(contact_info_frame, text="Home Address")
homeAddress_label.grid(row=0, column=0)
#Entry field for Home Address information
homeAddress_entry = tkinter.Entry(contact_info_frame)
homeAddress_entry.grid(row=1, column=0)

#Sets label for 'State' field
homeState_label = tkinter.Label(contact_info_frame, text="State")
homeState_label.grid(row=0, column=1)
#Sets combobox for list of 50 US states
homeState_combobox = ttk.Combobox(contact_info_frame, values=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])
homeState_combobox.grid(row=1, column=1)

#Sets label for 'Phone Number' field
phoneNumber_label = tkinter.Label(contact_info_frame, text="Phone Number (XXX-XXX-XXXX)")
phoneNumber_label.grid(row=0, column=2)
#Sets Entry field for phone number
phoneNumber_entry = tkinter.Entry(contact_info_frame)
phoneNumber_entry.grid(row=1, column=2)

#sets padding options which will apply to all widgets inside contact_info frame
for widget in contact_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Button for clearing all fields of entered data without saving
discardChart = tkinter.Button(frame, text="Discard and Clear Changes", command = clear_data)
discardChart.grid(row=3, column=0, sticky="news", padx=20, pady=10)

#Button for saving entered data
saveChart = tkinter.Button(frame, text="Save and Print Chart",command= save_data)
saveChart.grid(row=4, column=0, sticky="news", padx=20, pady=10)

#Button for exiting system
exitChart = tkinter.Button(frame, text="Exit ClaytonEMR", command=exit_EMR)
exitChart.grid(row=5, column=0,sticky="news", padx=20, pady=10) 

createNote = tkinter.Button(frame, text="Create Note", command=chart_note)
createNote.grid(row=6, column=0,sticky="news", padx=20, pady=10) 

window.mainloop()