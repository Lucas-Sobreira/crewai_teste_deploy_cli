from unittest import result
import requests
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

def setup_db():
    """Configura a conexão com o Banco de Dados SQL"""

    # Configuração do banco (substituir com seus dados reais)
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    # Criar conexão SQLAlchemy
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)
    return engine

def consulta_db(engine):
    """Executa queries no Banco de Dados"""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM public.bitcoin"))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df

if __name__ == "__main__":
    load_dotenv()
    engine=setup_db()

    print(consulta_db(engine))
