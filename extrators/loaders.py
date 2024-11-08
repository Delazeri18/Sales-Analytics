from bigquery import *

# função exportar planilha teste

BigQuery = BigQuery()
# dados campari club
BigQuery.obter_dados_Industrias(fornecedor=80047, mes_inicio=10, mes_fim=10, nome_arquivo='dados_Campari_club.csv')
'''
# campari p4p 
BigQuery.obter_dados_Industrias(fornecedor=80047, mes_inicio=10, mes_fim=10, nome_arquivo='dados_Campari_p4p.csv') # p4p

# maria rita 
BigQuery.obter_dados_Industrias(fornecedor=80047, mes_inicio=10, mes_fim=x, nome_arquivo='dados_Campari_club.csv')  # esse para ver 
# pernod

#jack
BigQuery.obter_dados_Industrias(fornecedor=x, mes_inicio=10, mes_fim=10, nome_arquivo='dados_Campari_club.csv')  # esse para ver 

#vct 
BigQuery.obter_dados_Industrias(fornecedor=x, mes_inicio=10, mes_fim=10, nome_arquivo='dados_Campari_club.csv')  # esse para ver 

#Beam
BigQuery.obter_dados_Industrias(fornecedor=x, mes_inicio=10, mes_fim=10, nome_arquivo='dados_Campari_club.csv')  # esse para ver 
'''