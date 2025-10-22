import sqlite3
import hashlib
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')
connection.commit()

def registrieren(username, password):
    if not username or not password:
        return "Bitte Benutzername und Passwort eingeben."

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        connection.commit()
        return "Registrierung erfolgreich!"
    except:
        return "Benutzername existiert bereits."

def login(username, password):
    if not username or not password:
        return "Bitte Benutzername und Passwort eingeben."

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and hashed_password == result[0]:
        return "Login erfolgreich!"
    elif result:
        return "Falsches Passwort."
    else:
        return "Benutzername nicht gefunden."

def passwordstrecheck(username, password):
    if len(password) <= 8 or len(password) >=20:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_,.?\":{}|<>]", password):
        return False
    return True
