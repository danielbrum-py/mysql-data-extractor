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
       
"""def toexcel(db):
    query = "SELECT * FROM samp_2026;"              
    dfb = pd.read_sql(query, con=db)
    df.to_excel('samp_2026', index = False)"""

def deleteall(db):
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE samp_2026")
    db.commit()
    cursor.close()
    
