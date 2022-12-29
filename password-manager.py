from tkinter import *
from tkinter import messagebox
#------------Password Generator------------#

#--------------Save Password---------------#

def add():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    
    if len(website) == 0 or len(password) == 0: #added validation so no entries are left empty
        messagebox.showinfo(title="Error", message="Please add details to the empty fields.")
    
    is_ok = messagebox.askokcancel(title=Website, message=f"Details entered:\n Email:{email} "
                                                    f"\nPassword: {password} \nIs thsi correct?")
    if is_ok:
        with open("password.txt", "a") as password_file: #this will create an open a txt file
            password_file.write(f"{website} | {email} | {password}\n") #this is the format that the text file will save data in
            web_entry.delete(0, END) #this deletes what's in the entry when add button is clicked.
            email_entry.delete(0, END)
            pass_entry.delete(0, END)
            
#----------------UI Setup------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10) #added padding

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
web_entry = Entry(width=43)#entry for website
web_entry.grid(row=1, column=1, columnspan=2)#position of the entry bar
web_entry.focus()#user can start typing without clicking web entry bar
email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
#email_entry.insert(0, "useremail@mail.com")-- (This is used to autofil email)
pass_entry = Entry(width=27)
pass_entry.grid(row=3, column=1)

#Buttons
create_password_button = Button(text="Create Password")#creates button that generates password
create_password_button.grid(row=3, column=2)#position of the button
add_button = Button(text="Add Password", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()