from tkinter import *
import json
from random import *
from tkinter import messagebox

def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
                with open("data.json","r") as json_file:
                    data=json.load(json_file)
                    website_name=website_entry.get()
                    required_dict=data[website_name]
                    messagebox.showinfo(title="Result",message="Email:"+required_dict["email"]+"\n"+"Website:"+website_name+"\n"+"Password:"+required_dict["password"])
        
        elif website_entry.get()=="" :
             messagebox.showinfo(title="Error", message="Please type something")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    


        

def add():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    json_dict={
        website:{
            "email":email,
            "password":password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        messagebox.askokcancel("Confirmation","Email : "+email+"\nPassword : "+password)
        try:
            with open("data.json","r") as data_file:
                json_data=json.load(data_file)
        

            

        except FileNotFoundError:
            data_file=open("data","w")
            json.dump(json_dict,data_file)
            

        else:
            
            json_data.update(json_dict)
            # print(json_data)
            with open("data.json", "w") as data_file:
                        #Saving updated data
                json.dump(json_data, data_file, indent=4)
            
        finally:
            password_entry.delete(0,END)    
            website_entry.delete(0,END)
                                



def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(5, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 3))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    





ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#231f20',padx=100)
ws.minsize(height=500,width=400)


canvas=Canvas(ws,width=250, height=300,highlightthickness=0 )
img = PhotoImage(file="image.png")
canvas.create_image(150,150,image=img)
canvas.grid(row=0,column=1)


website_label=Label(ws,foreground="white",bg="#231f20",text="Website",font=("Raleway",11))
website_label.grid(row=1,column=0)
email_label=Label(ws,bg="#231f20",foreground="white",text="Email",font=("Montserrat",11))
email_label.grid(row=2,column=0)
password_label=Label(ws,bg="#231f20",foreground="white",text="Password",font=("Rubik",11))
password_label.grid(row=3,column=0)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=1)
website_entry.config(highlightcolor="#008ff4",highlightthickness=2,highlightbackground="#96febf")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.config(highlightcolor="#008ff4",highlightthickness=2,highlightbackground="#96febf")
email_entry.insert(0, "vineet10338@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1,columnspan=1)
password_entry.config(highlightcolor="#008ff4",highlightthickness=2,highlightbackground="#96febf")


search_button = Button(text="Search",font=("Montserrat Bold",11),bg="#97fccf", width=7, command=search)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password",font=("Montserrat",11),bg="#97fccf", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=23,bg="#a5eeff",font=("Montserrat",11), command=add)
add_button.grid(row=4, column=1)

ws.mainloop()