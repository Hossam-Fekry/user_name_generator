#TODO:-
#   *make the main window of gui ✅
#   *add widgets to the window ✅
#   *connect with backend 
#   *make the style of the main window more good

#Importing Libraries
from tkinter import *
import generate

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
generate_button = Button(root, text="Generate", font="arial 15",)
generate_button.place(x=150, y=230)


root.mainloop()
