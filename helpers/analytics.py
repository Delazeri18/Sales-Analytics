import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
import os
from streamlit_extras.metric_cards import style_metric_cards
import streamlit as st


# Função de limpeza.
def clean_data_faseamento(df):
        df_sem_primeira_linha = df.drop(index=0)
        novos_nomes_colunas = df_sem_primeira_linha.iloc[0]
        df_sem_primeira_linha.columns = novos_nomes_colunas
        DF_PRINCIPAL = df_sem_primeira_linha[1:].reset_index(drop=True)

    # mapeando data frame.
        mapeamento_produtos = {
        # Campari
            816: "APEROL",
            9636: "CAMPARI",
            9637: "CAMPARI",
            423: "SAGATIBA",
            683: "SKYY",
            2805: "SKYY",
            8889: "SAGATIBA",
            1209: "SAGATIBA",
            4339: "CAMPARI",
        # Vct
            1381: "CELLAR",
            1573: "DEVILS",
            1575: "MARQUES",
            1901: "RESERVADO",
            1902: "RESERVADO",        #RESERVADO CASILLERO MARQUES TRIVENTO CELLAR DIABLO CDD CARNIVAL CDD BELIGHT GRAN RESERVA 
            1903: "RESERVADO",
            1904: "RESERVADO",
            1905: "RESERVADO",
            1909: "GRAN RESERVA",
            1910: "CASILLERO",
            1911: "CASILLERO",
            1912: "CASILLERO",
            1913: "CASILLERO",
            1914: "CASILLERO",
            1915: "CASILLERO",
            1916: "RESERVADO",
            1918: "RESERVADO",
            1923: "MARQUES",
            1934: "MARQUES",
            1935: "MARQUES",
            1936: "MARQUES",
            1937: "DIABLO",
            2001: "TRIVENTO",
            2002: "TRIVENTO",
            2539: "CELLAR",
            2947: "CELLAR",
            2994: "RESERVADO",
            3039: "CASILLERO",
            3199: "MARQUES",
            3252: "MARQUES",
            3275: "DIABLO",
            3286: "CELLAR",
            3288: "CELLAR",
            3291: "MARQUES",
            3292: "CELLAR",
            3293: "CELLAR",
            3303: "GRAN RESERVA",
            3304: "CELLAR",
            3424: "CASILLERO",
            3425: "CASILLERO",
            3442: "TRIVENTO",
            3458: "CELLAR",
            3511: "CASILLERO",
            3512: "CASILLERO",
            3513: "CASILLERO",
            3602: "MARQUES",
            3620: "CELLAR",
            3702: "CELLAR",
            3703: "CELLAR",
            3704: "TRIVENTO",
            3754: "CASILLERO",
            3996: "CELLAR",
            4149: "DIABLO",
            4344: "CASILLERO",
            4345: "CASILLERO",
            4802: "CELLAR",
            4999: "TRIVENTO",
            5007: "RESERVADO",
            5043: "CELLAR",
            5073: "CELLAR",
            5074: "CELLAR",
            5075: "CELLAR",
            5076: "CELLAR",
            5077: "CELLAR",
            5078: "CELLAR",
            5079: "CELLAR",
            5080: "CELLAR",
            5081: "MARQUES",
            6787: "MARQUES",
            8719: "TRIVENTO",
            8720: "GRAN RESERVA",
            8926: "CELLAR",
            9525: "CELLAR",
            9526: "CELLAR",
            9527: "TRIVENTO",
            9528: "CELLAR",
            9529: "RESERVADO",
            9598: "DIABLO",
            9599: "CDD CARNIVAL",
            9600: "CDD CARNIVAL",
            9601: "CDD CARNIVAL",
            9602: "CDD CARNIVAL",
            9603: "CELLAR",
            9617: "CDD BELIGHT",
            9671: "CDD BELIGHT",
            9701: "RESERVADO",
            9825: "MARQUES",
            9826: "CELLAR",
            9827: "CELLAR",
            3278: "CASILLERO",
        # Pernod
            444: "SAO FRANCISCO",
            690: "DOMECQ",
            8856: "BEEFEATER",
            689: "ABSOLUT",
            6883: "ABSOLUT",
            3726: "ABSOLUT",
            1560: "ABSOLUT",
            1348: "ABSOLUT",
            684: "ORLOFF",
            723: "BALLANTINES",
            1561: "BALLANTINES",
            4957: "BALLANTINES",
            740: "CHIVAS",
            1562: "CHIVAS",
            4265: "NATU",
            4276: "NATU",
            743: "PASSPORT",
            4738: "PASSPORT",
            8929: "BEEFEATER",
            8928: "BEEFEATER",
            4574: "BEEFEATER",
            9791: "BEEFEATER",
            1298: "BEEFEATER",
            2347: "BEEFEATER",
            4145: "ORLOFF",
            4358: "BALLANTINES",
            1524: "ABSOLUT",
            3569: "ABSOLUT",
            4305: "ABSOLUT",
            1317: "ABSOLUT",
            1508: "ABSOLUT",
            2269: "ABSOLUT",
            8888: "ABSOLUT",
            6798: "ABSOLUT",
            6814: "ABSOLUT",
            1525: "ABSOLUT",
            2948: "ABSOLUT",
            5047: "ORLOFF",
            708: "ORLOFF",
            9725: "BALLANTINES",
            9770: "BALLANTINES",
            709: "BALLANTINES",
            1507: "BALLANTINES",
            1232: "BALLANTINES",
            4273: "BALLANTINES",
            9567: "BALLANTINES",
            84103: "BALLANTINES",
            9566: "BALLANTINES",
            9707: "CHIVAS",
            1746: "CHIVAS",
            4274: "CHIVAS",
            1526: "CHIVAS",
            3510: "CHIVAS"
        }

        mapeamento_categoria = { # PERNOD
            "SAO FRANCISCO": "NACIONAL",
            "DOMECQ": "NACIONAL",
            "PASSPORT": "NACIONAL",
            "ORLOFF": "NACIONAL",
            "NATU": "NACIONAL"
        }



        mapeamentos_industria = {
            80047 : "CAMPARI",
            80145 : "JACK",
            80166 : "PERNOD",
            4135 : "VCT",
            80660 : "BEAM SUNTORY"
        }


        tipo_stab_map = {
            35: '5 A 10+ CHECKS',
            36: '5 A 10+ CHECKS'
        }


        # Funções de mapeamento
        def produtos_map(produtos):
            return mapeamento_produtos.get(produtos, 'PRODUTOS SEM MARCA')

        def map_tipo(estabelecimento):
            return tipo_stab_map.get(estabelecimento, 'XXXX')

        def nacional_map(marca):
            return mapeamento_categoria.get(marca, 'XXXXXX')

        def fabricante_map(fabricante):
            return mapeamentos_industria.get(fabricante, 'XXXXXX')

        # Aplicando funções
        DF_PRINCIPAL['Estabelecimento'] = DF_PRINCIPAL['Tipo Estabelecimento'].apply(map_tipo)
        DF_PRINCIPAL['Marca'] = DF_PRINCIPAL['Produto'].apply(produtos_map)
        DF_PRINCIPAL['Nacional?'] = DF_PRINCIPAL['Marca'].apply(nacional_map)
        DF_PRINCIPAL['Industria'] = DF_PRINCIPAL['Fornecedor'].apply(fabricante_map)

        # Mapeando equipes
        DF_PRINCIPAL['Nome Equipe'] = DF_PRINCIPAL['Nome Equipe'].replace({'BAR ESPECIAL': 'KEY ACCOUNT PR ON'})

        return DF_PRINCIPAL

    # função ler dados 

# função carregar. 
def load_data_faseamento():
    df = pd.read_excel("teste_faseamentos.xlsx")
    return clean_data_faseamento(df) # ajustar para universal 

# limpa e cria gráficos
def clean_data_campari_club():
    
    df_final = pd.read_excel("relatorios\\Template_CC.xlsx")

    #mapeando
    mapeamento_produtos = {
        816: "APEROL",
        9636: "CAMPARI",
        9637: "CAMPARI",
        423: "SAGATIBA",
        683: "SKYY",
        2805: "SKYY",
        8889: "SAGATIBA",
        1209: "SAGATIBA",
        4339: "CAMPARI",
        8815: "PREMIUM",
        657: "POPULAR CAMPARI",
        6195: "POPULAR CAMPARI",
        2522:"PREMIUM",
        10063: "PREMIUM",
        10064: "PREMIUM",
        10065: "PREMIUM",
        3423: 'PREMIUM',
        539: "PREMIUM",
        925: 'PREMIUM',
        2503 : 'PREMIUM',
        2804 : 'PREMIUM',
        832 : 'PREMIUM',
        2520: 'PREMIUM',
        1522 : 'PREMIUM',
        3426 : 'PREMIUM',
        8733 : 'PREMIUM',
        1399 : 'PREMIUM',
        1398 : 'PREMIUM',
        4327 : 'PREMIUM',
        2523 : "PREMIUM",
        2521 : "PREMIUM",
        716 : 'PREMIUM',
        715 : 'PREMIUM',
        8825 : 'PREMIUM',
        693: 'POPULAR CAMPARI',
        2522 : 'POPULAR CAMPARI',
        388 : 'POPULAR CAMPARI'
    }

    df_final['Marca'] = df_final['Produto'].map(mapeamento_produtos)

    todas_as_marcas = pd.DataFrame({
            'Marca': ['APEROL', 'CAMPARI', 'SAGATIBA', 'SKYY', 'PREMIUM','POPULAR CAMPARI']  # Inclua todas as marcas possíveis
    })

        # Funções de mapeamento
    def produtos_map(produtos):
        return mapeamento_produtos.get(produtos, 'PRODUTOS SEM MARCA')
        
    df_final['Marca'] = df_final['Produto'].apply(produtos_map)

        # filtrando filial
    df_SC = df_final[df_final['UF (Cliente)'] == 'SC'].reset_index(drop=True)
    df_PR = df_final[df_final['UF (Cliente)'] == 'PR'].reset_index(drop=True)

    positivacao_PR = df_PR.groupby('Marca')['Cliente'].nunique().reset_index()
    positivacao_SC = df_SC.groupby('Marca')['Cliente'].nunique().reset_index()

        # Mesclar com todas as marcas possíveis para garantir que todas apareçam, mesmo se a positivação for zero
    positivacao_PR = todas_as_marcas.merge(positivacao_PR, on='Marca', how='left').fillna(0)
    positivacao_SC = todas_as_marcas.merge(positivacao_SC, on='Marca', how='left').fillna(0)

    # calculando volume Total 

    volume_pr = df_PR['Volumes'].sum()
    volume_sc = df_SC['Volumes'].sum()

    volume_premium_pr = df_PR[df_PR['Marca'] == 'PREMIUM']['Volumes'].sum()
    volume_premium_sc = df_SC[df_SC['Marca'] == 'PREMIUM']['Volumes'].sum()

    # Quarteto:
     # Lista de todas as marcas que estamos interessados
    marcas_necessarias = ['APEROL', 'CAMPARI', 'SAGATIBA', 'SKYY']

        # Agrupar por CLIENTE e usar set() para verificar as marcas compradas por cada cliente
    QUARTETO_PR = df_PR.groupby('Cliente')['Marca'].apply(set).reset_index()
    QUARTETO_SC = df_SC.groupby('Cliente')['Marca'].apply(set).reset_index()

        # Filtrar clientes que compraram todas as marcas
    quarteto_PR = QUARTETO_PR[QUARTETO_PR['Marca'].apply(lambda x: set(marcas_necessarias).issubset(x))].reset_index()
    quarteto_SC = QUARTETO_SC[QUARTETO_SC['Marca'].apply(lambda x: set(marcas_necessarias).issubset(x))].reset_index()

        # Contar o número de clientes que compraram todas as marcas
    quarteto_PR_valor = quarteto_PR.shape[0]
    quarteto_SC_valor = quarteto_SC.shape[0]

    quarteto_data_PR = {
        'Marca': ['Quarteto'],
        'Cliente': [quarteto_PR_valor]  # Certifique-se de que quarteto_PR_valor é uma lista ou valor
    }

    # Criando um DataFrame para as novas linhas
    df_quarteto_pr = pd.DataFrame(quarteto_data_PR)

    # Criando os dados para o DataFrame de Quarteto para SC
    quarteto_data_SC = {
        'Marca': ['Quarteto'],
        'Cliente': [quarteto_SC_valor]  # Certifique-se de que quarteto_SC_valor é uma lista ou valor
    }

    # Criando um DataFrame para as novas linhas
    df_quarteto_sc = pd.DataFrame(quarteto_data_SC)

    # Concatenando os DataFrames com os DataFrames criados
    positivacao_PR = pd.concat([positivacao_PR, df_quarteto_pr], ignore_index=True)
    positivacao_SC = pd.concat([positivacao_SC, df_quarteto_sc], ignore_index=True)

        # Criar um dicionário de metas
    metas_dict_PR = {
            'APEROL': 1450,
            'CAMPARI': 4500,
            'SAGATIBA': 850,
            'SKYY': 1000,
            'Quarteto': 180,
            'POPULAR CAMPARI' : 0,
            'PREMIUM' : 100
    }


    metas_dict_SC = {
            'APEROL': 580,
            'CAMPARI': 1200,
            'SAGATIBA': 260,
            'SKYY': 380,
            'Quarteto': 110,
            'POPULAR CAMPARI' : 0,
            'PREMIUM' : 0       
    }
    
    # Adicionar a coluna de metas usando o método map
    positivacao_PR['Meta_Positivacao'] = positivacao_PR['Marca'].map(metas_dict_PR)
    positivacao_SC['Meta_Positivacao'] = positivacao_SC['Marca'].map(metas_dict_SC)



    # desejavel
    positivacao_PR['Desejavel'] = positivacao_PR['Meta_Positivacao'] * 1.2
    positivacao_SC['Desejavel'] = positivacao_SC['Meta_Positivacao'] * 1.2

    # renomeando coluna
    positivacao_PR = positivacao_PR.rename(columns={'Cliente': 'Positivação Realizada'})
    positivacao_SC = positivacao_SC.rename(columns={'Cliente': 'Positivação Realizada'})

    # coluna %
    positivacao_PR['Percentual'] = (positivacao_PR['Positivação Realizada'] / positivacao_PR['Meta_Positivacao']) * 100
    positivacao_SC['Percentual'] = (positivacao_SC['Positivação Realizada'] / positivacao_SC['Meta_Positivacao']) * 100

    positivacao_PR['Percentual'] =  positivacao_PR['Percentual'].round()
    positivacao_SC['Percentual'] =  positivacao_SC['Percentual'].round()
   
    # coluna diferença
    positivacao_PR['Faltante'] = positivacao_PR['Positivação Realizada'] - positivacao_PR['Desejavel']
    positivacao_SC['Faltante'] = positivacao_SC['Positivação Realizada'] - positivacao_SC['Desejavel']

    #coluna atingida
    positivacao_PR['Atingida'] = positivacao_PR['Faltante'].apply(lambda x: '✅' if x >= 0 else '❌')
    positivacao_SC['Atingida'] = positivacao_SC['Faltante'].apply(lambda x: '✅' if x >= 0 else '❌')

    # formatando dados
    positivacao_PR['Faltante'] = positivacao_PR['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    positivacao_SC['Faltante'] = positivacao_SC['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    positivacao_PR['Positivação Realizada'] = positivacao_PR['Positivação Realizada'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    positivacao_SC['Positivação Realizada'] = positivacao_SC['Positivação Realizada'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    positivacao_PR['Desejavel'] = positivacao_PR['Desejavel'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    positivacao_PR['Desejavel'] = positivacao_PR['Desejavel'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)


    # Filtrar o DataFrame para remover as linhas onde a coluna 'Marca' é igual a 'Premium'
    positivacao_PR_CC = positivacao_PR[~positivacao_PR['Marca'].isin(['PREMIUM', 'POPULAR CAMPARI'])]
    positivacao_SC_CC = positivacao_SC[~positivacao_SC['Marca'].isin(['PREMIUM', 'POPULAR CAMPARI'])]





    return volume_pr, volume_sc, positivacao_PR_CC, positivacao_SC_CC,volume_premium_pr, volume_premium_sc

def clean_data_campari_p4p():
    df_final = pd.read_excel("relatorios\\Campari_p4p.xlsx")
 
    
    mapeamento_produtos = {
        816: "APEROL",
        9636: "CAMPARI",
        9637: "CAMPARI",
        423: "SAGATIBA",
        683: "SKYY",
        2805: "SKYY",
        8889: "SAGATIBA",
        1209: "SAGATIBA",
        4339: "CAMPARI"
    }
    mapeamento_equipes = {
        "PILS": "MC",
        "BAR ESPECIAL": "ON",
        "BAGGIO": "MC",
        "KEY ACCOUNT PR OFF": "OFF",
        "TROPICAL": "MC",
        "KEY ACCOUNT PR ON": "ON",
        "CASCAVEL": "MC",
        "MARINGA": "MC",
        "LONDRINA": "MC",
        "EXTRA": "MC",
        "KEY ACCOUNT SC OFF": "OFF_SC",
        "INDUSTRIA E PROMOÇÕES": "MC",
        "SC NORTE": "MC_SC",
        "HEINEKEN": "MC",
        "SC SUL": "MC_SC",
        "TELEVENDAS": "MC",
        "EVENTOS PR": "MC",
        "KEY ACCOUNT SC ON": "ON_SC"
    }

    tipo_map = {
        35: '5 A 10+ CHECKS',
        36: '5 A 10+ CHECKS'
    }

    # Função para mapear o tipo de estabelecimento
    def map_tipo(estabelecimento):
        return tipo_map.get(estabelecimento, 'OUTROS')

    df_final['status'] = df_final['Nome Equipe'].map(mapeamento_equipes)
    df_final['MARCA'] = df_final['Produto'].map(mapeamento_produtos)
    df_final['Filial'] = df_final['Filial'].astype(int)
    df_final['Cliente'] = df_final['Cliente'].astype(int)
    df_final['TIPO'] = df_final['Tipo Estabelecimento'].apply(map_tipo)


    df_SC = df_final[df_final['UF (Cliente)'] == "SC"].reset_index(drop=True)
    df_PR = df_final[df_final['UF (Cliente)'] == "PR"].reset_index(drop=True)

    volumes_PR = df_PR.groupby('MARCA')['Volumes'].sum().reset_index()
    volumes_SC = df_SC.groupby('MARCA')['Volumes'].sum().reset_index()

    marcas_interesse = ["CAMPARI", "SAGATIBA", "SKYY", "APEROL"]
    todas_marcas = pd.DataFrame({'MARCA': marcas_interesse})
    volumes_pr = pd.merge(todas_marcas, volumes_PR, on='MARCA', how='left')
    volumes_sc = pd.merge(todas_marcas, volumes_SC, on='MARCA', how='left')

    volumes_pr = volumes_pr.infer_objects()
    volumes_sc = volumes_sc.infer_objects()


    volumes_pr['Volumes'] = volumes_pr['Volumes'].fillna(0)
    volumes_sc['Volumes'] = volumes_sc['Volumes'].fillna(0)


    volumes_pr_sorted = volumes_pr.sort_values(by='MARCA').reset_index(drop=True)
    volumes_sc_sorted = volumes_sc.sort_values(by='MARCA').reset_index(drop=True)


    Cobertura_PR = df_PR.groupby('TIPO')['Cliente'].nunique().reset_index()
    Cobertura_SC = df_SC.groupby('TIPO')['Cliente'].nunique().reset_index()

    # ARRUMANDO DF
    tipos_esperados = ['5 A 10+ CHECKS', 'OUTROS']
    tipos_df = pd.DataFrame({'TIPO': tipos_esperados})
    # Garantir que todos os tipos estejam presentes para PR
    Cobertura_PR = pd.merge(tipos_df, Cobertura_PR, on='TIPO', how='left').fillna(0)

    # Garantir que todos os tipos estejam presentes para SC
    Cobertura_SC = pd.merge(tipos_df, Cobertura_SC, on='TIPO', how='left').fillna(0)

    # pegar dados de cobertura  por tipo de establcimento
    mercados_sc = Cobertura_SC.loc[Cobertura_SC['TIPO'] == '5 A 10+ CHECKS', 'Cliente'].values[0]
    mercados_pr = Cobertura_PR.loc[Cobertura_PR['TIPO'] == '5 A 10+ CHECKS', 'Cliente'].values[0]

    geral_sc = Cobertura_SC['Cliente'].sum()
    geral_pr = Cobertura_PR['Cliente'].sum()

    # metas pra volumes
    metas_dict_PR = {
            'APEROL': 6000,
            'CAMPARI': 18500,
            'SAGATIBA': 1000,
            'SKYY': 1900
    }


    metas_dict_SC = {
            'APEROL': 7100,
            'CAMPARI': 10200,
            'SAGATIBA': 460,
            'SKYY': 1400
            }

    # Adicionar a coluna de metas usando o método map
    volumes_pr_sorted['Meta_Volume'] = volumes_pr_sorted['MARCA'].map(metas_dict_PR)
    volumes_sc_sorted['Meta_Volume'] = volumes_sc_sorted['MARCA'].map(metas_dict_SC)

    # arredondando volume 
    volumes_pr_sorted['Volumes'] = volumes_pr_sorted['Volumes'].round()
    volumes_sc_sorted['Volumes'] = volumes_sc_sorted['Volumes'].round()

    # renomeando coluna
    volumes_pr_sorted = volumes_pr_sorted.rename(columns={'Volumes': 'Volume Realizado'})
    volumes_sc_sorted = volumes_sc_sorted.rename(columns={'Volumes': 'Volume Realizado'})
   
    # coluna diferença
    volumes_sc_sorted['Faltante'] = volumes_sc_sorted['Volume Realizado'] - volumes_sc_sorted['Meta_Volume']
    volumes_pr_sorted['Faltante'] = volumes_pr_sorted['Volume Realizado'] - volumes_pr_sorted['Meta_Volume']


    # formatando dados
    volumes_pr_sorted['Faltante'] = volumes_pr_sorted['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    volumes_sc_sorted['Faltante'] = volumes_sc_sorted['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    volumes_pr_sorted['Volume Realizado'] = volumes_pr_sorted['Volume Realizado'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    volumes_sc_sorted['Volume Realizado'] = volumes_sc_sorted['Volume Realizado'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)


    # coluna %
    volumes_pr_sorted['Percentual'] = (volumes_pr_sorted['Volume Realizado'] / volumes_pr_sorted['Meta_Volume']) * 100
    volumes_sc_sorted['Percentual'] = (volumes_sc_sorted['Volume Realizado'] / volumes_sc_sorted['Meta_Volume']) * 100

    volumes_pr_sorted['Percentual'] =  volumes_pr_sorted['Percentual'].round()
    volumes_sc_sorted['Percentual'] =  volumes_sc_sorted['Percentual'].round()

    #coluna atingida
    volumes_pr_sorted['Atingida'] = volumes_pr_sorted['Faltante'].apply(lambda x: '✅' if x >= 0 else '❌')
    volumes_sc_sorted['Atingida'] = volumes_sc_sorted['Faltante'].apply(lambda x: '✅' if x >= 0 else '❌')


    return geral_pr, geral_sc,mercados_sc,mercados_pr,volumes_pr_sorted,volumes_sc_sorted


def clean_data_MariaRita():
    df_final = pd.read_excel("relatorios\\TEMPLATE_KA_MARIA.xlsx")

    # mapeando colunas: 
    mapeamento_produtos = {
        816: "APEROL",
        9636: "CAMPARI",
        9637: "CAMPARI",
        423: "SAGATIBA",
        683: "SKYY",
        2805: "SKYY",
        8889: "SAGATIBA",
        1209: "SAGATIBA",
        4339: "SUPER PREMIUM",
        6195: "POPULAR CAMPARI",
        10063: "SUPER PREMIUM",
        10064: "SUPER PREMIUM",
        10065: "SUPER PREMIUM",
        925: 'SUPER PREMIUM',
        2503 : 'SUPER PREMIUM',
        2804 : 'SUPER PREMIUM',
        832 : 'SUPER PREMIUM',
        2520: 'SUPER PREMIUM',
        1522 : 'SUPER PREMIUM',
        8733 : 'SUPER PREMIUM',
        1399 : 'SUPER PREMIUM',
        1398 : 'SUPER PREMIUM',
        4327 : 'CAMPARI',
        2523 : "SUPER PREMIUM",
        2521 : "SUPER PREMIUM",
        693: 'POPULAR CAMPARI',
        2522 : 'SUPER PREMIUM',
        388 : 'POPULAR CAMPARI',
        4456 : "SUPER PREMIUM",
        3653 : 'SUPER PREMIUM'
    }

    def classificar_categoria(marca):
        return mapeamento_produtos.get(marca, "OUTROS")


    df_final['MARCA'] = df_final['Produto'].apply(classificar_categoria)

    metas_dict = {
            'APEROL': 856,
            'CAMPARI': 688,
            'SAGATIBA': 113,
            'SKYY': 127,
            "SUPER PREMIUM": 620
        }


    df_maria_rita = df_final.groupby('MARCA')['Qtde'].sum().reset_index()
    df_maria_rita = df_maria_rita[df_maria_rita['MARCA'] != 'OUTROS']
    df_maria_rita = df_maria_rita[df_maria_rita['MARCA'] != 'POPULAR CAMPARI']
    df_maria_rita['Meta_Qtde'] = df_maria_rita['MARCA'].map(metas_dict)

    df_maria_rita['Faltante'] = df_maria_rita['Qtde'] - df_maria_rita['Meta_Qtde']
    df_maria_rita['Atingida'] = df_maria_rita['Faltante'].apply(lambda x: 'Sim' if x >= 0 else 'Não')


    df_maria_rita['Faltante'] = df_maria_rita['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    df_maria_rita['Faltante'] = df_maria_rita['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)

    df_maria_rita['Percentual'] = (df_maria_rita['Qtde'] / df_maria_rita['Meta_Qtde']) * 100
    df_maria_rita['Percentual'] =  df_maria_rita['Percentual'].round()

    df_maria_rita['Atingida'] = df_maria_rita['Faltante'].apply(lambda x: '✅' if x >= 0 else '❌')


    df_filtrado = df_maria_rita[df_maria_rita['MARCA'] != 'SUPER PREMIUM']

    total_quantidade_maria = df_filtrado['Qtde'].sum()

    return df_maria_rita, total_quantidade_maria


def clean_data_Pernod():
   # Ler o arquivo Excel
    df = pd.read_excel('relatorios\\template_pernod.xlsx')
    df_sem_primeira_linha = df.drop(index=0)
    novos_nomes_colunas = df_sem_primeira_linha.iloc[0]
    df_sem_primeira_linha.columns = novos_nomes_colunas
    df_final = df_sem_primeira_linha[1:].reset_index(drop=True)
    # REALAIZANDO MAPEAMENTO

    mapeamento_equipes = {
        "PILS": "MC",
        "BAR ESPECIAL": "ON",
        "BAGGIO": "MC",
        "KEY ACCOUNT PR OFF": "OFF",
        "TROPICAL": "MC",
        "KEY ACCOUNT PR ON": "ON",
        "CASCAVEL": "MC",
        "MARINGA": "MC",
        "LONDRINA": "MC",
        "EXTRA": "MC",
        "KEY ACCOUNT SC OFF": "OFF_SC",
        "INDUSTRIA E PROMOÇÕES": "MC",
        "SC NORTE": "MC_SC",
        "HEINEKEN": "MC",
        "SC SUL": "MC_SC",
        "TELEVENDAS": "MC",
        "EVENTOS PR": "Nao",
        "KEY ACCOUNT SC ON": "ON_SC"
    }

    mapeamento = {
        444: "SAO FRANCISCO",
        690: "DOMECQ",
        8856: "BEEFEATER",
        689: "ABSOLUT",
        6883: "ABSOLUT",
        3726: "ABSOLUT",
        1560: "ABSOLUT",
        1348: "ABSOLUT",
        684: "ORLOFF",
        723: "BALLANTINES",
        1561: "BALLANTINES",
        4957: "BALLANTINES",
        740: "CHIVAS",
        1562: "CHIVAS",
        4265: "NATU",
        4276: "NATU",
        743: "PASSPORT",
        4738: "PASSPORT",
        8929: "BEEFEATER",
        8928: "BEEFEATER",
        4574: "BEEFEATER",
        9791: "BEEFEATER",
        1298: "BEEFEATER",
        2347: "BEEFEATER",
        4145: "ORLOFF",
        4358: "BALLANTINES",
        1524: "ABSOLUT",
        3569: "ABSOLUT",
        4305: "ABSOLUT",
        1317: "ABSOLUT",
        1508: "ABSOLUT",
        2269: "ABSOLUT",
        8888: "ABSOLUT",
        6798: "ABSOLUT",
        6814: "ABSOLUT",
        1525: "ABSOLUT",
        2948: "ABSOLUT",
        5047: "ORLOFF",
        708: "ORLOFF",
        9725: "BALLANTINES",
        9770: "BALLANTINES",
        709: "BALLANTINES",
        1507: "BALLANTINES",
        1232: "BALLANTINES",
        4273: "BALLANTINES",
        9567: "BALLANTINES",
        84103: "BALLANTINES",
        9566: "BALLANTINES",
        9707: "CHIVAS",
        1746: "CHIVAS",
        4274: "CHIVAS",
        1526: "CHIVAS",
        3510: "CHIVAS"
    }


    mapeamento_categoria = {
        "SAO FRANCISCO": "NACIONAL",
        "DOMECQ": "NACIONAL",
        "PASSPORT": "NACIONAL",
        "ORLOFF": "NACIONAL",
        "NATU": "NACIONAL"
    }

    # Função para aplicar a lógica
    def classificar_categoria(marca):
        return mapeamento_categoria.get(marca, "OUTRO")

    # Arrumando DF
    df_final['EQUIPES'] = df_final['Nome Equipe'].map(mapeamento_equipes)
    df_final['MARCA'] = df_final['Produto'].map(mapeamento)
    df_final['LOCAL'] = df_final['MARCA'].apply(classificar_categoria)

    # convertendo filial para int
    df_final['Filial']=df_final['Filial'].astype(int)
    df_final['Cliente'] = df_final['Cliente'].astype(int)

    # retirando linhas de enventos
    df_filtrado = df_final.drop(df_final[df_final['Nome Equipe'] == 'EVENTOS PR'].index)

    # Resetando o índice do DataFrame resultante
    df_filtrado.reset_index(drop=True, inplace=True)

    # separando filiais
    df_filial_PR = df_filtrado[df_filtrado['Filial'] != 6]
    df_filial_SC = df_filtrado[df_filtrado['Filial'] == 6 ]


    # Volume
    volumes_PR = df_filial_PR.groupby('MARCA')['Volumes'].sum().reset_index()
    volumes_SC = df_filial_SC.groupby('MARCA')['Volumes'].sum().reset_index()


    marcas_interesse = ['ABSOLUT', 'BALLANTINES', 'BEEFEATER', 'CHIVAS', 'SAO FRANCISCO', 'DOMECQ', 'PASSPORT', 'ORLOFF', 'NATU']
    todas_marcas = pd.DataFrame({'MARCA': marcas_interesse})
    volumes_pr = pd.merge(todas_marcas, volumes_PR, on='MARCA', how='left')
    volumes_sc = pd.merge(todas_marcas, volumes_SC, on='MARCA', how='left')

    # volume Nacional
    volumes_nacional_SC = df_filial_SC[df_filial_SC['LOCAL'] == 'NACIONAL']['Volumes'].sum()
    volumes_nacional_PR = df_filial_PR[df_filial_PR['LOCAL'] == 'NACIONAL']['Volumes'].sum()


    volumes_sc = volumes_sc.infer_objects()
    volumes_pr = volumes_pr.infer_objects()
    volumes_pr['Volumes'] = volumes_pr['Volumes'].fillna(0)
    volumes_sc['Volumes'] = volumes_sc['Volumes'].fillna(0)


    nova_linha_df1 = {'MARCA': 'NACIONAL', 'Volumes': volumes_nacional_SC}
    nova_linha_df2 = {'MARCA': 'NACIONAL', 'Volumes': volumes_nacional_PR}

    # Adicionando as novas linhas a cada DataFrame
    volumes_pr = pd.concat([volumes_pr, pd.DataFrame([nova_linha_df2])], ignore_index=True)
    volumes_sc = pd.concat([volumes_sc, pd.DataFrame([nova_linha_df1])], ignore_index=True)

    # calculando positivação
    df_filial_SC_posi = df_filial_SC.drop_duplicates(subset='Cliente')
    df_filial_PR_posi = df_filial_PR.drop_duplicates(subset='Cliente')

    positivacao_sc = len(df_filial_SC_posi)
    positivacao_pr = len(df_filial_PR_posi)

    # inserindo metas
    # metas pra volumes
    metas = {
            'ABSOLUT' : 400,
            'BALLANTINES' : 300,
            'BEEFEATER' : 100,
            'CHIVAS' : 300,
            'NACIONAL' : 2200,
            'SAO FRANCISCO': 250,
            'DOMECQ': 300,
            'PASSPORT': 1000,
            'ORLOFF': 150,
            'NATU' : 500
    }

    volumes_sc['Meta_Volume'] = volumes_sc['MARCA'].map(metas)
    volumes_pr['Meta_Volume'] = volumes_pr['MARCA'].map(metas)

    # faltante 

 # renomeando coluna
    volumes_pr = volumes_pr.rename(columns={'Volumes': 'Volume Realizado'})
    volumes_sc = volumes_sc.rename(columns={'Volumes': 'Volume Realizado'})
   
    # coluna diferença
    volumes_sc['Faltante'] = volumes_sc['Volume Realizado'] - volumes_sc['Meta_Volume']
    volumes_pr['Faltante'] = volumes_pr['Volume Realizado'] - volumes_pr['Meta_Volume']


    # formatando dados
    volumes_pr['Faltante'] = volumes_pr['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    volumes_sc['Faltante'] = volumes_sc['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    volumes_pr['Volume Realizado'] = volumes_pr['Volume Realizado'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)
    volumes_sc['Volume Realizado'] = volumes_sc['Volume Realizado'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)


    # coluna %
    volumes_pr['Percentual'] = (volumes_pr['Volume Realizado'] / volumes_pr['Meta_Volume']) * 100
    volumes_sc['Percentual'] = (volumes_sc['Volume Realizado'] / volumes_sc['Meta_Volume']) * 100

    volumes_pr['Percentual'] =  volumes_pr['Percentual'].round()
    volumes_sc['Percentual'] =  volumes_sc['Percentual'].round()

    #coluna atingida
    volumes_pr['Atingida'] = volumes_pr['Faltante'].apply(lambda x: '✅' if x >= 0 else '❌')
    volumes_sc['Atingida'] = volumes_sc['Faltante'].apply(lambda x: '✅' if x >= 0 else '❌')

    
    return positivacao_sc, positivacao_pr, volumes_sc, volumes_pr

def clean_data_jack(): 
    # Ler o arquivo Excel
    df = pd.read_excel('relatorios\\TEMPLATE_JACK.xlsx')
    df_sem_primeira_linha = df.drop(index=0)
    novos_nomes_colunas = df_sem_primeira_linha.iloc[0]
    df_sem_primeira_linha.columns = novos_nomes_colunas
    df_final = df_sem_primeira_linha[1:].reset_index(drop=True)

    df_final['Filial'] = df_final['Filial'].replace({ 6 : 'BIGUAÇU', 7 : 'CURITIBA', 5 : 'CASCAVEL', 3 : 'CAMBE', 4 : 'CURITIBA'})

    clientes_distintos_por_filial = df_final.groupby('Filial')['Cliente'].nunique()

    clientes_distintos_por_filial = clientes_distintos_por_filial.reset_index()

    clientes_distintos_por_filial.columns = ['Filial', 'Positivações']

    Equipes_interesse = ["BIGUAÇU","CASCAVEL","LONDRINA","CAMBE","CURITIBA"]
    todas_Equipes = pd.DataFrame({'Filial': Equipes_interesse})

    positivacao_jack = pd.merge(todas_Equipes, clientes_distintos_por_filial, on='Filial', how='left').fillna(0) # arrumados os df 

    # metas
    metas = {
        'BIGUAÇU' : 100,
        'CASCAVEL' :100,
        'LONDRINA' :100,
        'CAMBE' : 100,
        'CURITIBA' :100 
    }

    positivacao_jack['Meta_positivação'] = positivacao_jack['Filial'].map(metas)
    # faltante
    positivacao_jack['Faltante'] = positivacao_jack['Positivações'] - positivacao_jack['Meta_positivação']

    positivacao_jack['Faltante'] = positivacao_jack['Faltante'].apply(lambda x: round(float(x)) if pd.notnull(x) else x)

    # percentual 
    positivacao_jack['Percentual'] = (positivacao_jack['Positivações'] / positivacao_jack['Meta_positivação']) * 100
    positivacao_jack['Percentual'] =  positivacao_jack['Percentual'].round()
    
    # atingida
    positivacao_jack['Atingida'] = positivacao_jack['Faltante'].apply(lambda x: '✅' if x >= 0 else '❌')



    return positivacao_jack

def clean_data_beam():
    df = pd.read_excel('relatorios\\TEMPLATE_BEAM SUNTORY.xlsx')

    # Remover a primeira linha do DataFrame e redefinir os nomes das colunas
    df_sem_primeira_linha = df.drop(index=0)
    novos_nomes_colunas = df_sem_primeira_linha.iloc[0]
    df_sem_primeira_linha.columns = novos_nomes_colunas
    df_final = df_sem_primeira_linha[1:].reset_index(drop=True)

    # Substituir valores na coluna 'Filial'
    df_final['Filial'] = df_final['Filial'].replace({6: 'BIGUAÇU', 7: 'CURITIBA', 5: 'CASCAVEL', 3: 'CAMBE', 4: 'CURITIBA'})

    # Contar clientes distintos por filial
    positivacao_beam = df_final.groupby('Filial')['Cliente'].nunique().reset_index(name='Positivações')

    # Definir as metas
    metas = {
        'BIGUAÇU': 100,
        'CASCAVEL': 100,
        'LONDRINA': 100,
        'CAMBE': 100,
        'CURITIBA': 100
    }

    # Adicionar a coluna de metas
    positivacao_beam['Meta_positivação'] = positivacao_beam['Filial'].map(metas)

    # Calcular o faltante
    positivacao_beam['Faltante'] = positivacao_beam['Meta_positivação'] - positivacao_beam['Positivações']

    # Calcular o percentual
    positivacao_beam['Percentual'] = (positivacao_beam['Positivações'] / positivacao_beam['Meta_positivação']) * 100
    positivacao_beam['Percentual'] = positivacao_beam['Percentual'].round()

    # Determinar se a meta foi atingida
    positivacao_beam['Atingida'] = positivacao_beam['Faltante'].apply(lambda x: '✅' if x <= 0 else '❌')

    return positivacao_beam

def clean_data_vct():
    df = pd.read_excel("relatorios\\VCT_PR_ONN_OFF.xlsx")
    df_sem_primeira_linha = df.drop(index=0)
    novos_nomes_colunas = df_sem_primeira_linha.iloc[0]
    df_sem_primeira_linha.columns = novos_nomes_colunas
    df_final = df_sem_primeira_linha[1:].reset_index(drop=True)

    mapeamento_equipes = {
        "PILS": "MC",
        "BAR ESPECIAL": "ON",
        "BAGGIO": "MC",
        "KEY ACCOUNT PR OFF": "OFF",
        "TROPICAL": "MC",
        "KEY ACCOUNT PR ON": "ON",
        "CASCAVEL": "MC",
        "MARINGA": "MC",
        "LONDRINA": "MC",
        "EXTRA": "MC",
        "HEINEKEN": "MC",
        "TELEVENDAS": "MC",
        "EVENTOS PR": "MC"
    }

    mapeamento_classes = {
        1381: "CELLAR",
        1573: "DEVILS",
        1575: "MARQUES",
        1901: "RESERVADO",
        1902: "RESERVADO",
        1903: "RESERVADO",
        1904: "RESERVADO",
        1905: "RESERVADO",
        1909: "GRAN RESERVA",
        1910: "CASILLERO DEL DIABLO",
        1911: "CASILLERO DEL DIABLO",
        1912: "CASILLERO DEL DIABLO",
        1913: "CASILLERO DEL DIABLO",
        1914: "CASILLERO DEL DIABLO",
        1915: "CASILLERO DEL DIABLO",
        1916: "RESERVADO",
        1918: "RESERVADO",
        1923: "MARQUES",
        1934: "MARQUES",
        1935: "MARQUES",
        1936: "MARQUES",
        1937: "DIABLO",
        2001: "TRIVENTO",
        2002: "TRIVENTO",
        2539: "CELLAR",
        2947: "CELLAR",
        2994: "RESERVADO",
        3039: "CASILLERO DEL DIABLO",
        3199: "MARQUES",
        3252: "MARQUES",
        3275: "DIABLO",
        3286: "CELLAR",
        3288: "CELLAR",
        3291: "MARQUES",
        3292: "CELLAR",
        3293: "CELLAR",
        3303: "GRAN RESERVA",
        3304: "CELLAR",
        3424: "CASILLERO DEL DIABLO",
        3425: "CASILLERO DEL DIABLO",
        3442: "TRIVENTO",
        3458: "CELLAR",
        3511: "CASILLERO DEL DIABLO",
        3512: "CASILLERO DEL DIABLO",
        3513: "CASILLERO DEL DIABLO",
        3602: "MARQUES",
        3620: "CELLAR",
        3702: "CELLAR",
        3703: "CELLAR",
        3704: "TRIVENTO",
        3754: "CASILLERO DEL DIABLO",
        3996: "CELLAR",
        4149: "DIABLO",
        4344: "CASILLERO DEL DIABLO",
        4345: "CASILLERO DEL DIABLO",
        4802: "CELLAR",
        4999: "TRIVENTO",
        5007: "RESERVADO",
        5043: "CELLAR",
        5073: "CELLAR",
        5074: "CELLAR",
        5075: "CELLAR",
        5076: "CELLAR",
        5077: "CELLAR",
        5078: "CELLAR",
        5079: "CELLAR",
        5080: "CELLAR",
        5081: "MARQUES",
        6787: "MARQUES",
        8719: "TRIVENTO",
        8720: "GRAN RESERVA",
        8926: "CELLAR",
        9525: "CELLAR",
        9526: "CELLAR",
        9527: "TRIVENTO",
        9528: "CELLAR",
        9529: "RESERVADO",
        9598: "DIABLO",
        9599: "CDD CARNIVAL",
        9600: "CDD CARNIVAL",
        9601: "CDD CARNIVAL",
        9602: "CDD CARNIVAL",
        9603: "CELLAR",
        9617: "CDD BELIGHT",
        9671: "CDD BELIGHT",
        9701: "RESERVADO",
        9825: "MARQUES",
        9826: "CELLAR",
        9827: "CELLAR",
        3278: "CASILLERO DEL DIABLO"
    }

    df_final['Classe'] = df_final['Produto'].map(mapeamento_classes)
    df_final['Equipe'] = df_final['Nome Equipe'].map(mapeamento_equipes)

    # Lista das marcas de interesse
    marcas_interesse = ["CASILLERO DEL DIABLO", "TRIVENTO", "RESERVADO", "DIABLO", "MARQUES"]

    # Agrupar por Marca e somar os volumes
    volumes_por_marca = df_final.groupby('Classe')['Volumes'].sum().reset_index()

    #Criar DataFrame com todas as marcas de interesse
    todas_marcas = pd.DataFrame({'Classe': marcas_interesse})

    # Combinar os resultados com todas as marcas de interesse
    volumes_completo = pd.merge(todas_marcas, volumes_por_marca, on='Classe', how='left')

    # Preencher valores ausentes com 0
    volumes_completo = volumes_completo.infer_objects()
    volumes_completo['Volumes'] = volumes_completo['Volumes'].fillna(0)

    # POSITIVACOES
    positivacao = df_final.groupby('Classe')['Cliente'].nunique().reset_index()
    marcas_interesse2 = ["CASILLERO DEL DIABLO", "TRIVENTO", "RESERVADO", "DIABLO", "MARQUES",'CDD CARNIVAL','CDD BELIGHT']
    todas_marcas2 = pd.DataFrame({'Classe': marcas_interesse2})
    positivacao_completo = pd.merge(todas_marcas2, positivacao, on='Classe', how='left')

    # Preencher valores ausentes com 0
    positivacao_completo['Cliente'] = positivacao_completo['Cliente'].fillna(0).infer_objects()
    positivacao_completo = positivacao_completo.sort_values(by='Classe').reset_index(drop=True)
    positivacao_completo.rename(columns={'Cliente': 'Positivação'}, inplace=True)

# Definir as metas positivação 
    metas_positivacao = {
        'RESERVADO': 100,
        'CASILLERO DEL DIABLO': 100,
        'MARQUES': 100,
        'TRIVENTO': 100,
        'CDD CARNIVAL': 100,
        'CDD BELIGHT' : 100,
        'DIABLO' : 100

    }

    # Adicionar a coluna de metas
    positivacao_completo['Meta_positivação'] = positivacao_completo['Classe'].map(metas_positivacao)

    # Calcular o faltante
    positivacao_completo['Faltante'] = positivacao_completo['Meta_positivação'] - positivacao_completo['Positivação']

    # Calcular o percentual
    positivacao_completo['Percentual'] = (positivacao_completo['Positivação'] / positivacao_completo['Meta_positivação']) * 100
    positivacao_completo['Percentual'] = positivacao_completo['Percentual'].round()

    # Determinar se a meta foi atingida
    positivacao_completo['Atingida'] = positivacao_completo['Faltante'].apply(lambda x: '✅' if x <= 0 else '❌')

    # Definir metas volume

    metas_volume = {
        'RESERVADO': 11500,
        'CASILLERO DEL DIABLO': 2800,
        'MARQUES': 45,
        'TRIVENTO': 100,
        'DIABLO' : 300,
        'CDD CARNIVAL': 0,
        'CDD BELIGHT' : 0
    }

    volumes_completo['Meta_Volume'] = volumes_completo['Classe'].map(metas_volume)

    # Calcular o faltante
    volumes_completo['Faltante'] = volumes_completo['Meta_Volume'] - volumes_completo['Volumes']

    # Calcular o percentual
    volumes_completo['Percentual'] = (volumes_completo['Volumes'] / volumes_completo['Meta_Volume']) * 100
    volumes_completo['Percentual'] = volumes_completo['Percentual'].round()

    # Determinar se a meta foi atingida
    volumes_completo['Volumes'] = volumes_completo['Volumes'].round()
    volumes_completo['Faltante'] = volumes_completo['Faltante'].round()

    volumes_completo['Atingida'] = volumes_completo['Faltante'].apply(lambda x: '✅' if x <= 0 else '❌')


    return positivacao_completo,volumes_completo


def clean_data_pernod_p4p():
    df = pd.read_excel("relatorios\\Pernod_p4p.xlsx")
    base_C9 = pd.read_excel("relatorios\\Produtos_Pernod_Com_Volume.xlsx")
    df_sem_primeira_linha = df.drop(index=0)
    novos_nomes_colunas = df_sem_primeira_linha.iloc[0]
    df_sem_primeira_linha.columns = novos_nomes_colunas
    df_final = df_sem_primeira_linha[1:].reset_index(drop=True)


    # Relaizando join para metricas C9
    df_resultado = pd.merge(df_final, base_C9, on='Produto', how='left')
    df_final = df_resultado
    mapeamento = {
        8702: "JAMESON",
        8740: "JAMESON",
        2715: "JAMESON",
        1696: "JAMESON",
        1051: "JAMESON",
        2714: "CHIVAS",
        4128: "CHIVAS",
        6815: "CHIVAS",
        4891: "CHIVAS",
        4958: "CHIVAS",
        740: "CHIVAS",
        1562: "CHIVAS",
        1892: "CHIVAS",
        9707: "CHIVAS",
        1746: "CHIVAS",
        4274: "CHIVAS",
        3510: "CHIVAS",
        659: "ABSOLUT",
        689: "ABSOLUT",
        702: "ABSOLUT",
        703: "ABSOLUT",
        704: "ABSOLUT",
        806: "ABSOLUT",
        812: "ABSOLUT",
        908: "ABSOLUT",
        914: "ABSOLUT",
        1240: "ABSOLUT",
        1317: "ABSOLUT",
        1318: "ABSOLUT",
        1348: "ABSOLUT",
        1508: "ABSOLUT",
        1524: "ABSOLUT",
        1525: "ABSOLUT",
        1560: "ABSOLUT",
        1747: "ABSOLUT",
        2269: "ABSOLUT",
        2477: "ABSOLUT",
        2948: "ABSOLUT",
        3520: "ABSOLUT",
        3533: "ABSOLUT",
        3540: "ABSOLUT",
        3541: "ABSOLUT",
        3543: "ABSOLUT",
        3569: "ABSOLUT",
        3726: "ABSOLUT",
        4305: "ABSOLUT",
        6158: "ABSOLUT",
        6159: "ABSOLUT",
        6160: "ABSOLUT",
        6798: "ABSOLUT",
        6814: "ABSOLUT",
        8888: "ABSOLUT",
        11525: "ABSOLUT",
        12269: "ABSOLUT",
        1298: "BEEFEATER",
        2347: "BEEFEATER",
        11298: "BEEFEATER",
        4574: "BEEFEATER",
        8929: "BEEFEATER",
        2348: "BEEFEATER",
        8856: "BEEFEATER",
        4780: "BEEFEATER",
        8701: "BEEFEATER",
        3181: "BEEFEATER",
        9725: "BALLANTINES",
        9770: "BALLANTINES",
        709: "BALLANTINES",
        2795: "BALLANTINES",
        1507: "BALLANTINES",
        1232: "BALLANTINES",
        4273: "BALLANTINES",
        723: "BALLANTINES",
        1561: "BALLANTINES",
        10723: "BALLANTINES",
        9567: "BALLANTINES",
        2794: "BALLANTINES",
        9566: "BALLANTINES",
        4957: "BALLANTINES",
        9611: "ROYAL SALUTE",
        9532: "ROYAL SALUTE",
        3169: "ROYAL SALUTE",
        3550: "ROYAL SALUTE",
        9610: "ROYAL SALUTE",
        4133: "ROYAL SALUTE",
        4746: "ROYAL SALUTE",
        10222: "ROYAL SALUTE",
        6166: "ROYAL SALUTE",
        6167: "ROYAL SALUTE",
        3302: "ROYAL SALUTE",
        1260: "GLENLIVET",
        3388: "GLENLIVET",
        3825: "GLENLIVET",
        3935: "GLENLIVET",
        4786: "GLENLIVET",
        701: "GLENLIVET",
        8884: "GLENLIVET",
        9308: "GLENLIVET",
        2481: "PERRIER JOUET",
        3572: "PERRIER JOUET",
        2479: "PERRIER JOUET",
        2594: "PERRIER JOUET",
        1396: "PERRIER JOUET",
        2480: "PERRIER JOUET",
        1397: "PERRIER JOUET",
        9614: "PERRIER JOUET"
    }


    mapeamento_main_priorites = {
        "JAMESON": "Main priorities",
        "ABSOLUT": "Main priorities",
        "BALLANTINES": "Main priorities",
        "BEEFEATER": "Main priorities",
        "ROYAL SALUTE": "Main priorities",
        "THE GLENLIVET": "Main priorities",
        "CHIVAS": "Main priorities",
        "PERRIER JOUET": "Main priorities"
    }

    #mapeando

    # Função para aplicar a lógica
    def classificar_categoria(marca):
        return mapeamento_main_priorites.get(marca, "OUTRO")



    df_final['Classificação'] = df_final['Produto'].map(mapeamento)

    df_final['Main priorities'] = df_final['Classificação'].apply(classificar_categoria).str.strip()

    df_final['Main priorities'] = df_final['Classificação'].apply(classificar_categoria)

    # classificar canal
    mapeando_canal = {
        44: "On Trade",
        42: "On Trade",
        43: "On Trade",
        41: "On Trade",
        46: "On Trade",
        45: "On Trade",
        53: "On Trade",
        52: "On Trade",
        51: "On Trade",
        82: "On Trade",
        84: "On Trade",
        83: "On Trade",
        30: "On Trade",
        81: "On Trade",
        91: "On Trade",
        92: "On Trade",
        61: "On Trade",
        62: "On Trade",
        63: "On Trade",
        101: "On Trade",
        103: "On Trade",
        95: "On Trade",
        102: "On Trade",
        93: "On Trade",
        64: "Off Trade",
        31: "Off Trade",
        32: "Off Trade",
        33: "Off Trade",
        25: "Off Trade",
        34: "Off Trade",
        35: "Off Trade",
        36: "Off Trade",
        21: "Off Trade",
        23: "Off Trade",
        22: "Off Trade",
        24: "Off Trade",
        26: "Off Trade",
        71: "Off Trade",
        72: "Off Trade",
        73: "Off Trade"
    }

    df_final['Canal'] = df_final['Tipo Estabelecimento'].map(mapeando_canal)
    # aplicando lógica para eventos
    # Função para alterar o tipo com base na equipe
    def alterar_tipo(row):
        if 'EVENTOS PR' in row['Nome Equipe']:  # Verifica se 'eventos' está na coluna equipe
            return 'EVENTOS PR'  # Altera o tipo para 'eventos'
        return row['Canal']  # Retorna o tipo atual se não for 'eventos'

    # Aplicando a função para atualizar a coluna tipo
    df_final['Canal'] = df_final.apply(alterar_tipo, axis=1)

    # flitrar filial
    df_SC = df_final[df_final['Filial'] == 6]
    df_PR = df_final[df_final['Filial'] != 6]


    # realizar análise PR

    # separando df's
    df_PR_on_trade = df_PR[df_PR['Canal'] == 'On Trade']
    df_PR_off_trade = df_PR[df_PR['Canal'] == 'Off Trade']
    df_PR_eventos = df_PR[df_PR['Canal'] == 'EVENTOS PR']


    # calculando volume
    # criando df para cada
    df_on_trade_marca = df_PR_on_trade.groupby('Classificação')['Volume C9'].sum().reset_index()

    # DataFrame para OffTrade
    df_off_trade_marca = df_PR_off_trade.groupby('Classificação')['Volume C9'].sum().reset_index()

    # DataFrame para Eventos
    df_eventos_marca = df_PR_eventos.groupby('Classificação')['Volume C9'].sum().reset_index()

    # meta volume 
    metas_volume_pr_off = {
        "JAMESON": 116.8 ,
        "ABSOLUT": 390.1,
        "BALLANTINES": 937.2,
        "BEEFEATER": 164.6,
        "ROYAL SALUTE": 1.2,
        "THE GLENLIVET": 1.3,
        "CHIVAS": 335.6,
        "PERRIER JOUET": 3.5 
    }

    metas_volume_pr_eventos = {
        "JAMESON": 10.4,
        "ABSOLUT": 44.4,
        "BALLANTINES": 28.1,
        "BEEFEATER": 14.6,
        "ROYAL SALUTE": 0.7,
        "THE GLENLIVET": 0.0,
        "CHIVAS": 10.1,
        "PERRIER JOUET":0.4 
    }

    metas_volume_pr_on = {
        "JAMESON": 84.9,
        "ABSOLUT": 301.1,
        "BALLANTINES":300.7,
        "BEEFEATER": 75.8,
        "ROYAL SALUTE": 0.5,
        "THE GLENLIVET": 0.1,
        "CHIVAS": 107.7,
        "PERRIER JOUET": 0.8
    }

    
    # garantindo que todas as marcas constem no df  

    todas_as_marcas = ['JAMESON', 'ABSOLUT', 'BALLANTINES', 'BEEFEATER', "ROYAL SALUTE" , "THE GLENLIVET" , "CHIVAS", "PERRIER JOUET"]

    df_completo = pd.DataFrame({'Classificação': todas_as_marcas})

    # Fazendo o merge com o DataFrame original
    df_eventos_marca = pd.merge(df_completo, df_eventos_marca, on='Classificação', how='left')
    df_off_trade_marca = pd.merge(df_completo, df_off_trade_marca, on='Classificação', how='left')
    df_on_trade_marca = pd.merge(df_completo, df_on_trade_marca, on='Classificação', how='left')

    # Adicionar a coluna de metas
    df_on_trade_marca['Meta Volume'] = df_on_trade_marca['Classificação'].map(metas_volume_pr_on)
    df_eventos_marca['Meta Volume'] = df_eventos_marca['Classificação'].map(metas_volume_pr_eventos)
    df_off_trade_marca['Meta Volume'] = df_off_trade_marca['Classificação'].map(metas_volume_pr_off)

        # %volume on
    df_on_trade_marca['Percentual'] = (df_on_trade_marca['Volume C9'] / df_on_trade_marca['Meta Volume']) * 100
    df_on_trade_marca['Percentual'] = df_on_trade_marca['Percentual'].round()
    
        # %volume eventos
    df_eventos_marca['Percentual'] = (df_eventos_marca['Volume C9'] / df_eventos_marca['Meta Volume']) * 100
    df_eventos_marca['Percentual'] = df_eventos_marca['Percentual'].round()
    
        # %volume off
    df_off_trade_marca['Percentual'] = (df_off_trade_marca['Volume C9'] / df_off_trade_marca['Meta Volume']) * 100
    df_off_trade_marca['Percentual'] = df_off_trade_marca['Percentual'].round()


    #calculando_positivação

    df_on_trade_positivacao = df_PR_on_trade.groupby('Classificação')['Cliente'].nunique().reset_index()
    df_on_trade_positivacao.rename(columns={'Cliente': 'Positivação'}, inplace=True)

    df_off_trade_positivacao = df_PR_off_trade.groupby('Classificação')['Cliente'].nunique().reset_index()
    df_off_trade_positivacao.rename(columns={'Cliente': 'Positivação'}, inplace=True)

    # merge Dfs
    df_on_trade_marca = df_on_trade_marca.merge(
        df_on_trade_positivacao[['Classificação', 'Positivação']], 
        on='Classificação', 
        how='left')
    
    df_off_trade_marca = df_off_trade_marca.merge(
        df_off_trade_positivacao[['Classificação', 'Positivação']], 
        on='Classificação', 
        how='left')
        


    # valores dos cards (volume e positivação)
    resultados_on_pr = df_PR[(df_PR['Canal'] == 'On Trade') & (df_PR['Main priorities'] == 'Main priorities')].agg({
        'Volume C9': 'sum',
        'Cliente': 'nunique'
    })


    resultados_off_pr = df_PR[(df_PR['Canal'] == 'Off Trade') & (df_PR['Main priorities'] == 'Main priorities')].agg({
        'Volume C9': 'sum',
        'Cliente': 'nunique'
    })

    resultados_eventos_pr = df_PR[(df_PR['Canal'] == 'EVENTOS PR') & (df_PR['Main priorities'] == 'Main priorities')].agg({'Volume C9': 'sum'})

    # card Jameson
    resultados_jameson_off_pr = df_PR.loc[(df_PR['Canal'] == 'Off Trade') & (df_PR['Classificação'] == 'JAMESON'), 'Volume C9'].sum()
    resultados_jameson_on_pr = df_PR.loc[(df_PR['Canal'] == 'Off Trade') & (df_PR['Classificação'] == 'JAMESON'), 'Volume C9'].sum()
    resultados_jameson_eventos_pr = df_PR.loc[(df_PR['Canal'] == 'Off Trade') & (df_PR['Classificação'] == 'JAMESON'), 'Volume C9'].sum()

    # card positivaçõa 

    resultado_posi_off_pr =  df_PR_off_trade['Cliente'].nunique()
    resultado_posi_on_pr =  df_PR_on_trade['Cliente'].nunique()
    
 

    # % Share

    # tempo de eventos


    # Análise SANTA CATARINA

    # volumes por canal
    df_Volume_sc_main = df_SC.groupby(['Canal', 'Main priorities'])['Volume C9'].sum().reset_index()
    # separando df's
    df_SC_off_trade = df_SC[df_SC['Canal'] == 'Off Trade']

    # calculando volume
    # DataFrame para OffTrade
    df_off_trade_marca_volume_sc = df_SC_off_trade.groupby('Classificação')['Volume C9'].sum().reset_index()


    #calculando_positivação

    df_off_trade_positivacao_sc = df_SC_off_trade.groupby('Classificação')['Cliente'].nunique().reset_index()
    df_off_trade_positivacao_sc.rename(columns={'Cliente': 'Positivação'}, inplace=True)


    # volumes por canal
    df_Volume_sc_main = df_SC.groupby(['Canal', 'Main priorities'])['Volume C9'].sum().reset_index()
    # positivação  por Classificação
    df_positivacao_sc_main = df_SC.groupby(['Canal', 'Main priorities'])['Cliente'].nunique().reset_index()


    # % Share 

    return df_on_trade_marca,df_off_trade_marca,df_eventos_marca, df_Volume_sc_main, df_off_trade_marca_volume_sc, df_positivacao_sc_main, resultados_on_pr, resultados_off_pr, resultados_eventos_pr,resultados_jameson_off_pr,resultados_jameson_eventos_pr,resultados_jameson_on_pr,resultado_posi_off_pr, resultado_posi_on_pr

def clean_data_hnk_geral():
    df = pd.read_excel('relatorios\\Hnk_geral.xlsx')


    clientes_sem_class = df.groupby('Mês')['Cliente'].nunique().reset_index()

    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    clientes_sem_class['Mês'] = pd.Categorical(clientes_sem_class['Mês'], categories=meses, ordered=True)

    # Ordenando o DataFrame
    clientes_por_mes = clientes_sem_class.sort_values('Mês')

    julho_clientes_posi_geral = clientes_por_mes.loc[clientes_por_mes['Mês'] == 'Julho', 'Cliente'].values[0]
    outubro_clientes_posi_geral = clientes_por_mes.loc[clientes_por_mes['Mês'] == 'Outubro', 'Cliente'].values[0]


    # Calcular o crescimento absoluto
    crescimento_absoluto_posi_geral = outubro_clientes_posi_geral - julho_clientes_posi_geral

    # Calcular a média de crescimento percentual
    crescimento_percentual_posi_geral = (crescimento_absoluto_posi_geral / julho_clientes_posi_geral) * 100
    

    volume_sem_clas = df.groupby('Mês')['Hecto total'].sum().reset_index()

    volume_sem_clas['Mês'] = pd.Categorical(volume_sem_clas['Mês'], categories=meses, ordered=True)

    # Ordenando o DataFrame
    volume_por_mes = volume_sem_clas.sort_values('Mês')


    # Calcular a média de crescimento percentual

    julho_volumes_geral = volume_por_mes.loc[volume_por_mes['Mês'] == 'Julho', 'Hecto total'].values[0]
    outubro_volumes_geral = volume_por_mes.loc[volume_por_mes['Mês'] == 'Outubro', 'Hecto total'].values[0]

    # Calcular o crescimento absoluto para Volumes
    crescimento_absoluto_volumes_geral = outubro_volumes_geral - julho_volumes_geral

    # Calcular a média de crescimento percentual para Volumes
    crescimento_percentual_volumes_geral = (crescimento_absoluto_volumes_geral / julho_volumes_geral) * 100

    crescimento_percentual_volumes_geral.round(2)

    # análises de top 15 clientes com maiores volumes. 
    df_top15 = df.groupby(['Cliente', 'Nome Cliente'])['Volumes'].sum().reset_index()

    df_top_15 = df_top15.sort_values(by='Volumes', ascending=False)

    # 3. Selecionar os top 15 clientes
    df_top_15 = df_top_15.head(15)

    df_top_15 = df_top_15.reset_index(drop=True)
    df_top_15.index = df_top_15.index + 1  # Ajusta o índice para começar em 1

    df_top_15['Cliente'] = df_top_15['Cliente'].astype(str)

    return clientes_por_mes, crescimento_percentual_posi_geral, volume_por_mes, crescimento_percentual_volumes_geral, df_top_15

def clean_data_hnk_mes():
    df = pd.read_excel('relatorios\\Hnk_Mes.xlsx')

    # positivações produtos
    produtos_posi = df.groupby('Nome Produto')['Cliente'].nunique().reset_index()

    # Renomeando as colunas para facilitar o entendimento
    produtos_posi.columns = ['Produto', 'Positivação']

    # positivações cidades
    cidades_posi = df.groupby('Nome Cidade')['Cliente'].nunique().reset_index()

    # Renomeando as colunas para facilitar o entendimento
    cidades_posi.columns = ['Cidade', 'Positivação']

    # positivações vendedores
    vendedores_posi = df.groupby('Nome Vendedor')['Cliente'].nunique().reset_index()

    # Renomeando as colunas para facilitar o entendimento
    vendedores_posi.columns = ['Vendedor', 'Positivação']

    return produtos_posi , cidades_posi, vendedores_posi

    

def Mandar_share():
   # Configurações
    site_url = "https://grupolorac.sharepoint.com/sites/Dinho"
    username = "kewin.delazer@grupolorac.onmicrosoft.com"
    password = '@@Bebidas2024'
    sharepoint_folder = "/sites/Dinho/Documentos Compartilhados/Dados/Comercial/Equipes/Gerencial/4 TRI 2024/Gráficos ( BETA )"
    local_folder = "C:/Users/dinho/Desktop/Projeto_vizualização/graficos"

    # Autenticação
    ctx_auth = AuthenticationContext(site_url)
    if not ctx_auth.acquire_token_for_user(username, password):
        print("Autenticação falhou")
        exit()

    ctx = ClientContext(site_url, ctx_auth)

    # Envio dos Arquivos
    for file_name in os.listdir(local_folder):
        file_path = os.path.join(local_folder, file_name)
        
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file_content:
                target_folder = ctx.web.get_folder_by_server_relative_url(sharepoint_folder)
                target_file = target_folder.upload_file(file_name, file_content)
                ctx.execute_query()
                print(f"Arquivo '{file_name}' enviado com sucesso!")
        else:
            print(f"'{file_name}' não é um arquivo. Ignorado.")





def cards_2(*args):
    # Dividir os argumentos em grupos de três (label, value, meta)
    metrics = [args[i:i+3] for i in range(0, len(args), 3)]
    
    # Criar colunas para os cards
    col1, col2 = st.columns(2)
    
    # Alternar entre as colunas
    for index, (label, value, meta) in enumerate(metrics):
        if index % 2 == 0:  # Índice par, coluna 1
            with col1:
                st.metric(label=f"{label}", value=f"{round(value)}/{meta}", delta=f"{round(value) - meta}")
        else:  # Índice ímpar, coluna 2
            with col2:
                st.metric(label=f"{label}", value=f"{round(value)}/{meta}", delta=f"{round(value) - meta}")
        # Exemplo de uso da função
            '''
            cards_2(
                'Volume Total', volume_pr, 8220, 
                'Volume Skyy', total_volume_sky_pr, 610, 
                'Volume Extra', extra_volume_pr, 3000, 
                'Volume Especial', special_volume_pr, 1500
            )
        '''
            
def cards_3(*args):
    # Organizar os argumentos em grupos de 3
    metrics = [args[i:i+3] for i in range(0, len(args), 3)]
    
    # Criar 3 colunas
    col1, col2, col3 = st.columns(3)
    
    # Alternar entre as colunas
    for index, (label, value, meta) in enumerate(metrics):
        if index % 3 == 0:  # Índice 0, coluna 1
            with col1:
                st.metric(label=f"{label}", value=f"{round(value)}/{meta}", delta=f"{round(value) - meta}")
        elif index % 3 == 1:  # Índice 1, coluna 2
            with col2:
                st.metric(label=f"{label}", value=f"{round(value)}/{meta}", delta=f"{round(value) - meta}")
        else:  # Índice 2, coluna 3
            with col3:
                st.metric(label=f"{label}", value=f"{round(value)}/{meta}", delta=f"{round(value) - meta}")
