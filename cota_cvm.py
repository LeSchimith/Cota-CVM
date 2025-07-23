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