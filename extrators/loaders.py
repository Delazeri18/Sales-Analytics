from bigquery import *

# função exportar planilha teste

BigQuery = BigQuery()
# dados campari club
BigQuery.obter_dados_Industrias(nome_arquivo='Base_Main')
