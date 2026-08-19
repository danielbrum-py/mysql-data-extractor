import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class app(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('450x400')
        self.title("MySQL Data Extractor")

        self.user_entry()
        self.password_entry()
        self.host_entry()
        self.bank_entry()

    def user_entry(self):
        user_label = ctk.CTkLabel(self, text="Insert your MySQL user:")
        user_label.pack(pady=5) 
        self.user_entry = ctk.CTkEntry(self)
        self.user_entry.pack(pady=10)

    def password_entry(self):
        password_label = ctk.CTkLabel(self, text="Insert your MySQL password:")
        password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=10)

    def host_entry(self):
        host_label = ctk.CTkLabel(self, text="Insert your MySQL host:")
        host_label.pack(pady=5)
        self.host_entry = ctk.CTkEntry(self)
        self.host_entry.pack(pady=10)

    def bank_entry(self):
        bank_label = ctk.CTkLabel(self, text=("Now what bank you want see"))
        bank_label.pack(pady=5)
        self.bank_entry = ctk.CTkEntry(self)
        self.bank_entry.pack(pady=10)

    def Button(self):
        pass

janela = app()
janela.mainloop()
print