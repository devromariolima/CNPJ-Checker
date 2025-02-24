import requests
import pandas as pd
import time

# Function to remove dots, bars and dashes from the CNPJ
def formatar_cnpj(cnpj):
    return cnpj.replace('.', '').replace('/', '').replace('-', '')

# API query function with timeout and sleep
def consultar_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro na consulta do CNPJ {cnpj}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão para o CNPJ {cnpj}: {e}")
        return None

# Function to check if the company is active
def is_ativa(dados):
    situacao = dados.get('situacao', '').lower()
    return situacao == 'ativa'

# Load the spreadsheet with the CNPJs from the "teste.xlsx" file
df = pd.read_excel('teste.xlsx')

# Check if the "CNPJ" or "cnpj" column exists and correct
if 'CNPJ' in df.columns:
    df['CNPJ'] = df['CNPJ']
elif 'cnpj' in df.columns:
    df['CNPJ'] = df['cnpj']
else:
    print("A coluna CNPJ não foi encontrada.")
    exit()

# Limit the number of lines to be processed (e.g. 5 lines)
MAX_LINHAS = 5

# List to store data from active companies
dados_ativos = []

# Process each CNPJ in the spreadsheet, up to the defined limit
for index, row in df.iterrows():
    if index >= 3:
        break
    
    cnpj = str(row['cnpj']).strip()
    
    # Skip lines with empty CNPJ
    if not cnpj:
        print(f"Linha {index + 1} ignorada (CNPJ vazio)")
        continue

    cnpj = cnpj.zfill(14)  # Correct the CNPJ format
    cnpj_formatado = formatar_cnpj(cnpj)  # Remove dots, bars and dashes
    
    print(f"Consultando CNPJ: {cnpj_formatado} ({index + 1}/{len(df)})")
    dados = consultar_cnpj(cnpj_formatado)

 # Checks if the data was returned and if the company is active
    if dados and is_ativa(dados):
        dados_ativos.append({
            'CNPJ': cnpj,
            'Nome': dados['nome'],
            'Situação': dados['situacao'],
            'Atividade Principal': dados['atividade_principal'][0]['text'],
            'UF': dados['uf'],
            'Município': dados['municipio'],
            'Telefone': dados['telefone']
        })

   # Wait 10 seconds between requests to avoid blocking
    time.sleep(10)

# Check for collected data
print(f"Total de empresas ativas: {len(dados_ativos)}")

# Save data from active companies to a new Excel file
if dados_ativos:
    df_ativos = pd.DataFrame(dados_ativos)
    df_ativos.to_excel('empresas_ativas.xlsx', index=False)
    print("Dados salvos em 'empresas_ativas.xlsx'")
else:
    print("Nenhuma empresa ativa encontrada.")
