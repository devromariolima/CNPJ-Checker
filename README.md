# CNPJ-Checker

- Descrição do Projeto

- CNPJ Checker é uma ferramenta em Python para automatizar a consulta de CNPJs de empresas na Receita Federal e verificar se estão ativas. Ele realiza a consulta de um conjunto de CNPJs de uma planilha Excel, obtém informações sobre as empresas e exporta os dados das empresas ativas para uma nova planilha.

# Funcionalidades
- Consulta de múltiplos CNPJs utilizando a API da Receita Federal.
- Verificação do status da empresa (ativa ou inativa).
- Formatação automática de CNPJs removendo caracteres inválidos como pontos, barras e traços.
- Exportação dos dados de empresas ativas para um arquivo Excel.
- Controle de requisições com intervalo de tempo para evitar bloqueios.

# Pré-requisitos
- Certifique-se de ter o Python instalado no seu sistema. Para verificar, execute:

- Você também precisará das seguintes bibliotecas Python, que podem ser instaladas via pip:

- pip install requests
- pip install pandas
- pip install openpyxl

# Limitações

O script processa um número limitado de linhas definido pela variável MAX_LINHAS, que pode ser alterado conforme a necessidade.
É importante respeitar os limites de requisições da API da Receita Federal, configurando adequadamente o tempo de espera entre consultas (variável time.sleep).