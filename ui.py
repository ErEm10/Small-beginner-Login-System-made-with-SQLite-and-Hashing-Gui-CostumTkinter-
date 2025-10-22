import customtkinter as ctk
from auth import login, registrieren

def create_gui():
    app = ctk.CTk()
    app.geometry("600x400")
    app.title("Login System")

    container = ctk.CTkFrame(app)
    container.pack(expand=True, fill="both")
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    login_frame = ctk.CTkFrame(container)
    reg_frame = ctk.CTkFrame(container)
    home_frame = ctk.CTkFrame(container)

    for f in (login_frame, reg_frame, home_frame):
        f.grid(row=0, column=0, sticky="nsew")

    def show_login(): login_frame.tkraise()
    def show_reg(): reg_frame.tkraise()
    def show_home(): home_frame.tkraise()

    # --- Login ---
    ctk.CTkLabel(login_frame, text="Login").pack(pady=10)
    login_entry = ctk.CTkEntry(login_frame, width=200, placeholder_text="Benutzername")
    login_entry.pack(pady=(0, 8))
    login_password_entry = ctk.CTkEntry(login_frame, width=200, placeholder_text="Passwort", show="*")
    login_password_entry.pack(pady=(0, 7))

    def handle_login():
        result = login(login_entry.get().strip(), login_password_entry.get().strip())
        print(result)
        if result == "Login erfolgreich!":
            show_home()

    ctk.CTkButton(login_frame, text="Login", command=handle_login).pack(pady=(0,6))
    ctk.CTkButton(login_frame, text="→ Keinen Account?", command=show_reg).pack()

    # --- Registrierung ---
    ctk.CTkLabel(reg_frame, text="Registrierung").pack(pady=10)
    reg_username_entry = ctk.CTkEntry(reg_frame, width=200, placeholder_text="Benutzername")
    reg_username_entry.pack(pady=(0, 8))
    reg_password_entry = ctk.CTkEntry(reg_frame, width=200, placeholder_text="Passwort", show="*")
    reg_password_entry.pack(pady=(0, 7))

    def handle_reg():
        result = registrieren(reg_username_entry.get().strip(), reg_password_entry.get().strip())
        print(result)

    ctk.CTkButton(reg_frame, text="Registrieren", command=handle_reg).pack(pady=(0,6))
    ctk.CTkButton(reg_frame, text="← Zurück", command=show_login).pack()

    # --- Home ---
    ctk.CTkLabel(home_frame, text="Willkommen auf der Startseite!").pack(pady=20)
    ctk.CTkButton(home_frame, text="Logout", command=show_login).pack()

    show_login()
    return app
