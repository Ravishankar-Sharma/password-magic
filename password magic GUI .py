import string
import random
from tkinter import *


def generate_password():
    try:
        plen = int(length_entry.get())
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        password = "".join(random.sample(s, plen))
        password_label.config(text=password)
    except ValueError:
        password_label.config(text="Invalid input")

root = Tk()
root.title("P@sSwoRd M@gIc")
root.geometry("300x330")
length_label = Label(root, text=" Password length:")
length_entry = Entry(root,bg="white",fg="darkgreen")
generate_button = Button(root, text="Generate Password", command=generate_password)
password_label = Label(root, text="")

length_label.pack()
length_entry.pack()
generate_button.pack()
password_label.pack()

root.mainloop()
