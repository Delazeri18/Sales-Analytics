from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime, timedelta
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

    def obter_dados_Industrias(self, nome_arquivo):
        # Determina a data atual
        data_atual = datetime.now()

        # Calcula a data de 3 meses atrás
        data_3_meses_antes = data_atual - timedelta(days=90)

        # Extrai o mês e o ano da data de 3 meses atrás
        mes_inicio = data_3_meses_antes.month
        ano_inicio = data_3_meses_antes.year

        # Extrai o mês e o ano da data atual
        mes_fim = data_atual.month
        ano_fim = data_atual.year

        # Verifica se o intervalo de meses ultrapassa o final do ano
        if mes_inicio > mes_fim:
            # Caso o intervalo atravesse o final do ano, fazemos a consulta com o ano separado
            query = f"""
            SELECT 
                pedido_data_emissao AS DataConsumo,
                filial AS Filial,
                cliente AS Cliente,
                tipo_estabelecimento AS TipoEstabelecimento,
                estado AS Estado,
                produto AS Produto,              
                fornecedor AS Fornecedor,
                volumes AS Volumes,
                quantidade AS Quantidade,
                equipe AS Equipe
            FROM 
            `dinho-dw.topsystem_bronze.consumo`
            WHERE 
                (EXTRACT(MONTH FROM pedido_data_emissao) BETWEEN {mes_inicio} AND 12
                AND EXTRACT(YEAR FROM pedido_data_emissao) = {ano_inicio})
                OR 
                (EXTRACT(MONTH FROM pedido_data_emissao) BETWEEN 1 AND {mes_fim}
                AND EXTRACT(YEAR FROM pedido_data_emissao) = {ano_fim})
            """
        else:
            # Caso contrário, o intervalo está dentro do mesmo ano
            query = f"""
            SELECT 
                pedido_data_emissao AS DataConsumo,
                filial AS Filial,
                cliente AS Cliente,
                tipo_estabelecimento AS TipoEstabelecimento,
                estado AS Estado,
                produto AS Produto,              
                fornecedor AS Fornecedor,
                volumes AS Volumes,
                quantidade AS Quantidade,
                equipe AS Equipe
            FROM 
            `dinho-dw.topsystem_bronze.consumo`
            WHERE 
                EXTRACT(MONTH FROM pedido_data_emissao) BETWEEN {mes_inicio} AND {mes_fim}
                AND EXTRACT(YEAR FROM pedido_data_emissao) = {ano_fim}
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