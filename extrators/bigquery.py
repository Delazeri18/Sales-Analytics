from google.cloud import bigquery
from google.oauth2 import service_account
import logging
from os import getenv
import pandas as pd
import os

class BigQuery:
    def __init__(self):
        credential_path = getenv('PYTHONPATH')+getenv('CREDENTIAL_PATH')
        credentials = service_account.Credentials.from_service_account_file(
            credential_path,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        self.client = bigquery.Client(credentials=credentials)
        # self.dataset_id = dataset
        self.dataset_id = "topsystem_bronze"

    def obter_dados_Industrias(self,fornecedor, mes_inicio, mes_fim, nome_arquivo):
        # Condição para industria
        estado_condition = ""
        if fornecedor in [80047, 80166]:
            estado_condition = "AND estado IN (41, 42)"
        # Consulta SQL com parâmetros de filtro para fornecedor e intervalo de mês
        query = f"""
        SELECT 
            data_consumo AS DataConsumo,
            filial AS Filial,
            cliente AS Cliente,
            tipoestabelecimento AS TipoEstabelecimento,    # validar o que precisa 3 fazer union
            estado AS Estado,
            produto AS Produto,              
            fornecedor AS Fornecedor,
            volumes AS Volumes,
            qtde AS Quantidade

        FROM 
        `dinho-dw.topsystem_bronze.consumo`

        WHERE 
            EXTRACT(MONTH FROM data_consumo) BETWEEN {mes_inicio} AND {mes_fim}
            AND EXTRACT(YEAR FROM data_consumo) = EXTRACT(YEAR FROM CURRENT_DATE())
            {estado_condition}
            AND fornecedor = {fornecedor}
        """
        
        try:
            # Executar a consulta e obter os resultados em um DataFrame
            df = self.client.query(query).to_dataframe()

            # Criar a pasta 'relatorios' se não existir
            pasta_relatorios = "relatorios"
            os.makedirs(pasta_relatorios, exist_ok=True)

            # Caminho do arquivo para salvar os dados
            caminho_arquivo = os.path.join(pasta_relatorios, nome_arquivo)
            df.to_csv(caminho_arquivo, index=False)
            print(f"Relatório salvo como: {caminho_arquivo}")

        except Exception as e:
            print(f"Ocorreu um erro ao obter os dados ou salvar o arquivo: {e}")
            return None

    def obter_dados_faseamento(self):
        # Condição para o estado

        # Consulta SQL para faseamento
        query = f"""
        SELECT 
            cliente AS Cliente,
            produto AS Produto,
            equipe AS Equipe,
            filial AS Filial,
            volumes AS Volumes,
            qtde AS Quantidade,
            fornecedor AS Fornecedor
        FROM 
            `dinho-dw.topsystem_bronze.consumo`
        WHERE 
            tipo = 'nf' 
            AND estado = 41
            AND EXTRACT(MONTH FROM data_consumo) = EXTRACT(MONTH FROM CURRENT_DATE())
            AND EXTRACT(YEAR FROM data_consumo) = EXTRACT(YEAR FROM CURRENT_DATE())
        """

        try:
            # Executar a consulta e obter os resultados em um DataFrame
            df = self.client.query(query).to_dataframe()

            # Criar a pasta 'relatorios' se não existir
            pasta_relatorios = "relatorios"
            os.makedirs(pasta_relatorios, exist_ok=True)

            nome_arquivo = 'teste_faseamentos'

            # Caminho do arquivo para salvar os dados
            caminho_arquivo = os.path.join(pasta_relatorios, nome_arquivo)
            df.to_excel(caminho_arquivo, index=False)
            print(f"Relatório de faseamento salvo como: {caminho_arquivo}")

        except Exception as e:
            print(f"Ocorreu um erro ao obter os dados ou salvar o arquivo: {e}")
            return None
        
        # Retornar o DataFrame com os dados
        return df