#TODO:-
#   *make the main window of gui ✅
#   *add widgets to the window ✅
#   *make the generate file and function ✅
#   *connect with generate files and output results
#   *make the style of the main window more good

#Importing Libraries
from tkinter import *
import generate
from tkinter import messagebox
#maek the main variables
user_name = ""
#make the send function
def send_data():
    f_name = f_name_e.get()
    l_name = l_name_e.get()
    if f_name == "" or l_name == "":
        messagebox.showerror("Error", "Please enter your first and last name")
    else:
        user_name = generate.generate(f_name, l_name)
        print(user_name)

        user_name = str(user_name)
        print(user_name)
        user_name_l.config(text=f"user name: {user_name}")
        
#make the root of the app
root = Tk()
root.title("user name Generator")
root.geometry("400x400+550+200")
root.resizable(False, False)

#make the widgets
#frist name label

f_name_l = Label(root, text="First Name: ", font="arial 15",)
f_name_l.place(x=10, y=50)

#last name label

l_name_l = Label(root, text="last Name: ", font="arial 15")
l_name_l.place(x=10, y=150)

#First name entry

f_name_e = Entry(root, width=20, font="arial 15")
f_name_e.place(x=125, y=50)

#last name entry

l_name_e = Entry(root, width=20, font="arial 15")
l_name_e.place(x=125, y=150)


#make the button
generate_button = Button(root, text="Generate", font="arial 15",command=send_data)
generate_button.place(x=150, y=230)
#make the user name label
user_name_l = Label(root, text=f"user name: {user_name}", font="arial 15")
user_name_l.place(x=10, y=300)


root.mainloop()
