import tkinter as tk
from tkinter import messagebox

from main import WebAutomation, get_credentials


class App:
    def __init__(self, root):
        self.root: tk.Tk = root
        self.root.title("Web Automation GUI")

        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, sticky="w")
        self.username = (tk.Entry(self.login_frame))
        self.username.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, sticky="w")
        self.password = tk.Entry(self.login_frame, show="*")
        self.password.grid(row=1, column=1, sticky="ew")

        # Form Submission Frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="Full Name").grid(row=0, column=0, sticky="w")
        self.fullname = tk.Entry(self.form_frame)
        self.fullname.grid(row=0, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Email").grid(row=1, column=0, sticky="w")
        self.email = tk.Entry(self.form_frame)
        self.email.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Current Address").grid(row=2, column=0, sticky="w")
        self.current_address = tk.Entry(self.form_frame)
        self.current_address.grid(row=2, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Permanent Address").grid(row=3, column=0, sticky="w")
        self.permanent_address = tk.Entry(self.form_frame)
        self.permanent_address.grid(row=3, column=1, sticky="ew")

        # Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Close Browser", command=self.close_browser).grid(row=0, column=1, padx=5)
        pass

    def submit_data(self):
        try:
            get_credentials()
        except FileNotFoundError:
            username = self.username.get()
            password = self.password.get()
        else:
            username, password = get_credentials()
        fullname = self.fullname.get()
        email = self.email.get()
        current_address = self.current_address.get()
        permanent_address = self.permanent_address.get()

        self.web_automation = WebAutomation()
        self.web_automation.login(username, password)
        self.web_automation.fill_form(fullname, email, current_address, permanent_address)

        pass

    def close_browser(self):
        self.web_automation.close()
        messagebox.showinfo("INFO", "Submitted Successfully")
        pass


root = tk.Tk()
app = App(root)
root.mainloop()
