from readline import backend
import threading
import Backend
import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class app(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        self.title("MySQL Data Extractor")

        self.user_entry()
        self.password_entry()
        self.host_entry()
        self.bank_entry()
        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(padx=30,pady=15,fill="x")
        self.progress.set(0)
        self.create_buttons()
    
    def user_entry(self):
        user_label = ctk.CTkLabel(self, text="Insert your MySQL user:", font=("Arial", 20, "bold"))
        user_label.pack(pady=5) 
        self.user_entry = ctk.CTkEntry(self, height=40, font=("Arial", 14))
        self.user_entry.pack(pady=5, padx=30, fill="x")

    def password_entry(self):
        password_label = ctk.CTkLabel(self, text="Insert your MySQL password:", font=("Arial", 20, "bold"))
        password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*", height=40, font=("Arial", 18))
        self.password_entry.pack(pady=5,padx=30, fill="x")

    def host_entry(self):
        host_label = ctk.CTkLabel(self, text="Insert your MySQL host:", font=("Arial", 20, "bold"))
        host_label.pack(pady=5)
        self.host_entry = ctk.CTkEntry(self, height=40, font=("Arial", 18))
        self.host_entry.pack(pady=5, padx=30, fill="x")

    def bank_entry(self):
        bank_label = ctk.CTkLabel(self, text="Now what bank you want see", font=("Arial", 20, "bold"))
        bank_label.pack(pady=5)
        self.bank_entry = ctk.CTkEntry(self, height=40, font=("Arial", 18))
        self.bank_entry.pack(pady=5, padx=30, fill="x")

    def create_buttons(self):
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=20)
        connect_button = ctk.CTkButton(button_frame,text="Connect",width=140,height=40,command=self.connect_database)
        connect_button.grid(row=0,column=0,padx=10)
        export_button = ctk.CTkButton(button_frame, text="Export XLSX", width=140, height=40, command=self.export_xlsx)
        export_button.grid(row=0,column=1,padx=10)

    def connect_database(self):
        self.db = Backend.conectar_mysql(self)
        self.CTkLabel(self, text="Connected to MySQL database!",font=("Arial", 16, "bold")).pack(pady=10)

    def export_xlsx(self):
        Backend.toexcel(self.db)

    def export_process(self):
        Backend.toexcel(self.db)
        self.after(0,self.export_finished)

    def export_finished(self):
        self.progress.set(1)
        self.export_button.configure(state="normal")
        self.CTkLabel(self, text="Excel exported successfully!", font=("Arial", 16, "bold")).pack(pady=10)

janela = app()
janela.mainloop()

db = Backend.conectar_mysql(
    app.user_entry,
    app.password_entry,
    app.host_entry,
    app.bank_entry
)