import os
import pandas as pd
from datetime import datetime, timedelta
from urllib.parse import quote
from dotenv import load_dotenv


def get_datas():
    """Retorna as datas de início e fim formatadas"""
    data_inicio = datetime.today()
    data_fim = data_inicio - timedelta(days=7)
    
    return data_inicio.strftime('%Y-%m-%d'), data_fim.strftime('%Y-%m-%d')


def get_url(data_inicio_str: str, data_fim_str: str) -> str:
    """Monta a URL da API"""
    load_dotenv()
    
    city = quote('São Paulo, BR')
    key = os.getenv("API_KEY")
    
    return (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        f"{city}/{data_fim_str}/{data_inicio_str}"
        f"?unitGroup=metric&include=days&key={key}&contentType=csv"
    )


def extrair_clima() -> None:
    """Extrai dados de clima e salva em CSV"""
    data_inicio_str, data_fim_str = get_datas()
    url = get_url(data_inicio_str, data_fim_str)
    
    df = pd.read_csv(url)
    
    file_path = f'data/raw/semana_{data_inicio_str}/'
    os.makedirs(file_path, exist_ok=True)
    
    df.to_csv(file_path + 'dados_brutos.csv', index=False)
    df[['datetime', 'tempmin', 'tempmax', 'temp']].to_csv(file_path + 'temperaturas.csv', index=False)
    df[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv', index=False)
    
    print(f"Dados salvos em {file_path}")


if __name__ == "__main__":
    extrair_clima()