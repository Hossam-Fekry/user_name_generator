#import modules

import random
from tkinter import messagebox

def generate(f_name, l_name):
    #generate the username
    number = random.randrange(0,999)
    final_user_name = str(f_name) + str(l_name) + str(number)

    messagebox.showinfo("your user name", final_user_name)