import pandas as pd 

def clean_data_pernod_p4p():
    df = pd.read_excel("template_pernod.xlsx")
    base_C9 = pd.read_excel("Produtos_Pernod_Com_Volume.xlsx")
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
    df_on_trade_marca_volume = df_PR_on_trade.groupby('Classificação')['Volume C9'].sum().reset_index()

    # DataFrame para OffTrade
    df_off_trade_marca_volume = df_PR_off_trade.groupby('Classificação')['Volume C9'].sum().reset_index()

    # DataFrame para Eventos
    df_eventos_marca_volume = df_PR_eventos.groupby('Classificação')['Volume C9'].sum().reset_index()


    #calculando_positivação

    df_on_trade_positivacao = df_PR_on_trade.groupby('Classificação')['Cliente'].nunique().reset_index()
    df_on_trade_positivacao.rename(columns={'Cliente': 'Positivação'}, inplace=True)

    df_off_trade_positivacao = df_PR_off_trade.groupby('Classificação')['Cliente'].nunique().reset_index()
    df_off_trade_positivacao.rename(columns={'Cliente': 'Positivação'}, inplace=True)


    # volumes por canal
    df_Volume_pr_main = df_PR.groupby(['Canal', 'Main priorities'])['Volume C9'].sum().reset_index()
    # positivação  por Classificação
    df_positivacao_pr_main = df_PR.groupby(['Canal', 'Main priorities'])['Cliente'].nunique().reset_index()


    # % Share

    # tempo de eventos

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


    # tempo de eventos

    # % Share 

    return df_on_trade_marca_volume,df_off_trade_marca_volume,df_eventos_marca_volume, df_Volume_pr_main, df_positivacao_pr_main, df_Volume_sc_main, df_off_trade_marca_volume_sc, df_positivacao_sc_main
