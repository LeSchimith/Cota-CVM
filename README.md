# Cota-CVM
Este projeto realiza a extração, leitura e filtragem de dados diários de fundos de investimento disponibilizados pela CVM (Comissão de Valores Mobiliários). Ele baixa os arquivos compactados, descompacta-os, carrega os dados em um DataFrame do pandas e filtra os registros de um fundo específico com base no CNPJ.

## 🚀 Começando
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos
Você precisará do Python 3 instalado, além das seguintes bibliotecas:

```
Pandas
Requests
```

Você pode instalá-las com pip:
```
pip install pandas requests
```

### 🔧 Instalação
1. Clone este repositório:
```
git clone https://github.com/LeSchimith/Cota-CVM
cd repositorio
```

2. Crie um arquivo Python com o seguinte código:

```
import pandas as pd
import requests
import zipfile
import io

nome_arquivo = "inf_diario_fi_202506.csv"
link_arquivo = "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_202506.zip"

request = requests.get(link_arquivo)
zip = zipfile.ZipFile(io.BytesIO(request.content))
zip = zip.open(nome_arquivo)

linhas = zip.readlines()
linhas = [i.strip().decode("ISO-8859-1") for i in linhas]
linhas = [i.split(';') for i in linhas]

dataframe = pd.DataFrame(linhas[1:], columns=linhas[0])

cnpj_fundo = "XX.XXX.XXX/XXXX-XX"
df_filtrado = dataframe[dataframe["CNPJ_FUNDO_CLASSE"] == cnpj_fundo]

print(df_filtrado)
```

3. Execute o script com:
```
python seu_arquivo.py
```
## ⚙️ Executando os testes

Este projeto não possui testes automatizados por enquanto, mas você pode verificar se o script está funcionando corretamente ao executar o código e conferir se o DataFrame retorna as informações esperadas.

### 🔩 Analise os testes de ponta a ponta

O teste principal é verificar se o script:
```
1. Baixa o arquivo .zip da CVM

2. Extrai corretamente o CSV

3. Carrega os dados no pandas

4. Filtra corretamente pelo CNPJ informado
```

## 📦 Implantação

Este projeto pode ser facilmente integrado a outras rotinas de análise de dados em Python. Basta importar o script e adaptar para usar em um pipeline automatizado ou notebook Jupyter.

## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem principal
* [pandas](https://pandas.pydata.org/) - Para manipulação de dados
* [requests](https://docs.python-requests.org/) - Para download HTTP
* [zipfile](https://docs.python.org/3/library/zipfile.html) - Para descompactar os arquivos

## 🎁 Expressões de agradecimento

* Conte a outras pessoas sobre este projeto 📢;
* Contribua com sugestões, melhorias e bugs 💡;
* Deixe uma estrela ⭐ no repositório;
* Compartilhe com colegas da área! 🫂
