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

# top frame --------------------------------
top_frame = tk.Frame(root, background="#333")
top_frame.pack(side="top")

# bottom frame ---------------------------------------------------
bottom_frame = tk.Frame(root, background="#333", padx=200, pady=50)
bottom_frame.pack(side="bottom", pady=10)

password = tk.StringVar()
# ===============================================================
# In the top frame
password_label = tk.Label(top_frame, text="Enter your Password: ")
password_label.pack()
password_input = tk.Entry(top_frame, textvariable=password)
password_input.pack()

# ===================================================================
# In the bottom frame
output_label = tk.Label(bottom_frame, text="Output", background="#444", foreground="#fff",padx=20, pady=20)
output_label.pack()

root.mainloop()