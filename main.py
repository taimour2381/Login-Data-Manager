import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():

    list_char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
          "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
          "!", "@", "#", "$", "%", "&", "*", "(", ")", "+", "_", "-"]
    password = []
    for n in range(2):
        n = random.choice(list_char[0:26])
        password.append(n)
    for b in range(3):
        b = random.choice(list_char[0:26])
        password.append(b.lower())
    for v in range(3):
        v = random.choice(list_char[26:36])
        password.append(v)
    for c in range(2):
        c = random.choice(list_char[36:])
        password.append(c)
    random.shuffle(password)
    entry3.insert(0, "".join(password))
    pyperclip.copy("".join(password))


def save_data():
    A = entry1.get()
    B = entry2.get()
    C = entry3.get()
    new_dict = {A: {"Email": B, "Password": C}}
    if len(A) == 0 and len(B) == 0 and len(C) == 0:
        messagebox.showerror(title="Error", message="Website/Email/Password field(s) empty!")
    else:
        prompt = messagebox.askokcancel(title="Confirmation", message=f"Are you sure you want to save the credentials?"
                                                                      f"\nWebsite: {A}\nEmail:{B}\nPassword: {C}")
        if prompt:
            try:
                with open("./data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("./data.json", mode="w") as data_file:
                    json.dump(new_dict, data_file, indent=4)
            else:
                data.update(new_dict)
                with open("./data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)


def search():
    A = entry1.get()
    with open("./data.json", mode="r") as data_file:
        data = json.load(data_file)
        if A in data:
            messagebox.showinfo(title=A, message=f"Data for {A} already exist."
                                                          f"\nUsername: {data[A]['Email']}"
                                                          f"\nUsername: {data[A]['Password']}")
        else:
            messagebox.showerror(title="No Data Found", message=f"No username/password found for {A}")


window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)
image = PhotoImage(file="./logo.png")
canvas = Canvas()
canvas.config(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.place(x=125, y=75)

prog_label = Label()
prog_label.config(text="MY PASSWORD MANAGER", font=("Courier", 25, "bold"), fg="red")
prog_label.place(x=40, y=30)

label1 = Label()
label1.config(text="Website or Service: ", font=("Arial", 11, "normal"), fg="black")
label1.place(x=20, y=275)

label2 = Label()
label2.config(text="Username/Email: ", font=("Arial", 11, "normal"), fg="black")
label2.place(x=34, y=300)

label3 = Label()
label3.config(text="Password: ", font=("Arial", 11, "normal"), fg="black")
label3.place(x=77, y=325)

entry1 = Entry()
entry1.focus()
entry1.place(x=160, y=275)

entry2 = Entry()
entry2.config(width=41)
entry2.place(x=160, y=300)

entry3 = Entry()
entry3.place(x=160, y=325)

generate_button = Button()
generate_button.config(text="Generate Password", width=14, command=generate_password)
generate_button.place(x=299, y=325)

save_button = Button()
save_button.config(text="Save Credentials", width=34, command=save_data)
save_button.place(x=158, y=360)

search_button = Button()
search_button.config(text="Search", width=14, command=search)
search_button.place(x=299, y=270)

window.mainloop()
