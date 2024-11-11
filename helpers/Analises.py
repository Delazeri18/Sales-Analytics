import pandas as pd 
import plotly.graph_objects as go
import os 
import plotly.io as pio
from datetime import datetime  # VER filtro filial, precisa ser ESTADO 

hoje = datetime.now().date()

def jack_graph(df, equipe):
        pasta_graficos = os.path.join('graficos')
        # nome que será usado dentro do arquivo do grafico.
        nome_arquivo = 'JACK'

        # filtrando por apenas aquilo que vai ser usado. 
        df_filtered_jack = df[(df['Industria'] == 'JACK') & (df['Nome Equipe'] == equipe)].copy()
        # definindo metas 
        df_filtered_jack['Meta_Positivacao'] = df_filtered_jack['Nome Equipe'].map({'PILS': 437, 'BAGGIO': 296, 'LONDRINA': 235, 'MARINGA' : 235, 'TROPICAL' : 235, 'CASCAVEL' : 316, 'KEY ACCOUNT PR OFF' : 77, 'KEY ACCOUNT PR ON' : 194})
        df_filtered_jack['Meta_Volume'] = df_filtered_jack['Nome Equipe'].map({'PILS': 169, 'BAGGIO': 91, 'LONDRINA': 91, 'MARINGA' : 91, 'TROPICAL' : 91, 'CASCAVEL' : 130, 'KEY ACCOUNT PR OFF' : 455, 'KEY ACCOUNT PR ON' : 182})
            
            # Agrupamento específico para o fabricante 'JACK'
        df_group_fab_a = df_filtered_jack[df_filtered_jack['Industria'] == 'JACK'].groupby('Nome Equipe').agg(
            Positivacoes=('Cliente', 'nunique'),  # Positivações por cliente
            Volume_Total=('Volumes', 'sum'),  # Volume total
            Meta_Positivacao = ('Meta_Positivacao','mean'),
            Meta_Volume = ('Meta_Volume','mean')
        ).reset_index()
            
        df_group_fab_a['Volume_Total'] = df_group_fab_a['Volume_Total'].apply(lambda x: f"{x:.2f}")
            
        # Criar o gráfico de barras com metas
        fig_volume = go.Figure()

        # Adicionar barras de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Nome Equipe'],
            y=df_group_fab_a['Volume_Total'].astype(float),  # Converter para float para gráficos
            name='Volume Total',
            text=df_group_fab_a['Volume_Total'],
            textposition='auto',
            marker_color='#3498db',
            width=0.2 ,# Ajuste a largura das barras de volume
            offsetgroup= '1' 
        ))

            # Adicionar barras de meta de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Nome Equipe'],
            y=df_group_fab_a['Meta_Volume'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Volume'],                
            textposition='auto',
            marker_color='#90ee90',
            width=0.2,  # Ajuste a largura das barras de meta
            offsetgroup = '2'
        ))

        fig_volume.update_layout(
            title=f'Volume e Metas Jack equipe: {equipe}',
            xaxis_title='Nome Equipe',
            yaxis_title='Valores',
            barmode='group',
            bargap=0.05,  # Pequeno espaço entre grupos de barras
            bargroupgap=0.0,  # Remove o espaço entre as barras dentro do grupo
            width=800,
            height=600            
        )
        fig_positivação = go.Figure()

        # Adicionar barras de positivação 
        fig_positivação.add_trace(go.Bar(
            x=df_group_fab_a['Nome Equipe'],
            y=df_group_fab_a['Positivacoes'].astype(float),  # Converter para float para gráficos
            name='Positivaçoes',
            text=df_group_fab_a['Positivacoes'],
            textposition='auto',
            marker_color='#3498db',
            width=0.3 
        ))


                    # Adicionar barras de meta de volume
        fig_positivação.add_trace(go.Bar(
            x=df_group_fab_a['Nome Equipe'],
            y=df_group_fab_a['Meta_Positivacao'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Positivacao'],
            textposition='auto',
            marker_color='#90ee90',
            width=0.2  # Ajuste a largura das barras de meta
        ))

        fig_positivação.update_layout(
            title=f'Positivações e Metas Jack equipe: {equipe}',
            xaxis_title='Nome Equipe',
            yaxis_title='Valores',
            barmode='group',
            bargap=0.2  # Espaço entre grupos de barras
        )
            # Atualizar o layout do gráfico
        fig_volume.update_layout(
            title='Volume e Metas',
            xaxis_title='Nome Equipe',               
            yaxis_title='Valores',
            barmode='group',  # Certifica que as barras fiquem lado a lado
            bargap=0.15,  # Espaço entre grupos de barras
            bargroupgap=0.1,  # Espaço entre as barras dentro de um grupo
            width=800,
            height=600            
        )

        # criando caminho e nomes.
        caminho_imagem1 = os.path.join(pasta_graficos, f"Posit_{equipe}_{nome_arquivo}__{hoje}.png")
        caminho_imagem2 = os.path.join(pasta_graficos, f"Vol_{equipe}_{nome_arquivo}__{hoje}.png")

        # mandando gráficos.
        pio.kaleido.scope.chromium_args += ("--single-process",) # imagem estática 
        fig_positivação.write_image(caminho_imagem1, engine="kaleido") 
        fig_volume.write_image(caminho_imagem2, engine="kaleido")

def beam_graph(df,equipe):
        # nome que será usado dentro do arquivo do grafico.
        pasta_graficos = os.path.join('graficos')
        nome_arquivo = 'BEAM SUNTORY'
        # Criando cópia para não dar erro:
        df_filtered_BEAM = df[(df['Industria'] == 'BEAM') & (df['Nome Equipe'] == equipe)].copy()


        # definindo metas 
        df_filtered_BEAM['Meta_Positivacao'] = df_filtered_BEAM['Nome Equipe'].map({'PILS': 119, 'BAGGIO': 80, 'LONDRINA': 64, 'MARINGA' : 64, 'TROPICAL' : 64, 'CASCAVEL' : 86, 'KEY ACCOUNT PR OFF' : 21, 'KEY ACCOUNT PR ON' : 53})
        df_filtered_BEAM['Meta_Volume'] = df_filtered_BEAM['Nome Equipe'].map({'PILS': 39, 'BAGGIO': 21, 'LONDRINA': 21, 'MARINGA' : 21, 'TROPICAL' : 21, 'CASCAVEL' : 30, 'KEY ACCOUNT PR OFF' : 105, 'KEY ACCOUNT PR ON' : 42})
            
            # Agrupamento específico para o fabricante 'Beam Suntory'
        df_group_fab_a = df_filtered_BEAM[df_filtered_BEAM['Industria'] == 'BEAM SUNTORY'].groupby('Nome Equipe').agg(
            Positivacoes=('Cliente', 'nunique'),  # Positivações por cliente
            Volume_Total=('Volumes', 'sum'),  # Volume total
            Meta_Positivacao = ('Meta_Positivacao','mean'),
            Meta_Volume = ('Meta_Volume','mean')
        ).reset_index()
            
        df_group_fab_a['Volume_Total'] = df_group_fab_a['Volume_Total'].apply(lambda x: f"{x:.2f}")
            
        # Criar o gráfico de barras com metas
        fig_volume = go.Figure()

        # Adicionar barras de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Nome Equipe'],
            y=df_group_fab_a['Volume_Total'].astype(float),  # Converter para float para gráficos
            name='Volume Total',
            text=df_group_fab_a['Volume_Total'],
            textposition='auto',
            marker_color='#3498db',
            width=0.2 # Ajuste a largura das barras de volume
        ))

            # Adicionar barras de meta de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Nome Equipe'],
            y=df_group_fab_a['Meta_Volume'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Volume'],
            textposition='auto',
            marker_color='#90ee90',
            width=0.2  # Ajuste a largura das barras de meta
        ))

        fig_volume.update_layout(
            title=f'Volume e Metas Beam {equipe}',
            xaxis_title='Nome Equipe',
            yaxis_title='Valores',
            barmode='group',
            bargap=0.2,  # Espaço entre grupos de barras
            width=800,
            height=600            
        )

        fig_positivação = go.Figure()
        # Adicionar barras de positivação 
        fig_positivação.add_trace(go.Bar(
            x=df_group_fab_a['Nome Equipe'],
            y=df_group_fab_a['Positivacoes'].astype(float),  # Converter para float para gráficos
            name='Positivaçoes',
            text=df_group_fab_a['Positivacoes'],
            textposition='auto',
            marker_color='#3498db',
            width=0.2
        ))


                    # Adicionar barras de meta de volume
        fig_positivação.add_trace(go.Bar(
            x=df_group_fab_a['Nome Equipe'],
            y=df_group_fab_a['Meta_Positivacao'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Positivacao'],
            textposition='auto',
            marker_color='#90ee90',
            width=0.2  # Ajuste a largura das barras de meta
        ))

        fig_positivação.update_layout(
            title=f'Positivações e Metas Beam equipe:{equipe}',
            xaxis_title='Nome Equipe',
            yaxis_title='Valores',
            barmode='group',
            bargap=0.2,  # Espaço entre grupos de barras
            width=800,
            height=600            
        )

        caminho_imagem1 = os.path.join(pasta_graficos, f"Posit_{equipe}_{nome_arquivo}__{hoje}.png")
        caminho_imagem2 = os.path.join(pasta_graficos, f"Vol_{equipe}_{nome_arquivo}__{hoje}.png")

            # mandando gráficos.
        pio.kaleido.scope.chromium_args += ("--single-process",) # imagem estática 
        fig_positivação.write_image(caminho_imagem1) 
        fig_volume.write_image(caminho_imagem2)

def vct_graph(df, equipe):
        # nome que será usado dentro do arquivo do grafico.
        pasta_graficos = os.path.join('graficos')
        nome_arquivo = 'VCT'
        # Criando cópia para não dar erro:
        df_filtered_VCT = df[(df['Industria'] == 'VCT') & (df['Nome Equipe'] == equipe)].copy()
        meta_por_marca_equipe = {
                ('RESERVADO', 'PILS'): {'Meta_Volume': 1065, 'Meta_Positivacao': 315},
                ('RESERVADO', 'BAGGIO'): {'Meta_Volume': 533, 'Meta_Positivacao': 90},
                ('RESERVADO', 'LONDRINA'): {'Meta_Volume': 533, 'Meta_Positivacao' : 195},
                ('RESERVADO', 'MARINGA'): {'Meta_Volume': 533, 'Meta_Positivacao': 180},  # #RESERVADO, CASILLERO MARQUES TRIVENTO CELLAR DIABLO CDD CARNIVAL CDD BELIGHT GRAN RESERVA 
                ('RESERVADO', 'TROPICAL'): {'Meta_Volume': 533, 'Meta_Positivacao': 180},
                ('RESERVADO', 'CASCAVEL'): {'Meta_Volume': 1065, 'Meta_Positivacao': 240},
                ('RESERVADO', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 4172, 'Meta_Positivacao': 75},
                ('RESERVADO', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 444, 'Meta_Positivacao': 120},

                ('CASILLERO', 'PILS'): {'Meta_Volume': 500, 'Meta_Positivacao': 253},
                ('CASILLERO', 'BAGGIO'): {'Meta_Volume': 250, 'Meta_Positivacao': 72},
                ('CASILLERO', 'LONDRINA'): {'Meta_Volume': 250, 'Meta_Positivacao': 157},
                ('CASILLERO', 'MARINGA'): {'Meta_Volume': 250, 'Meta_Positivacao': 145},  # #RESERVADO, CASILLERO MARQUES TRIVENTO CELLAR DIABLO CDD CARNIVAL CDD BELIGHT GRAN RESERVA 
                ('CASILLERO', 'TROPICAL'): {'Meta_Volume': 250, 'Meta_Positivacao': 145},
                ('CASILLERO', 'CASCAVEL'): {'Meta_Volume': 500, 'Meta_Positivacao': 193},
                ('CASILLERO', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 1957, 'Meta_Positivacao': 60},
                ('CASILLERO', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 208, 'Meta_Positivacao': 96},

                ('MARQUES', 'PILS'): {'Meta_Volume': 13, 'Meta_Positivacao': 16},
                ('MARQUES', 'BAGGIO'): {'Meta_Volume': 5, 'Meta_Positivacao': 5},
                ('MARQUES', 'LONDRINA'): {'Meta_Volume': 7, 'Meta_Positivacao': 10},
                ('MARQUES', 'MARINGA'): {'Meta_Volume': 7, 'Meta_Positivacao': 9},  # #RESERVADO, CASILLERO MARQUES TRIVENTO CELLAR DIABLO CDD CARNIVAL CDD BELIGHT GRAN RESERVA 
                ('MARQUES', 'TROPICAL'): {'Meta_Volume': 7, 'Meta_Positivacao': 9},
                ('MARQUES', 'CASCAVEL'): {'Meta_Volume': 13, 'Meta_Positivacao': 12},
                ('MARQUES', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 52, 'Meta_Positivacao': 4},
                ('MARQUES', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 6, 'Meta_Positivacao': 6},

                ('TRIVENTO', 'PILS'): {'Meta_Volume': 70, 'Meta_Positivacao': 76},
                ('TRIVENTO', 'BAGGIO'): {'Meta_Volume': 35, 'Meta_Positivacao': 22},
                ('TRIVENTO', 'LONDRINA'): {'Meta_Volume': 35, 'Meta_Positivacao': 47},
                ('TRIVENTO', 'MARINGA'): {'Meta_Volume': 35, 'Meta_Positivacao': 43},  # #RESERVADO, CASILLERO MARQUES TRIVENTO CELLAR DIABLO CDD CARNIVAL CDD BELIGHT GRAN RESERVA 
                ('TRIVENTO', 'TROPICAL'): {'Meta_Volume': 35, 'Meta_Positivacao': 43},
                ('TRIVENTO', 'CASCAVEL'): {'Meta_Volume': 70, 'Meta_Positivacao': 58},
                ('TRIVENTO', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 274, 'Meta_Positivacao': 18},
                ('TRIVENTO', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 29, 'Meta_Positivacao': 29},

                ('DIABLO', 'PILS'): {'Meta_Volume': 48, 'Meta_Positivacao': 76},
                ('DIABLO', 'BAGGIO'): {'Meta_Volume': 24, 'Meta_Positivacao': 22},
                ('DIABLO', 'LONDRINA'): {'Meta_Volume': 24, 'Meta_Positivacao': 47},
                ('DIABLO', 'MARINGA'): {'Meta_Volume': 24, 'Meta_Positivacao': 43},  # #RESERVADO, CASILLERO MARQUES TRIVENTO CELLAR DIABLO CDD CARNIVAL CDD BELIGHT GRAN RESERVA 
                ('DIABLO', 'TROPICAL'): {'Meta_Volume': 24, 'Meta_Positivacao': 43},
                ('DIABLO', 'CASCAVEL'): {'Meta_Volume': 48, 'Meta_Positivacao': 58},
                ('DIABLO', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 187, 'Meta_Positivacao': 18},
                ('DIABLO', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 20, 'Meta_Positivacao': 29},

                ('CDD CARNIVAL', 'PILS'): {'Meta_Volume': 0, 'Meta_Positivacao':76},
                ('CDD CARNIVAL', 'BAGGIO'): {'Meta_Volume': 0, 'Meta_Positivacao': 22},
                ('CDD CARNIVAL', 'LONDRINA'): {'Meta_Volume': 0, 'Meta_Positivacao': 47},
                ('CDD CARNIVAL', 'MARINGA'): {'Meta_Volume': 0, 'Meta_Positivacao': 43}, 
                ('CDD CARNIVAL', 'TROPICAL'): {'Meta_Volume': 0, 'Meta_Positivacao': 43},
                ('CDD CARNIVAL', 'CASCAVEL'): {'Meta_Volume': 0, 'Meta_Positivacao': 58},
                ('CDD CARNIVAL', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 0, 'Meta_Positivacao': 18},
                ('CDD CARNIVAL', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 0, 'Meta_Positivacao': 29},

                ('CDD BELIGHT', 'PILS'): {'Meta_Volume': 0, 'Meta_Positivacao': 76},
                ('CDD BELIGHT', 'BAGGIO'): {'Meta_Volume': 0, 'Meta_Positivacao': 22},
                ('CDD BELIGHT', 'LONDRINA'): {'Meta_Volume': 0, 'Meta_Positivacao': 47},
                ('CDD BELIGHT', 'MARINGA'): {'Meta_Volume': 0, 'Meta_Positivacao': 43}, 
                ('CDD BELIGHT', 'TROPICAL'): {'Meta_Volume': 0, 'Meta_Positivacao': 43},
                ('CDD BELIGHT', 'CASCAVEL'): {'Meta_Volume': 0, 'Meta_Positivacao': 58},
                ('CDD BELIGHT', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 0, 'Meta_Positivacao': 18},       
                ('CDD BELIGHT', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 0, 'Meta_Positivacao': 29},       

                ('GRAN RESERVA ', 'PILS'): {'Meta_Volume': 0, 'Meta_Positivacao': 0},
                ('GRAN RESERVA ', 'BAGGIO'): {'Meta_Volume': 0, 'Meta_Positivacao': 0},
                ('GRAN RESERVA ', 'LONDRINA'): {'Meta_Volume': 0, 'Meta_Positivacao': 0},
                ('GRAN RESERVA ', 'MARINGA'): {'Meta_Volume': 0, 'Meta_Positivacao': 0},  # #RESERVADO, CASILLERO MARQUES TRIVENTO CELLAR DIABLO CDD CARNIVAL CDD BELIGHT GRAN RESERVA 
                ('GRAN RESERVA ', 'TROPICAL'): {'Meta_Volume': 0, 'Meta_Positivacao': 0},
                ('GRAN RESERVA ', 'CASCAVEL'): {'Meta_Volume': 0, 'Meta_Positivacao': 0},
                ('GRAN RESERVA ', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 0, 'Meta_Positivacao': 0},
                ('GRAN RESERVA ', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 0, 'Meta_Positivacao': 0}, 
            }
            # Adicionar metas específicas por marca e equipe
        df_filtered_VCT['Meta_Volume'] = df_filtered_VCT.apply(
            lambda row: meta_por_marca_equipe.get((row['Marca'], row['Nome Equipe']), {'Meta_Volume': 0})['Meta_Volume'], axis=1)
        df_filtered_VCT['Meta_Positivacao'] = df_filtered_VCT.apply(
            lambda row: meta_por_marca_equipe.get((row['Marca'], row['Nome Equipe']), {'Meta_Positivacao': 0})['Meta_Positivacao'], axis=1)

        df_filtered_VCT = df_filtered_VCT[df_filtered_VCT['Marca'] != "PRODUTOS SEM MARCA" ]


        # agrupamento restante
        df_group_fab_a = df_filtered_VCT[df_filtered_VCT['Industria'] == 'VCT'].groupby(['Nome Equipe', 'Marca']).agg(
            Positivacoes=('Cliente', 'nunique'),  # Número de clientes únicos por marca e equipe
            Volume_Total=('Volumes', 'sum'),  # Volume total por marca e equipe
            Meta_Positivacao=('Meta_Positivacao', 'mean'),
            Meta_Volume=('Meta_Volume', 'mean')).reset_index()


        # arrumando formatação 
        df_group_fab_a['Volume_Total'] = df_group_fab_a['Volume_Total'].apply(lambda x: f"{x:.2f}")

        # Criar o gráfico de barras com metas
        fig_volume = go.Figure()

        # Adicionar barras de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Volume_Total'].astype(float),  # Converter para float para gráficos
            name='Volume Total',
            text=df_group_fab_a['Volume_Total'],
            textposition='auto',
            marker_color='#3498db',
            width=0.2 # Ajuste a largura das barras de volume
        ))

            # Adicionar barras de meta de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Meta_Volume'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Volume'],
            textposition='auto',
            marker_color='#90ee90',
            width=0.2  # Ajuste a largura das barras de meta
        ))

        fig_volume.update_layout(
            title=f'Volume VCT equipe: {equipe}',
            xaxis_title='Marcas',
            yaxis_title='Valores',
            barmode='group',
            bargap=0.2, # Espaço entre grupos de barras
            width=800,
            height=600
        )



        fig_positivacao = go.Figure()

        # Adicionar barras de Positivação
        fig_positivacao.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Positivacoes'].astype(float),  # Converter para float para gráficos
            name='Positivacoes',
            text=df_group_fab_a['Positivacoes'],
            textposition='auto',
            marker_color='#3498db',
            width=0.2 # Ajuste a largura das barras de volume
        ))

        # Adicionar barras de meta de volume
        fig_positivacao.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Meta_Positivacao'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Positivacao'],
            textposition='auto',
            marker_color='#90ee90',
            width=0.2  # Ajuste a largura das barras de meta
        ))

        fig_positivacao.update_layout(
            title=f'Positivação VCT equipe: {equipe}',
            xaxis_title='Marcas',
            yaxis_title='Valores',
            barmode='group',
            bargap=0.2, # Espaço entre grupos de barras
            width=800,
            height=600
        )

        caminho_imagem1 = os.path.join(pasta_graficos, f"Posit_{equipe}_{nome_arquivo}__{hoje}.png")
        caminho_imagem2 = os.path.join(pasta_graficos, f"Vol_{equipe}_{nome_arquivo}__{hoje}.png")

        # mandando gráficos.
        pio.kaleido.scope.chromium_args += ("--single-process",) # imagem estática 
        fig_positivacao.write_image(caminho_imagem1) 
        fig_volume.write_image(caminho_imagem2)
        
def campari_graph(df, equipe):
        pasta_graficos = os.path.join('graficos')
        # nome que será usado dentro do arquivo do grafico.
        nome_arquivo = 'Campari'
        # Criando cópia para não dar erro:
        df_filtered_CAMPARI = df[(df['Industria'] == 'CAMPARI') & (df['Nome Equipe'] == equipe)].copy()
        # Meta marca 
        meta_por_marca_equipe = {
                ('APEROL', 'PILS'): {'Meta_Volume': 168, 'Meta_Positivacao': 353},
                ('APEROL', 'BAGGIO'): {'Meta_Volume': 84, 'Meta_Positivacao': 101},
                ('APEROL', 'LONDRINA'): {'Meta_Volume': 84, 'Meta_Positivacao' : 174},
                ('APEROL', 'MARINGA'): {'Meta_Volume': 84, 'Meta_Positivacao': 174},   
                ('APEROL', 'TROPICAL'): {'Meta_Volume': 84, 'Meta_Positivacao': 202},
                ('APEROL', 'CASCAVEL'): {'Meta_Volume': 168, 'Meta_Positivacao': 32},
                ('APEROL', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 658, 'Meta_Positivacao': 84},
                ('APEROL', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 70, 'Meta_Positivacao': 134},
            
                ('SAGATIBA', 'PILS'): {'Meta_Volume': 41, 'Meta_Positivacao': 192},
                ('SAGATIBA', 'BAGGIO'): {'Meta_Volume': 21, 'Meta_Positivacao': 55},
                ('SAGATIBA', 'LONDRINA'): {'Meta_Volume': 21, 'Meta_Positivacao' : 89},
                ('SAGATIBA', 'MARINGA'): {'Meta_Volume': 21, 'Meta_Positivacao': 89},   
                ('SAGATIBA', 'TROPICAL'): {'Meta_Volume': 21, 'Meta_Positivacao': 109},
                ('SAGATIBA', 'CASCAVEL'): {'Meta_Volume': 41, 'Meta_Positivacao': 120},
                ('SAGATIBA', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 17, 'Meta_Positivacao': 46},
                ('SAGATIBA', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 161, 'Meta_Positivacao': 73},

                ('CAMPARI', 'PILS'): {'Meta_Volume': 764, 'Meta_Positivacao': 1033},
                ('CAMPARI', 'BAGGIO'): {'Meta_Volume': 382, 'Meta_Positivacao': 295},
                ('CAMPARI', 'LONDRINA'): {'Meta_Volume': 382, 'Meta_Positivacao' : 420},
                ('CAMPARI', 'MARINGA'): {'Meta_Volume': 382, 'Meta_Positivacao': 490},   
                ('CAMPARI', 'TROPICAL'): {'Meta_Volume': 382, 'Meta_Positivacao': 590},
                ('CAMPARI', 'CASCAVEL'): {'Meta_Volume': 764, 'Meta_Positivacao': 700},
                ('CAMPARI', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 2994, 'Meta_Positivacao': 11},
                ('CAMPARI', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 319, 'Meta_Positivacao': 394},

                ('SKYY', 'PILS'): {'Meta_Volume': 46, 'Meta_Positivacao': 227},
                ('SKYY', 'BAGGIO'): {'Meta_Volume': 23, 'Meta_Positivacao': 65},
                ('SKYY', 'LONDRINA'): {'Meta_Volume': 23, 'Meta_Positivacao' : 104},
                ('SKYY', 'MARINGA'): {'Meta_Volume': 23, 'Meta_Positivacao': 104},   
                ('SKYY', 'TROPICAL'): {'Meta_Volume': 23, 'Meta_Positivacao': 130},
                ('SKYY', 'CASCAVEL'): {'Meta_Volume': 46, 'Meta_Positivacao': 140},
                ('SKYY', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 181, 'Meta_Positivacao': 54},
                ('SKYY', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 19, 'Meta_Positivacao': 86},
        }

        # meta mercado 
        meta_mercado = {
                ('5 A 10+ CHECKS', 'PILS'): {'Meta_Volume': 0, 'Meta_Positivacao': 41},
                ('5 A 10+ CHECKS', 'BAGGIO'): {'Meta_Volume': 0, 'Meta_Positivacao': 12},
                ('5 A 10+ CHECKS', 'LONDRINA'): {'Meta_Volume': 0, 'Meta_Positivacao' : 26},
                ('5 A 10+ CHECKS', 'MARINGA'): {'Meta_Volume': 0, 'Meta_Positivacao': 24},   
                ('5 A 10+ CHECKS', 'TROPICAL'): {'Meta_Volume': 0, 'Meta_Positivacao': 24},
                ('5 A 10+ CHECKS', 'CASCAVEL'): {'Meta_Volume': 0, 'Meta_Positivacao': 32},
                ('5 A 10+ CHECKS', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 0, 'Meta_Positivacao': 10},
                ('5 A 10+ CHECKS', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 0, 'Meta_Positivacao': 16},
        }

            # Exemplo do DataFrame original de equipes
        todas_as_equipes = pd.DataFrame({'Nome Equipe': ['BAGGIO', 'PILS', 'TROPICAL', 'LONDRINA', 'MARINGA', 'CASCAVEL', 'KEY ACCOUNT PR ON', 'KEY ACCOUNT PR OFF']})

        # Agrupar quartetos
        grouped = df_filtered_CAMPARI.groupby(['Nome Equipe', 'Cliente'])['Marca'].apply(lambda x: set(x))

        # Filtrar clientes que compraram todas as 4 marcas
        marcas_requeridas = {'CAMPARI', 'SAGATIBA', 'SKYY', 'APEROL'}
        quartetos = grouped[grouped.apply(lambda x: marcas_requeridas.issubset(x))]

        # Contar o número de quartetos por equipe
        quartetos_por_equipe = quartetos.groupby('Nome Equipe').count().reset_index()
        quartetos_por_equipe.columns = ['Nome Equipe', 'Quantidade_de_Quartetos']

        # Garantir que todas as equipes estão presentes (mesmo com 0 quartetos)
        quartetos_por_equipe = todas_as_equipes.merge(quartetos_por_equipe, on='Nome Equipe', how='left')

        # Substituir valores NaN por 0, para equipes que não tiveram quartetos
        quartetos_por_equipe['Quantidade_de_Quartetos'] = quartetos_por_equipe['Quantidade_de_Quartetos'].fillna(0)

        # Mapeando metas de quarteto
        mapeamento_meta_quarteto = {'BAGGIO': 5, 'PILS': 19, 'TROPICAL': 11, 'LONDRINA': 12, 'MARINGA': 11, 'CASCAVEL': 14, 'KEY ACCOUNT PR ON': 7, 'KEY ACCOUNT PR OFF': 5} 
        quartetos_por_equipe['Meta_quarteto'] = quartetos_por_equipe['Nome Equipe'].map(mapeamento_meta_quarteto)

        # nomeando para aparecer no grafico
        quartetos_por_equipe['Nome'] = 'Quarteto'

        # Filtrar pela equipe fornecida
        quartetos_por_equipe_filtrado = quartetos_por_equipe[quartetos_por_equipe['Nome Equipe'] == equipe]

        # aplicando mapeamento. 
        df_filtered_CAMPARI['Meta_Volume'] = df_filtered_CAMPARI.apply(
            lambda row: meta_por_marca_equipe.get((row['Marca'], row['Nome Equipe']), {'Meta_Volume': 0})['Meta_Volume'], axis=1)
            
        df_filtered_CAMPARI['Meta_Positivacao'] = df_filtered_CAMPARI.apply(
            lambda row: meta_por_marca_equipe.get((row['Marca'], row['Nome Equipe']), {'Meta_Positivacao': 0})['Meta_Positivacao'], axis=1)

        df_filtered_CAMPARI['meta_positivacao_checkouts'] = df_filtered_CAMPARI.apply(
            lambda row: meta_mercado.get((row['Estabelecimento'], row['Nome Equipe']), {'Meta_Positivacao': 0})['Meta_Positivacao'], axis=1)
            
            # filtro para cada grupo
        df_mercado = df_filtered_CAMPARI[df_filtered_CAMPARI['Estabelecimento'] != "XXXX" ]
        df_marcas = df_filtered_CAMPARI[df_filtered_CAMPARI['Marca'] != "PRODUTOS SEM MARCA" ]


            # agrupamento restante
        df_group_fab_a = df_marcas[df_marcas['Industria'] == 'CAMPARI'].groupby(['Nome Equipe', 'Marca']).agg(
            Positivacoes=('Cliente', 'nunique'),  # Número de clientes únicos por marca e equipe
            Volume_Total=('Volumes', 'sum'),  # Volume total por marca e equipe
            Meta_Positivacao=('Meta_Positivacao', 'mean'),
            Meta_Volume=('Meta_Volume', 'mean')).reset_index()
            

        # formatando volume
        df_group_fab_a['Volume_Total'] = df_group_fab_a['Volume_Total'].apply(lambda x: f"{x:.2f}")

        # agrupando 5 a 10 chekouts 
        df_group_checkouts = df_mercado[df_mercado['Industria'] == 'CAMPARI'].groupby(['Nome Equipe', 'Estabelecimento']).agg(
            positivacao_checkouts = ('Cliente', 'nunique'), 
            meta_positivacao_checkouts = ('meta_positivacao_checkouts', 'mean')).reset_index()

        # Criar o gráfico de barras com metas
        fig_volume = go.Figure()

        # Adicionar barras de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Volume_Total'].astype(float),  # Converter para float para gráficos
            name='Volume Total',
            text=df_group_fab_a['Volume_Total'],
            textposition='auto',
            marker_color='#3498db',
            width=0.2 # Ajuste a largura das barras de volume
        ))

        # Adicionar barras de meta de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Meta_Volume'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Volume'],
            textposition='auto',
            marker_color='#90ee90',
            width=0.2  # Ajuste a largura das barras de meta
        ))

        fig_volume.update_layout(
            title=f'Volume equipe: {equipe}',
            xaxis_title='Marcas',
            yaxis_title='Valores',
            barmode='group',
            bargap=0.2, # Espaço entre grupos de barras
            width=1000,
            height=800
        )


        fig_positivacao = go.Figure()

        # Adicionar barras de Positivação
        fig_positivacao.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Positivacoes'].astype(float),  # Converter para float para gráficos
            name='Positivacoes',
            text=df_group_fab_a['Positivacoes'],
            textposition='auto',
            marker_color='#3498db',
        ))

            # Meta positivação 
        fig_positivacao.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Meta_Positivacao'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Positivacao'],
            textposition='auto',
            marker_color='#90ee90'
        ))


            # positivação checkouts
        fig_positivacao.add_trace(go.Bar(
            x=df_group_checkouts['Estabelecimento'],
            y=df_group_checkouts['positivacao_checkouts'].astype(float),  # Converter para float para gráficos
            name='Positivação',
            text=df_group_checkouts['positivacao_checkouts'],
            textposition='auto',
            marker_color='#3498db',
            showlegend=False
        ))

            # meta positivacao checkouts
        fig_positivacao.add_trace(go.Bar(
            x=df_group_checkouts['Estabelecimento'],
            y=df_group_checkouts['meta_positivacao_checkouts'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_checkouts['meta_positivacao_checkouts'],
            textposition='auto',
            marker_color='#90ee90',
            showlegend=False
        ))

            # positivação quarteto
        fig_positivacao.add_trace(go.Bar(
            x=quartetos_por_equipe_filtrado['Nome'],
            y=quartetos_por_equipe_filtrado['Quantidade_de_Quartetos'],  # Nome correto da coluna
            name='Quarteto',
            text=quartetos_por_equipe_filtrado['Quantidade_de_Quartetos'],  # Nome correto da coluna
            textposition='auto',
            marker_color='#3498db',     
            showlegend=False       
        ))


            # Meta Positivação quarteto
        fig_positivacao.add_trace(go.Bar(
            x=quartetos_por_equipe_filtrado['Nome'],
            y=quartetos_por_equipe_filtrado['Meta_quarteto'].astype(float),
            name='Meta',
            text=quartetos_por_equipe_filtrado['Meta_quarteto'],
            textposition='auto',
            marker_color='#90ee90',
            showlegend=False
        ))
            


        fig_positivacao.update_layout(
            title=f'Positivação equipe: {equipe}',
            xaxis_tickangle =- 45,
            yaxis = dict(
                title = 'Positivações',
                titlefont_size = 16,
                tickfont_size=14,
            ),
            legend = dict(
                x = 0,
                y=1.0,
                bgcolor = 'rgba(255, 255, 255, 0)' , 
                bordercolor = 'rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.1, # Espaço entre grupos de barras
            width=1000,
            height=800,
            bargroupgap = 0.1
        )
        

        caminho_imagem1 = os.path.join(pasta_graficos, f"Posit_{equipe}_{nome_arquivo}__{hoje}.png")
        caminho_imagem2 = os.path.join(pasta_graficos, f"Vol_{equipe}_{nome_arquivo}__{hoje}.png")

        # mandando gráficos.
        pio.kaleido.scope.chromium_args += ("--single-process",) # imagem estática 
        fig_positivacao.write_image(caminho_imagem1) 
        fig_volume.write_image(caminho_imagem2)

def pernod_graph(df, equipe):
        pasta_graficos = os.path.join('graficos')
        # nome que será usado dentro do arquivo do grafico.
        nome_arquivo = 'Pernod'
        # Criando cópia para não dar erro:
        df_filtered_PERNOD= df[(df['Industria'] == 'PERNOD') & (df['Nome Equipe'] == equipe)].copy()

        # Meta marca
        meta_por_marca_equipe = {
                ('CHIVAS', 'PILS'): {'Meta_Volume': 30, 'Meta_Positivacao': 43},
                ('CHIVAS', 'BAGGIO'): {'Meta_Volume': 16, 'Meta_Positivacao': 29},
                ('CHIVAS', 'LONDRINA'): {'Meta_Volume': 16, 'Meta_Positivacao' : 23},
                ('CHIVAS', 'MARINGA'): {'Meta_Volume': 16, 'Meta_Positivacao': 23},   
                ('CHIVAS', 'TROPICAL'): {'Meta_Volume': 16, 'Meta_Positivacao': 23},
                ('CHIVAS', 'CASCAVEL'): {'Meta_Volume': 23, 'Meta_Positivacao': 31},
                ('CHIVAS', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 81, 'Meta_Positivacao': 8},
                ('CHIVAS', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 32, 'Meta_Positivacao': 19},
            
                ('BALLANTINES', 'PILS'): {'Meta_Volume': 39, 'Meta_Positivacao': 65},
                ('BALLANTINES', 'BAGGIO'): {'Meta_Volume': 21, 'Meta_Positivacao': 44},
                ('BALLANTINES', 'LONDRINA'): {'Meta_Volume': 21, 'Meta_Positivacao' : 35},
                ('BALLANTINES', 'MARINGA'): {'Meta_Volume': 21, 'Meta_Positivacao': 35},   
                ('BALLANTINES', 'TROPICAL'): {'Meta_Volume': 21, 'Meta_Positivacao': 35},
                ('BALLANTINES', 'CASCAVEL'): {'Meta_Volume': 30, 'Meta_Positivacao': 47},
                ('BALLANTINES', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 105, 'Meta_Positivacao': 11},
                ('BALLANTINES', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 42, 'Meta_Positivacao': 29},

                ('ABSOLUT', 'PILS'): {'Meta_Volume': 46, 'Meta_Positivacao': 108},
                ('ABSOLUT', 'BAGGIO'): {'Meta_Volume': 25, 'Meta_Positivacao': 73},
                ('ABSOLUT', 'LONDRINA'): {'Meta_Volume': 25, 'Meta_Positivacao' : 58},
                ('ABSOLUT', 'MARINGA'): {'Meta_Volume': 25, 'Meta_Positivacao': 58},   
                ('ABSOLUT', 'TROPICAL'): {'Meta_Volume': 25, 'Meta_Positivacao': 58},
                ('ABSOLUT', 'CASCAVEL'): {'Meta_Volume': 35, 'Meta_Positivacao': 78},
                ('ABSOLUT', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 123, 'Meta_Positivacao': 19},
                ('ABSOLUT', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 49, 'Meta_Positivacao': 48},

                ('BEEFEATER', 'PILS'): {'Meta_Volume': 13, 'Meta_Positivacao': 43},
                ('BEEFEATER', 'BAGGIO'): {'Meta_Volume': 7, 'Meta_Positivacao': 29},
                ('BEEFEATER', 'LONDRINA'): {'Meta_Volume': 7, 'Meta_Positivacao' : 23},
                ('BEEFEATER', 'MARINGA'): {'Meta_Volume': 7, 'Meta_Positivacao': 23},     # metas outras marcas
                ('BEEFEATER', 'TROPICAL'): {'Meta_Volume': 7, 'Meta_Positivacao': 23},
                ('BEEFEATER', 'CASCAVEL'): {'Meta_Volume': 10, 'Meta_Positivacao': 31},
                ('BEEFEATER', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 35, 'Meta_Positivacao': 8},
                ('BEEFEATER', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 14, 'Meta_Positivacao': 19},
        }

        Meta_nacional = {
                ('NACIONAL', 'PILS'): {'Meta_Volume': 286},
                ('NACIONAL', 'BAGGIO'): {'Meta_Volume': 154},
                ('NACIONAL', 'LONDRINA'): {'Meta_Volume': 154},
                ('NACIONAL', 'MARINGA'):{'Meta_Volume': 154},      # meta nacional 
                ('NACIONAL', 'TROPICAL'): {'Meta_Volume': 154},
                ('NACIONAL', 'CASCAVEL'): {'Meta_Volume': 220 },
                ('NACIONAL', 'KEY ACCOUNT PR OFF'): {'Meta_Volume': 770},
                ('NACIONAL', 'KEY ACCOUNT PR ON'): {'Meta_Volume': 308}
        }

        meta_pernod_geral = {'BAGGIO': 496, 'PILS': 734, 'TROPICAL': 394, 'LONDRINA': 394, 'MARINGA': 394, 'CASCAVEL': 530, 'KEY ACCOUNT PR ON': 326, 'KEY ACCOUNT PR OFF': 129} 

             # Exemplo do DataFrame original de equipes
        todas_as_equipes = pd.DataFrame({'Nome Equipe': ['BAGGIO', 'PILS', 'TROPICAL', 'LONDRINA', 'MARINGA', 'CASCAVEL', 'KEY ACCOUNT PR ON', 'KEY ACCOUNT PR OFF']})

        marcas_requeridas = {'BEEFEATER', 'ABSOLUT', 'BALLETINES', 'CHIVAS'}

             # aplicando mapeamento. 
        df_filtered_PERNOD['Meta_Volume_marcas'] = df_filtered_PERNOD.apply(
            lambda row: meta_por_marca_equipe.get((row['Marca'], row['Nome Equipe']), {'Meta_Volume': 0})['Meta_Volume'], axis=1)
            
        df_filtered_PERNOD['Meta_Positivacao_marcas'] = df_filtered_PERNOD.apply(
            lambda row: meta_por_marca_equipe.get((row['Marca'], row['Nome Equipe']), {'Meta_Positivacao': 0})['Meta_Positivacao'], axis=1)

        df_filtered_PERNOD['Meta_positiva_geral'] = df_filtered_PERNOD['Nome Equipe'].map(meta_pernod_geral)

        df_filtered_PERNOD['Meta_Volume_nacional'] = df_filtered_PERNOD.apply(
            lambda row: Meta_nacional.get((row['Nacional?'], row['Nome Equipe']), {'Meta_Volume': 0})['Meta_Volume'], axis=1)

        # df para marcas 
        df_filtered_PERNOD_marcas = df_filtered_PERNOD[~df_filtered_PERNOD['Marca'].isin(["NATU", "ORLOFF", "PASSPORT", "DOMECQ", "SAO FRANCISCO", "PRODUTOS SEM MARCA"])]

        # df para nacional
        df_filtered_PERNOD = df_filtered_PERNOD[df_filtered_PERNOD['Nacional?'] != "XXXXXX" ]

 
            # agrupamento das marcas
        df_group_fab_a = df_filtered_PERNOD_marcas[df_filtered_PERNOD_marcas['Industria'] == 'PERNOD'].groupby(['Nome Equipe', 'Marca']).agg(
            Positivacoes=('Cliente', 'nunique'),  # Número de clientes únicos por marca e equipe
            Volume_Total=('Volumes', 'sum'),  # Volume total por marca e equipe
            Meta_Positivacao_marcas=('Meta_Positivacao_marcas', 'mean'),
            Meta_Volume_marcas=('Meta_Volume_marcas', 'mean')).reset_index()
            
        # positivação geral 
        df_posi_geral = df_filtered_PERNOD.groupby(['Nome Equipe', 'Industria']).agg(
            positivacao_geral = ('Cliente', 'nunique'),
            Meta_positiva_geral = ('Meta_positiva_geral', 'mean')).reset_index()

            # volume nacional
        df_group_nacional = df_filtered_PERNOD[df_filtered_PERNOD['Industria'] == 'PERNOD'].groupby(['Nome Equipe','Nacional?']).agg(
            Meta_Volume_nacional = ('Meta_Volume_nacional','mean'),
            volume_nacional = ('Volumes','sum')).reset_index()


        # formatando volume
        df_group_fab_a['Volume_Total'] = df_group_fab_a['Volume_Total'].apply(lambda x: f"{x:.2f}")
        df_group_nacional['volume_nacional'] = df_group_nacional['volume_nacional'].apply(lambda x: f"{x:.2f}")


        # Criar o gráfico de barras com metas
        fig_volume = go.Figure()

        # Adicionar barras de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_nacional['Nacional?'],
            y=df_group_nacional['volume_nacional'].astype(float),  # Converter para float para gráficos
            name='Volume Total',
            text=df_group_nacional['volume_nacional'],
            textposition='auto',
            marker_color='#3498db',
            width=0.2, # Ajuste a largura das barras de volume
            showlegend=False
        ))

        # Adicionar barras de meta de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_nacional['Nacional?'],
            y=df_group_nacional['Meta_Volume_nacional'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_nacional['Meta_Volume_nacional'],
            textposition='auto',
            marker_color='#90ee90',
            width=0.2, # Ajuste a largura das barras de meta
            showlegend=False
        ))

            # Adicionar barras de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Volume_Total'].astype(float),  # Converter para float para gráficos
            name='Volume Total',
            text=df_group_fab_a['Volume_Total'],
            textposition='auto',
            marker_color='#3498db',
            width=0.2 # Ajuste a largura das barras de volume
        ))

            # Adicionar barras de meta de volume
        fig_volume.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Meta_Volume_marcas'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Volume_marcas'],
            textposition='auto',
            marker_color='#90ee90',
            width=0.2  # Ajuste a largura das barras de meta
        ))

        ### trace volume nacional

        fig_volume.update_layout(
            title=f'Volume PERNOD equipe: {equipe}',
            xaxis_tickangle =- 45,
            yaxis = dict(
                title = 'Positivações',
                titlefont_size = 16,
                tickfont_size=14,
            ),
            legend = dict(
                x = -0.2,
                y=1.0,
                bgcolor = 'rgba(255, 255, 255, 0)' , 
                bordercolor = 'rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.1, # Espaço entre grupos de barras
            width=900,
            height=700,
            bargroupgap = 0.1
        )

        fig_positivacao = go.Figure()

        # Adicionar barras de Positivação geral pernod
        fig_positivacao.add_trace(go.Bar(
            x=df_posi_geral['Industria'],
            y=df_posi_geral['positivacao_geral'].astype(float),  # Converter para float para gráficos
            name='Positivacoes',
            text=df_posi_geral['positivacao_geral'],
            textposition='auto',
            marker_color='#3498db'
        ))

        # Meta positivação geral pernod
        fig_positivacao.add_trace(go.Bar(
            x=df_posi_geral['Industria'],
            y=df_posi_geral['Meta_positiva_geral'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_posi_geral['Meta_positiva_geral'],
            textposition='auto',
            marker_color='#90ee90'
        ))

        # Adicionar barras de Positivação marca pernod
        fig_positivacao.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Positivacoes'].astype(float),  # Converter para float para gráficos
            name='Positivacoes',
            text=df_group_fab_a['Positivacoes'],
            textposition='auto',
            marker_color='#3498db',
            showlegend=False
        ))

        # Meta positivação marca pernod
        fig_positivacao.add_trace(go.Bar(
            x=df_group_fab_a['Marca'],
            y=df_group_fab_a['Meta_Positivacao_marcas'].astype(float),  # Converter para float para gráficos
            name='Meta',
            text=df_group_fab_a['Meta_Positivacao_marcas'],
            textposition='auto',
            marker_color='#90ee90',
            showlegend=False
        ))

        fig_positivacao.update_layout(
            title=f'Positivação PERNOD equipe: {equipe}',
            xaxis_tickangle =- 45,
                yaxis = dict(
                title = 'Positivações',
                titlefont_size = 16,
                tickfont_size=14,
            ),
            legend = dict(
                x = -0.2,
                y=1.0,
                bgcolor = 'rgba(255, 255, 255, 0)' , 
                bordercolor = 'rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.1, # Espaço entre grupos de barras
            width=900,
            height=700,
            bargroupgap = 0.1
        )

        caminho_imagem1 = os.path.join(pasta_graficos, f"Posit_{equipe}_{nome_arquivo}__{hoje}.png")
        caminho_imagem2 = os.path.join(pasta_graficos, f"Vol_{equipe}_{nome_arquivo}__{hoje}.png")

        # mandando gráficos.
        pio.kaleido.scope.chromium_args += ("--single-process",) # imagem estática 
        fig_positivacao.write_image(caminho_imagem1) 
        fig_volume.write_image(caminho_imagem2)
