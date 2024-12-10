from tkinter import *
from captcha.image import ImageCaptcha
from tkinter import messagebox
import os

def addNumbers():
    a = u.get()
    b = p.get()
    ca = c.get()

    # Generate the captcha image
    image_info = ImageCaptcha(width=250, height=100)
    captcha_text = 'snjb'
    image_file = 'abc.png'
    
    # Ensure the captcha image is written before using it
    image_info.write(captcha_text, image_file)

    if a == 'test' and b == '1234':
        if ca == captcha_text:
            messagebox.showinfo("showinfo", "Login successfully")
        else:
            messagebox.showinfo("showinfo", "Login Failed")
    else:
        messagebox.showinfo("showinfo", "Login Failed")

    # Now we load the image into the Tkinter canvas
    img = PhotoImage(file=image_file)
    canvas.create_image(20, 20, anchor=NW, image=img)
    canvas.img = img  # Keep a reference to avoid garbage collection

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

l1 = Label(root, text="Username")
l1.config(font=("Courier", 14))

u = Entry(root)

l2 = Label(root, text="Password")
l2.config(font=("Courier", 14))

p = Entry(root)

l3 = Label(root, text="Captcha")
l3.config(font=("Courier", 14))

c = Entry(root)

b2 = Button(root, text="Login", command=addNumbers)

l1.pack()
u.pack()
l2.pack()
p.pack()
l3.pack()
c.pack()
b2.pack()

mainloop()
