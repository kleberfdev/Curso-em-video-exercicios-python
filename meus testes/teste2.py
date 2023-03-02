import pandas as pd
from database import getDatabaseConnection
import csv

def formatedData():
    with open('small.txt') as file:
        data = []
        for line in file.readlines():
            data.append(line)
        filtredData = []
        for row in range(len(data)):
            dto = data[row].replace('"', '')
            filtredData.append(dto.split(';'))
        return filtredData

def createCsv(data):
    df = pd.DataFrame(data, columns=[
      'CNPJ_BASICO', 'CNPJ_ORDEM', 'CNPJ_DV',
      'IDENTIFICADOR_MATRIZ_FILIAL', 'NOME_FANTASIA',
      'DATA_SITUACAO_CADASTRAL', 'MOTIVO_SITUACAO_CADASTRAL',
      'NOME_DA_CIDADE_NO_EXTERIOR', 'PAIS', 'DATA_DE_INICIO_ATIVIDADE',
      'CNAE_FISCAL_PRINCIPAL', 'CNAE_FISCAL_SECUNDARIA',
      'TIPO_DE_LOGRADOURO', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO',
      'BAIRRO', 'CEP', 'UF', 'MUNICIPIO', 'DDD1', 'TELEFONE1',
      'DDD2', 'TELEFONE2', 'DDD_DO_FAX', 'FAX', 'CORREIO_ELETRONICO',
      'SITUACAO_ESPECIAL', 'DATA_DA_SITUACAO_ESPECIAL', 'extra', 'extra2'
    ])
    label = 'csv.csv'
    df.to_csv(label)
    return label

db = getDatabaseConnection()
data = formatedData()
label = createCsv(data)
with open(label, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dbResponse = db.mycollection.insert_one(
            {
                'cnpj': str(row['CNPJ_BASICO'])+str(row['CNPJ_ORDEM'])+str(row['CNPJ_DV']),
                'tel': str(row['TELEFONE1'])+str(row['DDD1']),
                'nome_fantasia': row['NOME_FANTASIA'],
                'email': row['SITUACAO_ESPECIAL'],
                'cep': row['CEP']
            }
        )