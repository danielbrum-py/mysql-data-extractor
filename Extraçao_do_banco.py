import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("/home/mec/Documentos/vscode/python/Projeto-integraçao/samp-2026.csv",encoding="latin1", sep = ";")

engine = create_engine(
    "mysql+mysqlconnector://root:Linux2314@localhost/energia"
)

df.to_sql(
    "samp_2026",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=5000
)

print("Dados enviados para o MySQL")
