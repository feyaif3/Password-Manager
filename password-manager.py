from tkinter import *
#------------Password Generator------------#

#--------------Save Password---------------#

#----------------UI Setup------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20) #added padding

canvas = Canvas(height=300, width=300) #creating the canvas with the specific dimensions
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img) #addidng the image to the canvas with the x/y position
canvas.grid(row=0, column=1) #this is where the image will be in the page

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = Label(text="Username/Email:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

#Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

#Buttons
create_password_button = Button(text="Generate Password")
create_password_button.grid(row=3, column=2)
add_button = Button(text="Add Password")
add_button.grid(row=4, column=1)
window.mainloop()