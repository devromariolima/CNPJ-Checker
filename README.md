## CNPJ-Checker

- Descrição do Projeto

- CNPJ Checker é uma ferramenta em Python para automatizar a consulta de CNPJs de empresas na Receita Federal e verificar se estão ativas. Ele realiza a consulta de um conjunto de CNPJs de uma planilha Excel, obtém informações sobre as empresas e exporta os dados das empresas ativas para uma nova planilha.

## Funcionalidades
- Consulta de múltiplos CNPJs utilizando a API da Receita Federal.
- Verificação do status da empresa (ativa ou inativa).
- Formatação automática de CNPJs removendo caracteres inválidos como pontos, barras e traços.
- Exportação dos dados de empresas ativas para um arquivo Excel.
- Controle de requisições com intervalo de tempo para evitar bloqueios.

## Pré-requisitos
- Certifique-se de ter o Python instalado no seu sistema. Para verificar, execute:

- Você também precisará das seguintes bibliotecas Python, que podem ser instaladas via pip:

- pip install requests
- pip install pandas
- pip install openpyxl

## Uso

- Certifique-se de que sua planilha está no formato correto. A planilha deve conter uma coluna chamada CNPJ (ou cnpj em minúsculo) com os CNPJs a serem consultados.

## O script irá:

- Ler a planilha e remover caracteres indesejados do CNPJ.
- Consultar a API da Receita Federal para cada CNPJ válido.
- Verificar se a empresa está ativa.
- Exportar os dados de empresas ativas em um arquivo Excel chamado empresas_ativas.xlsx.

## Execute o script:

- python Cnpj_Checker.py

## Limitações

O script processa um número limitado de linhas definido pela variável MAX_LINHAS, que pode ser alterado conforme a necessidade.
É importante respeitar os limites de requisições da API da Receita Federal, configurando adequadamente o tempo de espera entre consultas (variável time.sleep).