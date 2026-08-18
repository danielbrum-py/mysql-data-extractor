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
    cursor = db.cursor
    cursor.execute("""SELECT * FROM energia""")
    dados = cursor.fetchall()
    for i in dados:
        print(i)
    db.commit()
    cursor.close()
       
def toexcel(db):
    query = "SELECT * FROM energia;"              
    dfb = pd.read_sql(query, con=db)
    dfb.to_excel('samp-2026', index = False)

def deleteall(db):
    cursor = db.cursor
    cursor.execute("TRUNCATE TABLE energia")
    db.commit()
    cursor.close()
    
