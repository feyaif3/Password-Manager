from tkinter import *
#------------Password Generator------------#

#--------------Save Password---------------#

#----------------UI Setup------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20) #added padding

canvas = Canvas(height=500, width=500) #creating the canvas with the specific dimensions#
logo_img = PhotoImage(file="logo.png")
canvas.create_image(250, 250, image=logo_img) #addidng the image to the canvas with the x/y position#
canvas.pack()

#Labels
web_label = Label(text="Website")
email_label = Label(text="Username/Email")
pass_label = Label(text="Password")

window.mainloop()