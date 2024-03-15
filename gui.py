from checkmypass import main
import tkinter as tk
from typing import List

# test comment

"""
   so now i can use main() with the input from tkinter
   but i need to work out a function that gets the password
   from the password stringvar and configure the output label
   so that it displays the messages from main() 
"""

root = tk.Tk()
root.geometry("900x350")
root.title("Check My Pass!")
root.configure(background="#333")

# Functions ------------------------------------------------------
def check_password(*args, **kwargs) -> None:
    pword = password.get()
    result = main([pword])[0].strip('{}')
    output_label.config(text=result)
# top frame -----------------------------------------
top_frame = tk.Frame(root, background="#444", padx=10)
top_frame.pack(side="top")

# bottom frame ---------------------------------------------------
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom")

password = tk.StringVar()

# ===============================================================
# In the top frame
password_label = tk.Label(top_frame, text="Enter your Password: ")
password_label.pack(pady=30, padx=20)
password_label.config(font=("Arial", 20))

password_input = tk.Entry(top_frame, textvariable=password, width=50)
password_input.pack(pady=10, ipady=10)
password_input.config(font=("Arial", 20))
password_input.focus()

message_label = tk.Label(top_frame, text="Click button or press ENTER")
message_label.pack()
check_btn = tk.Button(top_frame, text="Check Password", command=check_password, background="#333", foreground="chartreuse")
check_btn.pack(padx=10, pady=10)
check_btn.config(font=("Arial", 12))

# ===================================================================
# In the bottom frame
output_label = tk.Label(bottom_frame, background="#333", foreground="#fff", pady=40)
output_label.pack()
output_label.config(font=("Arial", 12))

# bind the enter key to enter button
password_input.bind("<Return>", lambda event=None: check_password())

root.mainloop()
