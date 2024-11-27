# Importação relativa de 'analytics' para evitar problemas de caminho absoluto
from .analytics import *
import plotly.graph_objects as go




def graph_hnk():
    clientes_por_mes = clean_data_hnk_geral()[0]
    volume_por_mes = clean_data_hnk_geral()[2]

    fig_posi_geral = go.Figure()

    # Adicionar linha para Clientes
    fig_posi_geral.add_trace(go.Scatter(
        x=clientes_por_mes['Mês'], 
        y=clientes_por_mes['Cliente'], 
        mode='lines+markers', 
        name='Positivações', 
        line=dict(color='green', width=2), 
        marker=dict(size=8, color='black')
    ))

    # Configurar layout do gráfico
    fig_posi_geral.update_layout(
        title='Número de Positivações por Mês',
        xaxis_title='Mês',
        yaxis_title='Número de Positivações',
        template='plotly',
        showlegend=True,
        xaxis=dict(
            title_font=dict(size=14, family='Arial', color='black'),  # Título do eixo X
            tickfont=dict(size=16, family='Arial', color='black')  # Aumentar o tamanho dos rótulos do eixo X
        ),
        yaxis=dict(
            title_font=dict(size=14, family='Arial', color='black'),  # Título do eixo Y
            tickfont=dict(size=12, family='Arial', color='black')  # Tamanho dos rótulos do eixo Y
        )
    )

    fig_volume_geral = go.Figure()

    # Adicionar linha para Clientes
    fig_volume_geral.add_trace(go.Scatter(
        x=volume_por_mes['Mês'], 
        y=volume_por_mes['Hecto total'], 
        mode='lines+markers', 
        name='Hectolitros', 
        line=dict(color='green', width=2), 
        marker=dict(size=8, color='black')
    ))

    # Configurar layout do gráfico
    fig_volume_geral.update_layout(
        title='Número de Hectolitros por Mês',
        xaxis_title='Mês',
        yaxis_title='Número de Hectolitros',
        template='plotly',
        showlegend=True,
        xaxis=dict(
            title_font=dict(size=14, family='Arial', color='black'),  # Título do eixo X
            tickfont=dict(size=16, family='Arial', color='black')  # Aumentar o tamanho dos rótulos do eixo X
        ),
        yaxis=dict(
            title_font=dict(size=14, family='Arial', color='black'),  # Título do eixo Y
            tickfont=dict(size=12, family='Arial', color='black')  # Tamanho dos rótulos do eixo Y
        )
    )
    return fig_posi_geral, fig_volume_geral
