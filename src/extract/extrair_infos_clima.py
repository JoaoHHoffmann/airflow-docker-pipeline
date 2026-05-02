import os
import pandas as pd
from datetime import datetime, timedelta
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio - timedelta(days=7)

# formatando as datas
data_inicio_str = data_inicio.strftime('%Y-%m-%d')
data_fim_str = data_fim.strftime('%Y-%m-%d')

city = quote('São Paulo, BR')
key = os.getenv("API_KEY")

url = (
    f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    f"{city}/{data_fim_str}/{data_inicio_str}"
    f"?unitGroup=metric&include=days&key={key}&contentType=csv"
)


df = pd.read_csv(url)

file_path = f'data/raw/semana_{data_inicio_str}/'
os.makedirs(file_path, exist_ok=True)

df.to_csv(file_path + 'dados_brutos.csv', index=False)
df[['datetime', 'tempmin', 'tempmax', 'temp']].to_csv(file_path + 'temperaturas.csv', index=False)
df[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv', index=False)

