import mysql.connector
import pandas as pd 

def conectar_mysql(app):
    db = mysql.connector.connect(
        host = app.host_entry.get(),
        user = app.user_entry.get(),
        password = app.password_entry.get(),
        database = app.bank_entry.get()
    )
    return db

def showdata(db):
    cursor = db.cursor()
    dados = cursor.fetchall()
    for i in dados:
        print(i)
    cursor.close()
       
def toexcel(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM samp_2026;")
    dados = cursor.fetchall()
    colunas = [i[0] for i in cursor.description]
    cursor.close()
    df = pd.DataFrame(dados, columns=colunas)
    df.to_excel('mysql_extracted_file.xlsx', index=False)
    print("Excel exported successfully!")