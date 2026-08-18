import Backend
import customtkinter as ctk

usuario = input("Insira seu usuario do mysql: ")
senha = input("Insira sua senha mysql: ")
host = input("Insira seu host mysql: ")
bancodados = input("Insira o banco de dados sql que vai usar: ")

db = Backend.conectar_mysql(
    usuario,
    senha,
    host,
    bancodados
)

print("Conectado ao MySQL!")