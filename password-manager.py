from tkinter import *
#------------Password Generator------------#

#--------------Save Password---------------#

#----------------UI Setup------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70) #added padding

canvas = Canvas(height=200, width=200) #creating the canvas with the specific dimensions
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) #addidng the image to the canvas with the x/y position
canvas.grid(row=0, column=1) #this is where the image will be in the page

#Labels
web_label = Label(text="Website:") #website label
web_label.grid(row=1, column=0) #label position for website
email_label = Label(text="Username/Email:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

#Entries
web_entry = Entry(width=35)#entry for website
web_entry.grid(row=1, column=1, columnspan=2)#position of the entry bar
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

#Buttons
create_password_button = Button(text="Generate Password")#creates button that generates password
create_password_button.grid(row=3, column=2)#position of the button
add_button = Button(text="Add Password", width=36)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()