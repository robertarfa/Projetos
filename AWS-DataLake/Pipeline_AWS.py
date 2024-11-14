# import urllib.request

# def extract_data(url, filename):
#   try:
#     urllib.request.urlretrieve(url, filename)
#   except Exception as e:
#     print(e)

# extract_data("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/c9509ab4-6f6d-4b97-979a-0cf2a10c922b/download/311_service_requests_2015.csv", "data/dados_2015.csv")
# extract_data("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/b7ea6b1b-3ca4-4c5b-9713-6dc1db52379a/download/311_service_requests_2016.csv", "data/dados_2016.csv")
# extract_data("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/30022137-709d-465e-baae-ca155b51927d/download/311_service_requests_2017.csv", "data/dados_2017.csv")
# extract_data("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/2be28d90-3a90-4af1-a3f6-f28c1e25880a/download/311_service_requests_2018.csv", "data/dados_2018.csv")
# extract_data("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/ea2e4696-4a2d-429c-9807-d02eb92e0222/download/311_service_requests_2019.csv", "data/dados_2019.csv")
# extract_data("https://data.boston.gov/dataset/8048697b-ad64-4bfc-b090-ee00169f2323/resource/6ff6a6fd-3141-4440-a880-6f60a37fe789/download/script_105774672_20210108153400_combine.csv", "data/dados_2020.csv")

#Criar a lista com arquivos para que possam ser transformadas em dicionários
arquivos = [
  "data/dados_2015.csv",
  "data/dados_2016.csv",
  "data/dados_2017.csv",
  "data/dados_2018.csv",
  "data/dados_2019.csv",
  "data/dados_2020.csv",
]

dfs = {}

#função utilizando pandas para consultar os arquivos
import pandas as pd

for arquivo in arquivos:
  ano = arquivo.split("_")[-1]
  print(ano)
  ano2  = ano.split(".")[0]
  print(ano2)

  dfs[ano2] = pd.read_csv(arquivo)

  #Verificar se os arquivos estão corretos
  dfs['2018'].head()

import boto3
import os
from dotenv import dotenv_values

config = dotenv_values(".env") 

aws_access_key_id = config['AWS_ACCESS_KEY_ID']
aws_secret_access_key = config['AWS_SECRET_ACCESS_KEY']
region_name = "us-east-1"

print(aws_access_key_id)
print(aws_secret_access_key)

#criar uma sessão padrão
boto3.setup_default_session(
  aws_access_key_id =aws_access_key_id,
  aws_secret_access_key = aws_secret_access_key,
  region_name = region_name
)

#cliente s3

s3 = boto3.client("s3")

#arquivo teste
content = """Olá, S3"""

with open("hello-s3.txt", 'w+') as file:
  file.write(content)

#subir arquivo para aws
s3.upload_file("hello-s3.txt", "robsdatalakeaws", "bronze/hello-s3.txt")
