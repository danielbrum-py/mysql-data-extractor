import mysql.connector
import pandas as pd

def conectar_mysql(usuario, senha, host, bancodados):
    db = mysql.connector.connect(
        host = host,
        user = usuario,
        password = senha,
        database = bancodados
    )
    return db

def showdata(db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM samp_2026""")
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