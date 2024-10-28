import tkinter as bot
from tkinter import ttk

# Initialize main window
rootwindow = bot.Tk()
rootwindow.geometry('400x300')
rootwindow.configure(background='coral')
rootwindow.title('Employee Management System Login')

def enterbuttonthing():
    if passwordentry.get() == 'password': 
        opennewscreen()
    else:
        errorlabel.config(text="Incorrect password", fg='red')

# Open main application window
def opennewscreen():
    rootwindow.withdraw() 

    # Initialize new window
    newwindow = bot.Toplevel(rootwindow)
    newwindow.title("Employee Management System")
    newwindow.geometry("1400x800")
    newwindow.configure(background='coral')

    # Frame for input section
    labelframeinput = bot.LabelFrame(newwindow, text='Input', font=('arial', 15, 'italic'), background='light blue')
    labelframeinput.pack(fill='both', expand='yes', padx=10, pady=10)

    # Frame for operations section
    labelframeoperation = bot.LabelFrame(newwindow, text='Operation', font=('arial', 15, 'italic'), background='light blue')
    labelframeoperation.pack(fill='both', expand='yes', padx=10, pady=10)

    # Frame for output display
    labeloutput = bot.LabelFrame(newwindow, text='Output', font=('arial', 15, 'italic'), background='lightblue')
    labeloutput.pack(fill='both', expand='yes', padx=10, pady=10)

    # Initialize lists to store employee data
    listemployename = []
    listID = []
    listdesignation = []
    listmailID = []
    listsalary = []
    listnum = []

    # Function to add employee record to file and display success message
    def configmsg():
        employename = employenameentry.get()
        employeID = employeIDentry.get()
        employedesignation = employedesignationentry.get()
        employemailID = employemailIDentry.get()
        employesalary = employesalaryentry.get()
        employenumber = employenumberentry.get()

        # Append details to lists
        listemployename.append(employename)
        listID.append(employeID)
        listdesignation.append(employedesignation)
        listmailID.append(employemailID)
        listsalary.append(employesalary)
        listnum.append(employenumber)

        # Save to file
        with open('home\passwordprogram.txt', 'a') as f:
            f.write(f"{employename},{employeID},{employedesignation},{employemailID},{employesalary},{employenumber}\n")

        # Update success message label
        statusmsg = f"Added: {employename}, {employeID}, {employedesignation}, {employemailID}, {employesalary}, {employenumber}"
        labelsucessmessage.config(text=statusmsg)

    # Function to display all employee records in the Treeview
    def displayall():
        treeviewdisplay.delete(*treeviewdisplay.get_children()) 
        with open('home\passwordprogram.txt', 'r') as f:
            for line in f:
                treeviewdisplay.insert('', 'end', values=line.strip().split(','))

    # Input Frame for Employee Details
    imputemployedetails = bot.LabelFrame(labelframeinput, text='Employee Details', font=('arial', 15, 'italic', 'underline'), background='light green')
    imputemployedetails.pack(side=bot.LEFT, fill='both', expand='yes', padx=10, pady=10)

    # Labels and Entries for Employee Details
    employename = bot.Label(imputemployedetails, text='Enter Employee Name :', font=('arial', 15, 'bold'), background='light green')
    employename.grid(row=0, column=0)
    employenameentry = bot.Entry(imputemployedetails, font=('arial', 15, 'bold'))
    employenameentry.grid(row=0, column=1)

    employeID = bot.Label(imputemployedetails, text='Enter Employee ID :', font=('arial', 15, 'bold'), background='light green')
    employeID.grid(row=1, column=0)
    employeIDentry = bot.Entry(imputemployedetails, font=('arial', 15, 'bold'))
    employeIDentry.grid(row=1, column=1)

    employedesignation = bot.Label(imputemployedetails, text='Enter Employee Designation :', font=('arial', 15, 'bold'), background='light green')
    employedesignation.grid(row=2, column=0)
    employedesignationentry = bot.Entry(imputemployedetails, font=('arial', 15, 'bold'))
    employedesignationentry.grid(row=2, column=1)

    employemailID = bot.Label(imputemployedetails, text='Enter Employee Mail ID :', font=('arial', 15, 'bold'), background='light green')
    employemailID.grid(row=3, column=0)
    employemailIDentry = bot.Entry(imputemployedetails, font=('arial', 15, 'bold'))
    employemailIDentry.grid(row=3, column=1)

    # Input Frame for Employee Contact Details
    imputemployecontact = bot.LabelFrame(labelframeinput, text='Employee Contact Details', font=('arial', 15, 'italic', 'underline'), background='light green')
    imputemployecontact.pack(side=bot.LEFT, fill='both', expand='yes', padx=10, pady=10)

    # Labels and Entries for Contact Details
    employesalary = bot.Label(imputemployecontact, text='Enter Employee Salary :', font=('arial', 15, 'bold'), background='light green')
    employesalary.grid(row=1, column=0)
    employesalaryentry = bot.Entry(imputemployecontact, font=('arial', 15, 'bold'))
    employesalaryentry.grid(row=1, column=1)

    employenumber = bot.Label(imputemployecontact, text='Enter Employee Ph. No. :', font=('arial', 15, 'bold'), background='light green')
    employenumber.grid(row=2, column=0)
    employenumberentry = bot.Entry(imputemployecontact, font=('arial', 15, 'bold'))
    employenumberentry.grid(row=2, column=1)

    # Buttons for Operations
    buttonconfigureall = bot.Button(labelframeoperation, text='Configure', font=('arial', 15, 'bold'), background='orange', command=configmsg)
    buttonconfigureall.grid(row=0, column=0, padx=10, pady=10)

    buttondisplayall = bot.Button(labelframeoperation, text='Display All', font=('arial', 15, 'bold'), background='orange', command=displayall)
    buttondisplayall.grid(row=0, column=1, padx=10, pady=10)

    # Success Message
    labelsucessmessage = bot.Label(labelframeoperation, text='', font=('arial', 15, 'bold'), background='light green')
    labelsucessmessage.grid(row=0, column=2, padx=10, pady=10)

    # Treeview Display
    treeviewdisplay = ttk.Treeview(labeloutput, columns=(1, 2, 3, 4, 5, 6), show='headings', height=8)
    headings = ["Employee Name", "Employee ID", "Employee Designation", "Employee Mail ID", "Employee Salary", "Employee Ph. No."]
    for i, heading in enumerate(headings, 1):
        treeviewdisplay.heading(i, text=heading)
    treeviewdisplay.pack(fill='both', expand='yes', padx=10, pady=10)

# Login Screen Elements
labelheading = bot.Label(rootwindow, text='Enter password:', font=('arial', 15, 'bold'), background='coral')
labelheading.pack()

passwordentry = bot.Entry(rootwindow, font=('arial', 15, 'bold'), foreground='black', show="*")
passwordentry.pack(padx=10, pady=10)

enterbutton = bot.Button(rootwindow, text='Enter', font=('arial', 15, 'bold'), background='orange', command=enterbuttonthing)
enterbutton.pack()

errorlabel = bot.Label(rootwindow, text='', font=('arial', 12), background='coral', fg='red')
errorlabel.pack()

rootwindow.mainloop()
