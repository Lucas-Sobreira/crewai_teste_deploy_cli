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

def get_bitcoin_df() -> pd.DataFrame:
    """Coleta e salva os dados do BitCoin em um Dataframe Pandas"""
    
    # URL da API da Coinbase para o preço spot do Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    # Requisição GET
    response = requests.get(url)
    data = response.json()

    # Extrair dados relevantes
    preco = float(data['data']['amount'])
    ativo = data['data']['base']        # "BTC"
    moeda = data['data']['currency']    # "USD"
    horario_coleta = datetime.now()

    # Criar DataFrame no padrão em português
    df = pd.DataFrame([{
        'ativo': ativo,
        'preco': preco,
        'moeda': moeda,
        'horario_coleta': horario_coleta
    }])

    return df

if __name__ == "__main__": 
    # Carrega variáveis do .env
    load_dotenv()

    # Engine de Conexão com o Banco de Dados
    engine = setup_db()

    # Dataframe com os dados do BitCoin
    df = get_bitcoin_df()
    print(df)    

    # Salva no banco (append)
    df.to_sql("bitcoin", engine, if_exists="append", index=False)

    print("✅ Cotações inseridas no banco com sucesso!")