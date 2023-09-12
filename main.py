from tkinter import *
from tkinter import messagebox
import random
import json

DARK = "#001C30"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.delete(0, END)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            'email': email,
            'password': password,
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="OOPS", message="Some fields are empty! Please fill in all information.")
    else:
        try:
            with open("data.json", "r") as data:
                #Reading old data
                read_data = json.load(data)
                #Updating old data with new data
                read_data.update(new_data)

            with open("data.json", "w") as data:            
                #Saving updated data
                json.dump(read_data, data, indent=4)
        except:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
# ---------------------------- SEARCH INFO ------------------------------- #
def search_info():
    website = website_entry.get().title()

    with open("data.json", "r") as data:
        read_data = json.load(data)
        try:
            if read_data[website]:
                messagebox.showinfo(title=f"{website}", message=f"Email: {read_data[website]['email']}\nPassword: {read_data[website]['password']}")
        except KeyError:
            messagebox.showerror(title="Data Not Found", message="No Data found with that Website name.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=DARK)

canvas = Canvas(width=200, height=200, bg=DARK, highlightthickness= 0)
#bg_image = PhotoImage(file="..\img\logo.png")
bg_image = PhotoImage(file="img\logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1,row=0)

#Label
website_label = Label(text="Website:", bg=DARK, fg="white")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=DARK, fg="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=DARK, fg="white")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=55)
email_entry.insert(END, "123@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

#Buttons
search_ = Button(text="Search", width=14, font=("Arial", 10), command=search_info)
search_.grid(column=2, row=1)

generate_password = Button(text="Generate Password", font=("Arial", 10), command=gen_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=46, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()