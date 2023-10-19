# Import necessary modules
from tkinter import *
from tkinter import messagebox
import sqlite3

# Create GUI for login page
def login():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter login details").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

    login_screen.mainloop()

# Verify login details from database
def login_verify():
    username = username_verify.get()
    password = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
    row = cur.fetchone()

    if row:
        messagebox.showinfo("Success", "Login Successful!")
        login_screen.destroy()
        adblock()
    else:
        messagebox.showerror("Error", "Invalid Login Details")

# Create GUI for register page
def register():
    global register_screen
    register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()

    register_screen.mainloop()

# Insert new user details into database
def register_user():
    username_info = username.get()
    password_info = password.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL, password TEXT NOT NULL)")
    cur.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username_info, password_info))
    conn.commit()
    messagebox.showinfo("Success", "Registration Successful!")
    register_screen.destroy()

# Adblock program in Python
def adblock():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    # Disable ads using ad blocker extension
    chrome_options = Options()
    # Location of AdBlock extension (change path as necessary)
    adblock_path = r"C:\adblocker\adblocker.crx"
    chrome_options.add_extension(adblock_path)
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.google.com")

# Create main menu
def main_menu():
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Welcome")

    Label(text="Select an option below", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()

    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()

if __name__ == '__main__':
    main_menu()