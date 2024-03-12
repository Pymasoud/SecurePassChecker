from checkmypass import main
import tkinter as tk

# ----- This works ---------
# check = main("345hey")
# print(check)
"""
   so now i can use main() with the input from tkinter
   but i need to work out a function that gets the password
   from the password stringvar and configure the output label
   so that it displays the messages from main() 
"""

root = tk.Tk()
root.geometry("600x400")
root.title("Check My Pass!")
root.configure(background="#333")

# Functions ------------------------------------------------------
def check_password(*args, **kwargs):
   pword = password.get()
   check = main(pword)
   output_label.config(text=check)
   
# top frame -----------------------------------------
top_frame = tk.Frame(root, background="#444", padx=90)
top_frame.pack(side="top")

# bottom frame ---------------------------------------------------
bottom_frame = tk.Frame(root, background="#444", padx=200, pady=50)
bottom_frame.pack(side="bottom", pady=20)

password = tk.StringVar()

# ===============================================================
# In the top framew
password_label = tk.Label(top_frame, text="Enter your Password: ")
password_label.pack(pady=30, padx=20)
password_label.config(font=("Arial", 20))

password_input = tk.Entry(top_frame, textvariable=password, width=50)
password_input.pack(pady=10, ipady=10)
password_input.config(font=("Arial", 20))

check_btn = tk.Button(top_frame, text="Check Password", command=check_password)
check_btn.pack(padx=10, pady=10)
check_btn.config(font=("Arial", 12))

# ===================================================================
# In the bottom frame
output_label = tk.Label(bottom_frame, text="Output",background="#444", foreground="#fff",padx=90, pady=10)
output_label.pack()
output_label.config(font=("Arial", 12))

root.mainloop()