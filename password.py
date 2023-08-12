import string
import random
from tkinter import *

# Create the main window
Screen = Tk()
Screen.geometry("700x600")
Screen.title("Password Generator")

# Center the window on the screen
Screen.eval('tk::PlaceWindow . center')

# Function to be executed when a radio button is selected
def SelectionOptions():
    pass  # Placeholder for future functionality

# Label for the title
Label(Screen, text="Welcome! Create Your Password Here", font=("Montserrat Classic", 16, "bold")).pack(anchor=CENTER, padx=10, pady=(20, 0))

# Radio buttons for password strength selection
Choice = IntVar()
RadioButton1 = Radiobutton(Screen, text="POOR", variable=Choice, value=1, command=SelectionOptions)
RadioButton2 = Radiobutton(Screen, text="AVERAGE", variable=Choice, value=2, command=SelectionOptions)
RadioButton3 = Radiobutton(Screen, text="STRONG", variable=Choice, value=3, command=SelectionOptions)
RadioButton1.pack(anchor=CENTER, padx=10, pady=5)
RadioButton2.pack(anchor=CENTER, padx=10, pady=5)
RadioButton3.pack(anchor=CENTER, padx=10, pady=5)

# Label for password length selection
LengthLabel = StringVar()
LengthLabel.set("Password Length")
LengthTitle = Label(Screen, textvariable=LengthLabel).pack(anchor=CENTER, padx=10, pady=5)

# Spinbox for selecting password length
Value = IntVar()
SpinLength = Spinbox(Screen, from_=9, to_=25, textvariable=Value, width=14)
SpinLength.pack(anchor=CENTER, padx=10, pady=5)

# Define character sets for password generation
Poor = string.ascii_uppercase + string.ascii_lowercase
Average = string.ascii_uppercase + string.ascii_lowercase + string.digits
Symbols = """~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/ """
Advance = Poor + Average + Symbols

# Initialize an empty list for password history
password_history = []

# Function to generate a password based on user's choices
def PassGen():
    selected_strength = Choice.get()
    password_length = Value.get()

    if selected_strength == 1:
        password = "".join(random.sample(Poor, password_length))
    elif selected_strength == 2:
        password = "".join(random.sample(Average, password_length))
    elif selected_strength == 3:
        password = "".join(random.sample(Advance, password_length))

    # Add the generated password to history list
    password_history.append(password)
    return password

# Label for displaying the new password
Label(Screen, text="New Password:", font=("Times New Roman", 1, "bold")).pack(anchor=CENTER, padx=10, pady=(20, 0))

# Text widget for displaying the new password
Lsum = Text(Screen, height=6, width=40)
Lsum.pack(anchor=CENTER, padx=10, pady=5)

# Label for displaying password history
Label(Screen, text="Password History:", font=("Times New Roman", 18, "bold")).pack(anchor=CENTER, padx=10, pady=5)

# Listbox widget for displaying password history
history_listbox = Listbox(Screen, height=6, width=40)
history_listbox.pack(anchor=CENTER, padx=10, pady=5)

# Function to update the UI when the "Generate Password" button is clicked
def CallBack():
    password = PassGen()
    
    # Clear existing content in the text widget
    Lsum.delete("1.0", END)
    # Insert the generated password
    Lsum.insert(END, password)
    Lsum.tag_configure("new_password", foreground="green")  # Configure tag for highlighting

    # Highlight the new password using the "new_password" tag
    Lsum.tag_add("new_password", "1.0", "end")

    # Update the password history listbox
    history_listbox.delete(0, END)
    for item in password_history:
        history_listbox.insert(END, item)

    # Highlight the passwords in the history list using the "new_password" tag
    for idx, item in enumerate(password_history):
        history_listbox.itemconfig(idx, {'fg': 'red'})

# Button to generate a new password
PassGenButton = Button(Screen, text="Generate Password", bd=5, height=2, command=CallBack, pady=3)
PassGenButton.pack(anchor=CENTER, padx=10, pady=(20, 0))

# Start the Tkinter event loop
Screen.mainloop()
