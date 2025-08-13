from unittest import result
import requests
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
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

engine = setup_db()
with engine.connect() as connection:
    sql_query = "SELECT * FROM public.bitcoin"
    result = connection.execute(sql_query)
    print(result)