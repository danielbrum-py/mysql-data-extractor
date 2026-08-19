import threading
import customtkinter as ctk 
import Backend

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('500x450')
        self.title("MySQL Data Extractor")

        self.setup_user_entry()
        self.setup_password_entry()
        self.setup_host_entry()
        self.setup_bank_entry()
        
        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(padx=30, pady=15, fill="x")
        self.progress.set(0)
        
        self.create_buttons()
        self.db = None
    
    def setup_user_entry(self):
        user_label = ctk.CTkLabel(self, text="Insert your MySQL user:", font=("Arial", 18, "bold"))
        user_label.pack(pady=2.5) 
        self.user_entry = ctk.CTkEntry(self, height=40, font=("Arial", 18))
        self.user_entry.pack(pady=2.5, padx=30, fill="x")

    def setup_password_entry(self):
        password_label = ctk.CTkLabel(self, text="Insert your MySQL password:", font=("Arial", 18, "bold"))
        password_label.pack(pady=2.5)
        self.password_entry = ctk.CTkEntry(self, show="*", height=40, font=("Arial", 18))
        self.password_entry.pack(pady=2.5, padx=30, fill="x")

    def setup_host_entry(self):
        host_label = ctk.CTkLabel(self, text="Insert your MySQL host:", font=("Arial", 18, "bold"))
        host_label.pack(pady=2.5)
        self.host_entry = ctk.CTkEntry(self, height=40, font=("Arial", 18))
        self.host_entry.pack(pady=2.5, padx=30, fill="x")

    def setup_bank_entry(self):
        bank_label = ctk.CTkLabel(self, text="Now what bank you want see", font=("Arial", 18, "bold"))
        bank_label.pack(pady=2.5)
        self.bank_entry = ctk.CTkEntry(self, height=40, font=("Arial", 18))
        self.bank_entry.pack(pady=2.5, padx=30, fill="x")

    def create_buttons(self):
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=5)
        connect_button = ctk.CTkButton(button_frame, text="Connect", width=140, height=40, command=self.connect_database)
        connect_button.grid(row=0, column=0, padx=10)
        self.export_button = ctk.CTkButton(button_frame, text="Export XLSX", width=140, height=40, command=self.export_xlsx)
        self.export_button.grid(row=0, column=1, padx=10)

    def connect_database(self):
        self.db = Backend.conectar_mysql(self)

        if not hasattr(self, "status_label"):
            self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 16, "bold"))
            self.status_label.pack(pady=5)
            
        self.status_label.configure(text="Connected to MySQL database!", text_color="green")

    def export_xlsx(self):
        if not hasattr(self, "status_label"):
            self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 16, "bold"))
            self.status_label.pack(pady=5)

        if not hasattr(self, "db") or not self.db:
            self.status_label.configure(text="Please connect to the database first!", text_color="red")
            return

        self.export_button.configure(state="disabled")
        self.progress.set(0)
        thread = threading.Thread(target=self.export_process)
        thread.start()

    def export_process(self):
        Backend.toexcel(self.db)
        self.after(0, self.export_finished)

    def export_finished(self):
        self.progress.set(1)
        self.export_button.configure(state="normal")
        self.status_label.configure(text="Excel exported successfully!", text_color="green")

if __name__ == "__main__":
    janela = App()
    janela.mainloop()
